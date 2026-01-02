# Publishing to the HACS default store

This repository contains both:

- a Home Assistant **integration** (`custom_components/bring_shopping`)
- a Lovelace **plugin/card** (`bring-shopping-card.js`, built from `src/` into `dist/`)

To make it available to all users in the HACS marketplace ("Explore & Download"), you need to get it included in the HACS **default** store and meet the publishing requirements.

## 1) One-time GitHub repo setup

- Ensure the repo is public, has a description, and issues are enabled.
- Add GitHub topics (HACS checks that topics exist). Suggested topics:
  - `home-assistant`, `hacs`
  - `integration`, `plugin`, `lovelace`
  - `bring`, `shopping`, `grocery`, `groceries`, `shopping-list`

## 2) Make sure automated checks pass

This repo includes GitHub Actions workflows to validate:

- `HACS (Integration)` (`.github/workflows/hacs.yml`)
- `HACS (Plugin)` (`.github/workflows/hacs-plugin.yml`)
- `Hassfest` (`.github/workflows/hassfest.yml`)

Before submitting to the default store, the HACS Action must pass without errors or ignores.

## 3) Home Assistant Brands (required for integrations)

For default-store inclusion as an integration, HACS requires the integration to be added to `home-assistant/brands`.

Prepared artwork is included here:

- `brands/custom_integrations/bring_shopping/icon.png`
- `brands/custom_integrations/bring_shopping/logo.png`

Submit a PR to `https://github.com/home-assistant/brands` adding those files under:

- `custom_integrations/bring_shopping/icon.png`
- `custom_integrations/bring_shopping/logo.png`

## 4) Releases (required in practice)

HACS expects your repository to have at least one GitHub Release.

This repo includes a release workflow (`.github/workflows/release.yml`) that:

- builds the frontend bundle
- attaches `dist/bring-shopping-card.js` to the GitHub Release as `bring-shopping-card.js`

Release checklist:

- bump `custom_components/bring_shopping/manifest.json` `version`
- create a git tag (`vX.Y.Z` recommended)
- push the tag to GitHub
- verify the GitHub Release contains the `bring-shopping-card.js` asset

## 5) Submit to HACS default

The default repositories list is maintained in `https://github.com/hacs/default`.

Because this repo provides both an integration and a plugin, submit it in both places:

- add the repo URL to `./integration`
- add the repo URL to `./plugin`

Follow the PR template carefully; reviews can take time (often weeks/months).

