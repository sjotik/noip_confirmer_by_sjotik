FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
# Set NoIP account username to UNAME variable
ENV UNAME=
RUN if [ -z "$UNAME" ]; then echo 'Environment variable UNAME must be specified. Exiting.'; exit 1; fi
# Set NoIP account password to PW variable
ENV PW=
RUN if [ -z "$PW" ]; then echo 'Environment variable PW must be specified. Exiting.'; exit 1; fi

CMD python3 noip.py $UNAME $PW