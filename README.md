# Sistema de Crawler

- Processos distribuído com Celery
- Sistema de filas com Redis
- Web crawler com requests
- Sistema de administração com Django
- Banco de dados com Mysql
- Logs

## Iniciar o sistema

### Criar a pasta onde o volume docker será relacionado.
Nesta pasta compartilhará os arquivo baixados pelo crawler

```bash
    mkdir /home/${USER}/crawler
```

### Inicie o docker-compose
```bash
    docker-compose up --build -d
```
### Crie um usuário admin no Django
Para criar o usuário admin você precisará entrar dentro do container do servidor Django.

```bash
    docker ps
    docker exec -i -t id_imagem_django_web /bin/bash
    python manage.py createsuperuser
```

### Acesse o sistema Admin
http://localhost:8000

### Crie na tabela  Sites
Após logar no sistema admin, vá para a barra lateral e escolha a tab Sites. Crie um novo item com o nome de Arezzo. Este item é referente a pasta que contem a lógica de extração do site Arezzo na pasta crawler.

### Executar crawlers
Após ter um site registrado e com uma lógica de extração disponível, é possível executar o crawler através
<p align="center">
<img width="360" style="border-radius: 5px" height="250" src="./images/runCrawler.png" alt="Intro">
</p>


### Acompanhar filas de workers
No admin você pode clicar em "Ir para o Flowers" para abrir a página de acompanhamento do sistema distribuído de crawler, no qual mostrar os works, fila de tarefas, e histórico de execução.
<p align="center">
<img style="border-radius: 5px"  src="./images/flowers.png" alt="Intro">
</p>