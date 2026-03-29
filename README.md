---
title: Smart API
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_file: main.py
pinned: false
---
# Smart Task Automation OpenEnv API

## Description

This project is an Open Environment (OpenEnv) API system that simulates a simple text-processing environment.
An agent interacts with the environment using `/reset`, `/step`, and `/state` APIs.

The goal of the agent is to apply the correct operation (action) based on the given task.

---

## Features

* Uppercase conversion
* Reverse text
* Word count
* Clean text
* Extract keywords
* Summarize text

---

## OpenEnv APIs

### 1. Reset Environment

**POST /reset**

Initializes the environment with a task and input text.

#### Example:

```json
{
  "task": "reverse",
  "text": "hello world"
}
```

#### Response:

```json
{
  "state": {
    "text": "hello world",
    "task": "reverse",
    "done": false
  },
  "message": "Environment reset"
}
```

---

### 2. Take Step (Action)

**POST /step**

Applies an action to the current state.

#### Example:

```json
{
  "action": "reverse"
}
```

#### Response:

```json
{
  "state": {
    "text": "dlrow olleh",
    "task": "reverse",
    "done": true
  },
  "reward": 1,
  "done": true
}
```

---

### 3. Get Current State

**GET /state**

Returns current environment state.

---

## Reward Logic

* If `action == task` → reward = 1 and done = true
* If `action != task` → reward = 0 and done = false

---

## How to Run

### Run Without Docker

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

---

### Run With Docker

```bash
docker build -t smart-api .
docker run -p 8000:8000 smart-api
```

---

## API Testing

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Example Workflow

1. Call `/reset`
2. Call `/step` with action
3. Check reward and done
4. Use `/state` to inspect environment

---

## Notes

* Environment resets for each new task
* Designed to simulate agent-environment interaction
* Lightweight and easy to test

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Docker

---

## Conclusion

This project demonstrates a simple OpenEnv-compatible system where agents can interact via APIs to perform tasks and receive rewards based on correctness.
