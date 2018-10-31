FROM ubuntu:latest

# Install latest updates
RUN apt-get update \
    && apt-get upgrade -y

#Install Python3
RUN apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

# Install your software
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install sqlite3

# Set working dir
WORKDIR .

# Copy dataset to working dir
COPY unique_tracks.txt .
COPY triplets_sample_20p.txt .

# Copy your code
COPY reader.py .

# Set starting command (run your code)
CMD python3 reader.py
