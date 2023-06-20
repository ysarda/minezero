FROM pytorch/pytorch

RUN apt-get update && \
    apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    tmux \
    htop \
    gcc \
    xvfb \
    python-opengl \
    x11-xserver-utils \
    openjdk-8-jdk

RUN useradd -ms /bin/bash docker
RUN mkdir -p /workspaces/minezero && chown -R docker:docker /workspaces/minezero
COPY --chown=docker:docker ./ /workspaces/minezero
USER docker

RUN python -m pip install --upgrade pip
RUN pip install --upgrade --user minerl
RUN pip install -r /workspaces/minezero/requirements.txt
RUN pip install -e /workspaces/minezero

WORKDIR /workspaces/minezero
CMD ["bash","/bin/bash"]