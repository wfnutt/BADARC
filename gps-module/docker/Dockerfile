FROM alpine:latest AS workshop

ENV WORKSHOP_USER=badarc
RUN apk update \
  && apk upgrade \
  && apk add python3 picocom nano joe vim \
  && adduser -g "BADARC Workshop User" ${WORKSHOP_USER} -D \
  && addgroup  ${WORKSHOP_USER} dialout

USER ${WORKSHOP_USER}
ENV PROJECT=gps-module
RUN mkdir -p /home/${WORKSHOP_USER}/${PROJECT}
RUN echo ". bin/activate" >> /home/${WORKSHOP_USER}/.profile
WORKDIR /home/${WORKSHOP_USER}/${PROJECT}

RUN python3 -m venv . \
  && source ./bin/activate \
  && pip3 install --upgrade pip \
  && pip3 install --upgrade pyubx2 pyserial \
  && pip3 install --upgrade pygnssutils

CMD /bin/sh -li
