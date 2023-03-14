FROM python

RUN apt-get update && \
    apt-get install -y \
    tzdata \
    curl \
    git

RUN add-apt-repository ppa:openjdk-r/ppa && apt-get update && apt-get install openjdk-8-jdk

RUN useradd -ms /bin/bash docker
RUN mkdir -p /workspaces/minezero && chown -R docker:docker /workspaces/minezero
COPY --chown=docker:docker ./ /workspaces/minezero
USER docker

RUN python -m pip install --upgrade pip
RUN pip install -r /workspaces/minezero/requirements.txt
RUN pip install -e /workspaces/minezero

WORKDIR /workspaces/minezero
