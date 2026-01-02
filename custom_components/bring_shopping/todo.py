"""Todo platform for Bring! Shopping Card."""
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from homeassistant.components.todo import (
    TodoItem,
    TodoItemStatus,
    TodoListEntity,
    TodoListEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import BringDataUpdateCoordinator, BringItem, BringListData

if TYPE_CHECKING:
    from . import BringConfigEntry

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: BringConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Bring! todo entities from a config entry."""
    coordinator = config_entry.runtime_data

    entities = []
    for list_uuid, list_data in coordinator.data.lists.items():
        entities.append(
            BringTodoListEntity(
                coordinator=coordinator,
                list_uuid=list_uuid,
                list_name=list_data.name,
            )
        )

    async_add_entities(entities)


class BringTodoListEntity(CoordinatorEntity[BringDataUpdateCoordinator], TodoListEntity):
    """A Bring! shopping list as a todo entity."""

    _attr_has_entity_name = True
    _attr_supported_features = (
        TodoListEntityFeature.CREATE_TODO_ITEM
        | TodoListEntityFeature.UPDATE_TODO_ITEM
        | TodoListEntityFeature.DELETE_TODO_ITEM
    )

    def __init__(
        self,
        coordinator: BringDataUpdateCoordinator,
        list_uuid: str,
        list_name: str,
    ) -> None:
        """Initialize the todo entity."""
        super().__init__(coordinator)
        self._list_uuid = list_uuid
        self._attr_name = list_name
        self._attr_unique_id = f"{DOMAIN}_{list_uuid}"

    @property
    def _list_data(self) -> BringListData | None:
        """Get the current list data."""
        if self.coordinator.data:
            return self.coordinator.data.lists.get(self._list_uuid)
        return None

    @property
    def todo_items(self) -> list[TodoItem]:
        """Return the todo items."""
        if not self._list_data:
            return []

        items = []

        # Purchase items (to buy) - needs action
        for item in self._list_data.purchase:
            items.append(
                TodoItem(
                    uid=item.original_name,
                    summary=item.name,
                    description=item.specification or None,
                    status=TodoItemStatus.NEEDS_ACTION,
                )
            )

        # Recently completed items
        for item in self._list_data.recently[:10]:  # Limit to 10 recent
            items.append(
                TodoItem(
                    uid=f"recent_{item.original_name}",
                    summary=item.name,
                    description=item.specification or None,
                    status=TodoItemStatus.COMPLETED,
                )
            )

        return items

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Create a new todo item (add to shopping list)."""
        if not item.summary:
            return

        await self.coordinator.async_add_item(
            self._list_uuid,
            item.summary,
            item.description or "",
        )

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Update a todo item."""
        if not item.uid:
            return

        # Handle completion status change
        if item.status == TodoItemStatus.COMPLETED:
            # Item is being marked as completed
            original_name = item.uid.replace("recent_", "")
            await self.coordinator.async_complete_item(
                self._list_uuid,
                original_name,
            )
        else:
            # Update specification
            original_name = item.uid.replace("recent_", "")
            await self.coordinator.async_update_item(
                self._list_uuid,
                original_name,
                item.description or "",
            )

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Delete todo items."""
        for uid in uids:
            original_name = uid.replace("recent_", "")
            await self.coordinator.async_remove_item(
                self._list_uuid,
                original_name,
            )
