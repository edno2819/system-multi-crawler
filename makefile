.PHONY: requirements docker-build docker-run docker-compose-up celery-start server-start docker-exec

requirements:
    pip freeze > requirements.txt

docker-build:
    docker build -t umodecrawler .

docker-run:
    docker run -it --rm --name my-running-app umodecrawler

docker-compose-up:
    docker-compose up --build -d

celery-start:
    celery -A tasks worker --loglevel=info

server-start:
    python server.py

docker-exec:
    docker exec -i -t container_id /bin/bash
