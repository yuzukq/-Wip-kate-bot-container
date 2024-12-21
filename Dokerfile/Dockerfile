FROM debian
USER root

RUN mkdir /home/bot && \
    apt-get update && \
    apt-get install -y python  \
    sudo && \
    rm -rf /var/lib/apt/lists/ 
    
WORKDIR /home/bot

