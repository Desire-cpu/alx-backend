import kue from 'kue';

const que = kue.createQueue();
const job = {
  phoneNumber: '0731199417',
  message: 'This account is verified',
};

const queue = 'push_notification_code';

const job = que.create(queue, job).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
