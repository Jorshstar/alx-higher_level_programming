#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);

  const todos = JSON.parse(body);
  const completedTasks = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
