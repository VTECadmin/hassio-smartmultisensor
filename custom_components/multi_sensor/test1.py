"""Support for Multisensor integration, heavily based on megakid/ha_hildebrand_glow_ihd_mqtt"""

import json
import re
import logging

from homeassistant.components import mqtt
from homeassistant.components.mqtt.models import PublishMessage
from homeassistant.components.switch import SwitchEntity

ALARM_BUTTON = [
    {
        "name": "Alarm_button",
        "func": lambda js: js['value']
    }
]

class Testcase(SwitchEntity, Multisensor):

    def __init__(self, hass, name, mqtt_in, mqtt_out, mac, uid, ip_address):
        Multisensor.__init__(
            self=self,
            hass=hass,
            name=name,
            mqtt_in=mqtt_in,
            mqtt_out=mqtt_out,
            mac=mac,
            uid=uid,
            ip_address=ip_address,
        )
        self._is_on = False

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""
        await mqtt.async_publish(
            hass=self._hass,
            topic=self._out_topic("/multisensor/MS-IPe0e2e6742eff/peripherals/sound/POST"),
            payload="{"mode" : "ON", "duration" : 1000}"
            retain=False,
        )  