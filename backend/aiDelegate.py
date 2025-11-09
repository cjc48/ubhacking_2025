import requests


OLLAMA_HOST = "http://127.0.0.1:11434/"  

# Model names
MODEL_INTENT = "phi3:mini"
MODEL_RESPONSETYPE = "mistral:7b"
MODEL_RETRIEVAL_EMBED = "mxbai-embed-large"
MODEL_SUMMERIZATION = "phi3:mini"
MODEL_GENERATION = "llama3:8b"
MODEL_STYLIZER = "mistral:7b"
MODEL_CRITIQUE = "llama3:8b"

MainLLM = "llama3:8b"
MainHelper = "phi3:mini"
MainComposer = "mistral:7b"
MainRetriever = "mxbai-embed-large"


# ===============================

def _ollama_query(model_name: str, prompt: str, host: str = OLLAMA_HOST) -> str:
    """Send a prompt to a locally hosted Ollama model."""
    response = requests.post(
        f"{host}/api/generate",
        json={"model": model_name, "prompt": prompt, "stream": False},
        timeout=300
    )
    return response.json().get("response", "").strip()

# ===============================

def intent_detectionAI(prompt: str) -> str:
    return _ollama_query(MODEL_INTENT, prompt, OLLAMA_HOST)


def response_typeAI(prompt: str) -> str:
    return _ollama_query(MODEL_RESPONSETYPE, prompt, OLLAMA_HOST)


def retrievalAI(prompt: str) -> str:
    return _ollama_query(MODEL_RETRIEVAL_EMBED, prompt, OLLAMA_HOST)


def key_sentence_extractionAI(prompt: str) -> str:
    return _ollama_query(MODEL_SUMMERIZATION, prompt, OLLAMA_HOST)


def generateAI(prompt: str) -> str:
    return _ollama_query(MODEL_GENERATION, prompt, OLLAMA_HOST)


def messageStyleAI(prompt: str) -> str:
    return _ollama_query(MODEL_STYLIZER, prompt, OLLAMA_HOST)


def critiqueAI(prompt: str) -> str:
    return _ollama_query(MODEL_CRITIQUE, prompt, OLLAMA_HOST)


# ===============================

def mainLLM(prompt: str) -> str:
    return _ollama_query(MainLLM, prompt, OLLAMA_HOST)

def mainHelper(prompt: str) -> str:
    return _ollama_query(MainHelper, prompt, OLLAMA_HOST)

def mainComposer(prompt: str) -> str:
    return _ollama_query(MainComposer, prompt, OLLAMA_HOST)

def mainRetriever(prompt: str) -> str:
    return _ollama_query(MainRetriever, prompt, OLLAMA_HOST)
