const { Kafka } = require("kafkajs");
const ip = require('ip')

const kafka = new Kafka({
  clientId: "my-app",
  brokers: [`kafka:9092`],
});

const consumer = kafka.consumer({ groupId: "1" });

async function consume() {
  await consumer.connect();
  await consumer.subscribe({
    topic: "dbserver1.inventory.customers",
    fromBeginning: true,
  });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        value: message.value.toString(),
      });
    },
  });
}

consume()
