# Bring! Shopping Card for Home Assistant

A beautiful, modern shopping list card for [Bring!](https://www.getbring.com/) - fully integrated with Home Assistant.

> **Disclaimer**: This project is not affiliated with, endorsed by, or connected to Bring! Labs AG or the official Bring! app.

## Features

- **Beautiful Dark Theme** - Modern design that looks great on any dashboard
- **Real Product Images** - Fetches images from Bring CDN with emoji fallback
- **Multiple Lists** - Switch between your Bring! lists with a dropdown
- **Drag & Drop Reordering** - Organize your shopping list your way
- **Dynamic Search** - Filter items as you type with live suggestions
- **Multiple Sort Options** - Manual, A-Z, By Category, Recently Added
- **Item Notes** - Add specifications like "2 lbs" or "organic"
- **Quick Add** - One-tap add from recently purchased items
- **Auto-Refresh** - Syncs every 60 seconds
- **Native HA Theming** - Adapts to your Home Assistant theme

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to **Integrations** → **+ Explore & Download Repositories**
3. Search for "Bring! Shopping Card"
4. Click **Download**
5. Restart Home Assistant
6. Add the integration: **Settings** → **Devices & Services** → **+ Add Integration** → "Bring! Shopping Card"
7. Enter your Bring! email and password
8. Add the card to your dashboard

### Manual Installation

1. Download `bring-shopping-card.js` from the [latest release](https://github.com/costantinoai/bring-widget-hacs/releases)
2. Copy to `/config/www/bring-shopping-card.js`
3. Add the resource in **Settings** → **Dashboards** → **Resources**:
   ```yaml
   url: /local/bring-shopping-card.js
   type: module
   ```
4. Copy `custom_components/bring_shopping/` to your `/config/custom_components/` directory
5. Restart Home Assistant
6. Add the integration and card as described above

## Card Configuration

Add the card to your dashboard:

```yaml
type: custom:bring-shopping-card
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `title` | string | List name | Custom card title |
| `show_recently` | boolean | `true` | Show quick-add section |
| `show_available` | boolean | `true` | Show all items by category |
| `max_quick_items` | number | `12` | Maximum items in quick-add section |
| `sort_default` | string | `manual` | Default sort: `manual`, `alpha`, `category`, `recent` |

### Example

```yaml
type: custom:bring-shopping-card
title: Groceries
show_recently: true
show_available: false
max_quick_items: 8
sort_default: category
```

## Multiple Lists

If you have multiple Bring! lists, a dropdown appears in the card header. Click the list name to switch between lists. Your selection is remembered per card.

## Todo Integration

This integration also creates native Home Assistant todo entities for each of your Bring! lists. You can use these with:

- Home Assistant's built-in todo card
- Automations (e.g., "When I arrive at the store, show my shopping list")
- Voice assistants

## Troubleshooting

### Card shows "Failed to connect to Bring! integration"

Make sure you've added the Bring! Shopping Card integration in Settings → Devices & Services.

### Items not syncing

The card refreshes every 60 seconds. Click the refresh button for immediate sync.

### Images not loading

Some items may not have images on Bring's CDN. The card falls back to emoji icons automatically.

## Development

```bash
# Install dependencies
npm install

# Build for production
npm run build

# Watch mode for development
npm run watch
```

## License

MIT License - see [LICENSE](LICENSE) for details.

This project is not affiliated with Bring! Labs AG.
