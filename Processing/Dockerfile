FROM ubuntu:latest

# Install latest updates
RUN apt-get update \
    && apt-get upgrade -y

#Install Python3
RUN apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

# Set encoding to UTF-8
ENV PYTHONIOENCODING=utf-8
ENV LC_ALL=en_CA.UTF-8
ENV LANG=en_CA.UTF-8
ENV LANGUAGE=en_CA.UTF-8

# Set working dir
WORKDIR .

# Copy dataset to working dir
COPY unique_tracks.txt .
COPY triplets_sample_20p.txt .

# Copy your code
COPY diction.py .

# Set starting command (run your code)
CMD python3 diction.py
