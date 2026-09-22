FROM ubuntu:latest
LABEL authors="vadimsemenov"

ENTRYPOINT ["top", "-b"]