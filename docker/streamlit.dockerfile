FROM python:3.12-slim

WORKDIR /streamlit
COPY .env /streamlit/
COPY uv.lock /streamlit/
COPY packages/dev_ui/README.md ./
COPY packages/dev_ui /streamlit/
# COPY packages/dev_ui/pyproject.toml ./

# RUN apt-get update && apt-get install -y curl bash && \
#     curl -LsSf https://astral.sh/uv/install.sh | sh

# ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl=7.88.* && \
    curl --proto '=https' --tlsv1.2 -LsSf https://github.com/astral-sh/uv/releases/download/0.5.26/uv-installer.sh | sh && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"


RUN uv sync --all-packages

CMD [".venv/bin/streamlit", "run", "src/dev_ui/ui/Homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]
