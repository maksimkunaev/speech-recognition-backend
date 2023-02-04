# Speech-recognition-backend

Start docker

`sudo systemctl status docker`

# 1) run docker environment

`docker build -t app-image .`

`docker run -p 5000:5000 app-image`

if http://127.0.0.1:5000/ is not working then run
`docker run --network host -p 5000:5000 app-image`

API endoints:

- POST [http://localhost:5000/transcript](http://localhost:5000/transcript)
  FormData `{ sample: Blob (binary); }` // audio/wav binary blob

# 2) run in development mode

## Set up & Installation.

**macOS/Linux**

```bash
git clone https://github.com/maksimkunaev/nlp-service-docker.git
cd nlp-service-docker
python3 -m venv venv

```

### 2 .Activate the environment

**macOS/Linux**

`. venv/bin/activate`
or
`source venv/bin/activate`

### 3 .Install the requirements

Applies for windows/macOS/Linux

```
pip install -r requirements.txt
```

install ffmpeg for 'whisper': https://github.com/openai/whisper

### 5. Run the application

`python server.py`
