# Simple RAG with CODEGEMMA:7B 

This work implements a simple RAG system with `Google\Codegemma:7b` , `Qdrant as VectorDB` and `CoNaLa` dataset
We develop a simple app with `GRADIO` and create `Dcoker` image for conatiner runtime.

## Gradio App UI

<img src="https://github.com/swastikmaiti/RAG_with_local_LLM/blob/8d8b0bd8e413bc3e720de6e82162c5bf20e280e7/gradio-ui.png">
<img src="https://github.com/swastikmaiti/RAG_with_local_LLM/blob/8d8b0bd8e413bc3e720de6e82162c5bf20e280e7/llm-output.png">

# File Structures

- ***rag_localLLM.ipynb:*** This notebook contains code and explanation for implementing RAG with Codegemma.
  - Connecting to Local LLM via Ollama
  - Import Data
  - Import Embedding Model
  - Embed the documents and Create Vector Database
  - Take user query
  - Perform query embedding and Retrieval
  - Perform RAG with Codegemma
- ***vector_database.py:** The code for creating VectorDB
- ***app.py:*** The code for Gradio Application

# Architectures

- **Vector Database:** Qdrant
- **application framework:** Gradio
- **LLM:** Google\Codegemma
- ***LLM server:** Ollama
- **Embedding:** all-MiniLM-L6-v2

# Docker 
The docker image of the app is pushed to docker hub. To run the application we need Linux System with minimun 8GB Memory.
To run the app simply execute the command
```
docker compose up
```

### If you find the repo helpful, please drop a ⭐
