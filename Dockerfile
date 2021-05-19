FROM ubuntu
COPY . /usr/docker
EXPOSE 5000
WORKDIR /usr/docker
RUN pip install -r requirements.txt
CMD python3 flask_api.py

