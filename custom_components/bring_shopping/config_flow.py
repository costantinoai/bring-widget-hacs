"""Config flow for Bring! Shopping Card integration."""
from __future__ import annotations

import logging
from typing import Any

from bring_api import Bring, BringAuthException, BringRequestException
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_EMAIL): str,
        vol.Required(CONF_PASSWORD): str,
    }
)


class BringShoppingConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bring! Shopping Card."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            session = async_get_clientsession(self.hass)
            bring = Bring(session, user_input[CONF_EMAIL], user_input[CONF_PASSWORD])

            try:
                # Validate credentials by attempting to login
                auth_response = await bring.login()

                # Use the Bring UUID as unique ID
                await self.async_set_unique_id(bring.uuid)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=auth_response.name or user_input[CONF_EMAIL],
                    data=user_input,
                )

            except BringAuthException:
                errors["base"] = "invalid_auth"
            except BringRequestException:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception during Bring setup")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_reauth(
        self, entry_data: dict[str, Any]
    ) -> ConfigFlowResult:
        """Handle reauthorization."""
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle reauthorization confirmation."""
        errors: dict[str, str] = {}

        if user_input is not None:
            session = async_get_clientsession(self.hass)
            bring = Bring(session, user_input[CONF_EMAIL], user_input[CONF_PASSWORD])

            try:
                await bring.login()

                # Update the config entry
                entry = self.hass.config_entries.async_get_entry(
                    self.context["entry_id"]
                )
                if entry:
                    self.hass.config_entries.async_update_entry(
                        entry, data=user_input
                    )
                    await self.hass.config_entries.async_reload(entry.entry_id)

                return self.async_abort(reason="reauth_successful")

            except BringAuthException:
                errors["base"] = "invalid_auth"
            except BringRequestException:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception during reauth")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
