FROM python:3.11-slim

ARG USERNAME=python
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
USER python

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash"]
