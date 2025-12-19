from fastapi import FastAPI, Request, Query

app = FastAPI()

VERIFY_TOKEN = "my_verify_token"

@app.get("/webhook")
def verify(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return "Verification failed"


@app.post("/webhook")
async def receive(request: Request):
    data = await request.json()
    print(data)
    return "ok"
