from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from frigate.comms.dispatcher import Dispatcher
from frigate.config import FrigateConfig
from frigate.api.defs.tags import Tags

import logging

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

logger = logging.getLogger(__name__)

router = APIRouter(tags=[Tags.reset])

config = FrigateConfig.load()


@router.post("/{camera_name}/reset")
async def reset_camera(camera_name: str):
    topic = f"{camera_name}/reset"
    payload = "reset"
    mqtt_config = config.mqtt
    client = mqtt.Client(
        callback_api_version=CallbackAPIVersion.VERSION2,
        client_id=mqtt_config.client_id,
    )
    
    client.connect(mqtt_config.host, mqtt_config.port, 60)
    
    client.publish(f"{mqtt_config.topic_prefix}/{topic}", payload, retain=True)

    client.disconnect()

    return JSONResponse(
        content={
            "success": True,
            "message": f"Camera {camera_name} reset, Published to {topic}",
        },
        status_code=200,
    )
