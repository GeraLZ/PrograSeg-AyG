FROM tsl0922/ttyd

RUN apt-get -y update \  
    && apt-get install -y openssh-client \
    && apt-get -y clean


EXPOSE 7681

ENV USER_TTYD=""
ENV PASS_TTYD=""

COPY ./run.sh /
RUN chmod 700 /run.sh
RUN useradd -s /bin/bash limitado

CMD /run.sh