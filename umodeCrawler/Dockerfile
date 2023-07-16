FROM python:3.10

ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=123456
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

# Instale as dependências do seu projeto Django
RUN pip install django


COPY . /app
WORKDIR /app

# Execute os comandos para migrar o banco de dados e criar o superusuário
RUN python manage.py migrate && \
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
    User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists() or \
    User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" \
    | python manage.py shell


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
