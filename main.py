from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---------- STATE ----------
env_state = {
    "text": "",
    "task": "",
    "done": False
}

class ResetRequest(BaseModel):
    task: str
    text: str

class StepRequest(BaseModel):
    action: str

# ---------- RESET ----------
@app.post("/reset")
def reset(data: ResetRequest):
    env_state["text"] = data.text
    env_state["task"] = data.task.lower()
    env_state["done"] = False

    return {
        "state": env_state,
        "message": "Environment reset"
    }

# ---------- STEP ----------
@app.post("/step")
def step(data: StepRequest):
    action = data.action.lower()
    text = env_state["text"]

    result = text
    reward = 0

    if action == "uppercase":
        result = text.upper()
    elif action == "reverse":
        result = text[::-1]
    elif action == "clean":
        result = " ".join(text.split())
    elif action == "word_count":
        result = str(len(text.split()))
    elif action == "summarize":
        result = " ".join(text.split()[:10])

    # FIXED LOGIC
    if action == env_state["task"]:
        reward = 1
        done = True
    else:
        reward = 0
        done = False

    env_state["text"] = result
    env_state["done"] = done

    return {
        "state": env_state,
        "reward": reward,
        "done": done
    }

# ---------- STATE ----------
@app.get("/state")
def get_state():
    return env_state

# ---------- HOME ----------
@app.get("/")
def home():
    return {"message": "OpenEnv Smart API Running"}