"""Constants for the Bring! Shopping Card integration."""
from typing import Final

DOMAIN: Final = "bring_shopping"

# Configuration keys
CONF_EMAIL: Final = "email"
CONF_PASSWORD: Final = "password"

# Bring CDN base URL for item images
BRING_CDN_BASE: Final = "https://web.getbring.com/assets/images/items/"

# Update interval in seconds
UPDATE_INTERVAL: Final = 60

# WebSocket API commands
WS_TYPE_GET_LISTS: Final = "bring_shopping/get_lists"
WS_TYPE_GET_ITEMS: Final = "bring_shopping/get_items"
WS_TYPE_ADD_ITEM: Final = "bring_shopping/add_item"
WS_TYPE_COMPLETE_ITEM: Final = "bring_shopping/complete_item"
WS_TYPE_UPDATE_ITEM: Final = "bring_shopping/update_item"
WS_TYPE_REORDER_ITEMS: Final = "bring_shopping/reorder_items"

# Attribute names
ATTR_LIST_UUID: Final = "list_uuid"
ATTR_ITEM_NAME: Final = "item_name"
ATTR_ORIGINAL_NAME: Final = "original_name"
ATTR_SPECIFICATION: Final = "specification"
ATTR_ORDER: Final = "order"
