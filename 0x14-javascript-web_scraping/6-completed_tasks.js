#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasks = todos.filter((todo) => todo.completed);

  const users = new Map();

  completedTasks.forEach((todo) => {
    const userId = todo.userId;

    if (!users.has(userId)) {
      users.set(userId, 0);
    }

    users.set(userId, users.get(userId) + 1);
  });

  for (const [userId, numCompletedTasks] of users.entries()) {
    if (numCompletedTasks > 0) {
      console.log(`User ID: ${userId}, Tasks Completed: ${numCompletedTasks}`);
    }
  }
});
