FROM python:3.10-slim

# Install essential tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    vim \
    nano \
    less \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y install --no-install-recommends ca-certificates \
    && update-ca-certificates \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages useful for competitive programming
RUN pip install --no-cache-dir \
    pytest \
    ipython \
    black \
    flake8 \
    mypy

# Set up working directory
WORKDIR /workspace

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1
