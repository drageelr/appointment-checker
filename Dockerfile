FROM selenium/standalone-chrome:114.0.5735.133-chromedriver-114.0.5735.90

USER root

WORKDIR /root
SHELL ["/bin/bash", "-c"]

# Install Pip Dependencies
RUN sudo apt update && \
    sudo apt install -y python3-distutils

# Install Pip
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

# Install Node & PM2
RUN sudo apt install -y nodejs && \
    sudo apt install -y npm && \
    npm install pm2 -g

ENV PIDUSAGE_USE_PS=true

COPY . .

RUN pip install -r requirements.txt
