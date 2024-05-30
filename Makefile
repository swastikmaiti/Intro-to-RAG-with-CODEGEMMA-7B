install:
		pip install	--upgrade pip &&\
		pip install	-r requirements.txt

ollama-dependency:
		curl https://ollama.ai/install.sh | sh
