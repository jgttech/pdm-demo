FROM ubuntu:latest

RUN mkdir /svc
WORKDIR /svc

COPY dist/das .

CMD ./das