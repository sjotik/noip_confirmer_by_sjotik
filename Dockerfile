FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
# Replace XXX to NoIP account username
ENV UNAME XXX
# Replace XXX to NoIP account password
ENV PW XXX

CMD python3 noip.py $UNAME $PW