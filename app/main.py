from fastapi import FastAPI

app = FastAPI(
    title="Healthcare Document RAG Assistant",
    description="Portfolio prototype. Not a diagnostic tool.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}