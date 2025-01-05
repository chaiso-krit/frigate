import mqtt from "mqtt";

export const publishData = (topic: string, data: string) => {
  const client = mqtt.connect("mqtt://0.0.0.0:1885");

  client.on("connect", () => {
    client.publish(topic, data);
  });

  return "Success";
};
