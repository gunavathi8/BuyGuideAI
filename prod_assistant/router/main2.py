import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage

from workflow.agentic_rag_workflow import AgenticRAG

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- FastAPI Endpoints for index.html ----------

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_api(request: Request):
    """
    Accepts JSON POST requests from index.html chat widget.
    Expects: { "user_input": "..." }
    Returns: { "response": "..." }
    """
    data = await request.json()
    user_input = data.get("user_input", "")
    if not user_input:
        return JSONResponse({"response": "Please enter a valid query."})
    rag_agent = AgenticRAG()
    answer = rag_agent.run(user_input)
    print(f"Agentic Response: {answer}")
    return JSONResponse({"response": answer})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)