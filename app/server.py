from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatHuggingFace
from langserve import add_routes

app = FastAPI(
    title="Jose-app",
    version="1.0",
    description="An AI chatbot api"
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(
    app,
    ChatHuggingFace(),
    path="/huggingface"
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
