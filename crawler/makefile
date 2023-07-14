pip freeze > requirements.txt

docker build -t umodecrawler .


docker run -it --rm --name my-running-app umodecrawler

docker-compose up --build -d


celery -A tasks worker --loglevel=info


python server.py