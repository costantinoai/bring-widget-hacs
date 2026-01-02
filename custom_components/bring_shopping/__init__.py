"""The Bring! Shopping Card integration."""
from __future__ import annotations

import logging

from bring_api import Bring, BringAuthException, BringRequestException

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN
from .coordinator import BringDataUpdateCoordinator
from .websocket_api import async_register_websocket_api

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.TODO]

type BringConfigEntry = ConfigEntry[BringDataUpdateCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool:
    """Set up Bring! Shopping Card from a config entry."""
    email = entry.data[CONF_EMAIL]
    password = entry.data[CONF_PASSWORD]

    session = async_get_clientsession(hass)
    bring = Bring(session, email, password)

    try:
        await bring.login()
    except BringAuthException as err:
        raise ConfigEntryAuthFailed("Invalid credentials") from err
    except BringRequestException as err:
        raise ConfigEntryNotReady(f"Failed to connect to Bring: {err}") from err
    except Exception as err:
        raise ConfigEntryNotReady(f"Unexpected error: {err}") from err

    # Create coordinator
    coordinator = BringDataUpdateCoordinator(hass, bring)

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator in runtime data
    entry.runtime_data = coordinator

    # Register WebSocket API
    async_register_websocket_api(hass)

    # Forward setup to platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: BringConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
