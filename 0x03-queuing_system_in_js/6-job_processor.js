import kue from 'kue';

const q = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

const queueName = 'push_notification_code';

q.process(queueName, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
