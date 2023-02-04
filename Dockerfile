# syntax=docker/dockerfile:1

FROM python:3.9.2
WORKDIR python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

# Install build tools, libsndfile1, and ffmpeg
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
    libsndfile1 ffmpeg

# Install git
RUN apt-get update && apt-get install -y git

# Install rust development environment
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="$HOME/.cargo/bin:$PATH"

# Install setuptools-rust
RUN pip install setuptools-rust

CMD [ "python3", "server.py"]
