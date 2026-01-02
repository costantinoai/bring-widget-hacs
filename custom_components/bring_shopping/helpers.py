"""Helper functions for the Bring! Shopping Card integration."""
from __future__ import annotations

import json
import logging
import urllib.request
from typing import Any

from .const import BRING_CDN_BASE
from .translations_data import (
    CATEGORY_ICONS,
    CATEGORY_TRANSLATIONS,
    DEFAULT_ICON,
    ITEM_ICONS,
)

_LOGGER = logging.getLogger(__name__)

# Cache for translations loaded from Bring
_translations_cache: dict[str, str] = {}


async def load_translations_from_bring() -> dict[str, str]:
    """Load translations from Bring locale files (German -> English)."""
    global _translations_cache

    if _translations_cache:
        return _translations_cache

    try:
        url = "https://web.getbring.com/locale/articles.en-US.json"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            _translations_cache = data
            _LOGGER.debug("Loaded %d translations from Bring", len(_translations_cache))
    except Exception as err:
        _LOGGER.warning("Failed to load translations from Bring: %s", err)
        _translations_cache = {}

    return _translations_cache


def translate(text: str) -> str:
    """Translate German item name to English."""
    if not text:
        return text

    # Check cache from Bring API
    if text in _translations_cache:
        return _translations_cache[text]

    # Return original if no translation found
    return text


def translate_category(category: str) -> str:
    """Translate category name from German to English."""
    if not category:
        return ""
    return CATEGORY_TRANSLATIONS.get(category, category)


def get_image_url(item_name: str) -> str | None:
    """Get CDN image URL for an item."""
    if not item_name:
        return None

    # The CDN uses lowercase names
    clean_name = item_name.lower()
    return f"{BRING_CDN_BASE}{clean_name}.png"


def get_icon_for_item(
    item_name: str,
    icon_id: str | None = None,
    category: str | None = None,
) -> str:
    """Get appropriate emoji icon for an item (fallback when CDN fails)."""
    # Try item name first (both original and translated)
    if item_name in ITEM_ICONS:
        return ITEM_ICONS[item_name]

    translated = translate(item_name)
    if translated in ITEM_ICONS:
        return ITEM_ICONS[translated]

    # Try icon_id (German product name)
    if icon_id:
        if icon_id in ITEM_ICONS:
            return ITEM_ICONS[icon_id]
        translated_icon = translate(icon_id)
        if translated_icon in ITEM_ICONS:
            return ITEM_ICONS[translated_icon]

    # Try category
    if category:
        if category in CATEGORY_ICONS:
            return CATEGORY_ICONS[category]
        translated_cat = translate_category(category)
        if translated_cat in CATEGORY_ICONS:
            return CATEGORY_ICONS[translated_cat]

    return DEFAULT_ICON


def enrich_item(item: dict[str, Any], details_map: dict[str, dict]) -> dict[str, Any]:
    """Enrich a shopping list item with translations, icons, and image URLs."""
    name = item.get("name", "")
    detail = details_map.get(name, {})
    category = detail.get("userSectionId", "")
    icon_item_id = detail.get("userIconItemId", name)

    return {
        "name": translate(name),
        "originalName": name,
        "specification": item.get("specification", ""),
        "icon": get_icon_for_item(name, icon_item_id, category),
        "imageUrl": get_image_url(icon_item_id or name),
        "category": translate_category(category),
    }
