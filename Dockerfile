FROM python:3.7.2-stretch

#berjalan terus
#RUN rm -rf /var/cache/apk/* && \rm -rf /tmp/*

#RUN echo -e "https://nl.alpinelinux.org/alpine/v3.5/main\nhttps://nl.alpinelinux.org/alpine/v3.5/community" > /etc/apk/repositories

RUN apt update

#RUN apt add --update socat bash && \rm -rf /var/cache/apk/*
RUN apt install socat -y

RUN useradd -m syntek

ADD validator.py /home/syntek/validator.py

RUN chmod 500 /home/syntek/validator.py

RUN chown -R syntek:root /home/syntek

#ganti dr root ke syntek
USER syntek

WORKDIR /home/syntek

CMD socat TCP-L:9090,fork EXEC:"/usr/bin/python3 validator.py",reuseaddr,stderr
