FROM ubuntu:20.04

USER root

WORKDIR /app

# General updating
RUN apt-get update -y && apt-get upgrade -y

# Instll required packages
RUN set -ex && cd ~ \
  && apt-get install -y apt-utils 2>&1 \
  && apt-get install -y curl gnupg gnupg1 gnupg2 unzip tar \
  && apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

# Install Terraform
ARG TERRAFORM_VERSION=0.14.10
ARG TERRAFORM_SHA256SUM=45d4a12ca7b5c52983f43837d696f45c5ed9ebe536d6b44104f2edb2e1a39894
RUN set -ex && cd ~ \
  && curl -sSLO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && [ $(sha256sum terraform_${TERRAFORM_VERSION}_linux_amd64.zip | cut -f1 -d ' ') = ${TERRAFORM_SHA256SUM} ] \
  && unzip -o -d /usr/local/bin -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && rm -vf terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Install Python3
ARG PYTHON_VERSION=3.9.5
ARG PYTHON_SHA256SUM=
RUN set -ex && cd ~ \
  && curl -sSLO https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
  && [ $(sha256sum Python-${PYTHON_VERSION}.tgz | cut -f1 -d ' ') = ${PYTHON_SHA256SUM} ] \
  && tar -xf Python-${PYTHON_VERSION}.tgz \
  && cd Python-${PYTHON_VERSION} \
  && ./configure ––enable–optimizations

COPY requirements.txt .
COPY src/ .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "" ]