FROM python:3

COPY Untitled.py /

WORKDIR /

CMD [ "python3", "./Untitled.py", "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs", "17/May/2015:08:05:32", "01/Jun/2015:15:06:43", "404" ]
