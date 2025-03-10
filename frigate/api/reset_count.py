from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from frigate.config import FrigateConfig
from frigate.api.defs.tags import Tags

import logging

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

logger = logging.getLogger(__name__)

router = APIRouter(tags=[Tags.reset])

config = FrigateConfig.load()


@router.get("/{camera_name}/reset")
async def reset_camera(camera_name: str):
    payload = "reset"
    topic = f"{camera_name}/reset"
    mqtt_config = config.mqtt
    client = mqtt.Client(
        callback_api_version=CallbackAPIVersion.VERSION2,
        client_id=mqtt_config.client_id,
    )

    try:
        client.connect(mqtt_config.host, mqtt_config.port, 60)
        result = client.publish(
            f"{mqtt_config.topic_prefix}/{topic}", payload, retain=True
        )

        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            return JSONResponse(
                content={
                    "success": False,
                    "message": f"Failed to reset camera {camera_name}",
                },
                status_code=500,
            )

    except Exception as e:
        logger.error(f"Error resetting camera {camera_name}: {e}")
        return JSONResponse(
            content={
                "success": False,
                "message": f"Error resetting camera {camera_name}: {str(e)}",
            },
            status_code=500,
        )
    finally:
        client.disconnect()

    return JSONResponse(
        content={
            "success": True,
            "message": f"Camera {camera_name} reset",
        },
        status_code=200,
    )
