# RAG with local LLM

llamafile@https://github.com/Mozilla-Ocho/llamafile.git

llamafile enable execution and distribution of LLM with a single file.
All we need is to download LLM weights in GGUF format and llamfile.exe.
We can run the file across varous OS and platforms.

On execution llamafile start a local server for interacting with LLM via UI.
Developer can choose to interact with Curl API via CLI or with OpenAI API via python.


LLM used @[TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

### Example

```python
user_prompt: "how to sort list in python"

model out_put: {'intent': 'sorting the lists in list of lists `data`', 'snippet': '[sorted(item) for item in data]'}, {'intent': 'sorting the lists in list of lists `data` with custom sorting function `func`', 'snippet': '[sorted(item, key=func) for item in data]'}
```
