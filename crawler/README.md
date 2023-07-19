# Sistema de Crawler

* SQLAlqmy
* logs
* celery
* libcloud
* Flask

## Estrutura de Pastas
Dentro da pasta onde for configurado para salvar os arquivos

### Iniciar sistema direto
Para iniciar o crawler diretamente.

```bash
    python main.py
```
Ele ira rodar os crawlers um de cada vez conforme os sites dentro do arquivo de configuração .yaml

### Para adicionar um novo site de crawler
- Crie uma pasta dentro de "src/brands/nome-do-site"
- Crie os arquivos:
    * `__init__.py`
    * main.py
    * config.yaml
        - Configurações individuais para cada site
    * info.md
        - Opcional: Anotações sobre a estratégia para crawlear cada site

Dentro do arquivo `main.py` deve haver uma classe nesse estilo

```python
class NomeDoSite(RequestController):

    def __init__(self, database: DatabaseManager, config: dict, site_id: str):
        super().__init__(database, config, site_id)

    def run(self): pass
```
Deve herdar da classe `RequestController`, no qual implementa a base para algumas funcionalidades comuns do crawler usando request. E deve implementar o método `run`, no qual vai executar a lógica do crawler.

### Carregamento do módulo de cada Site
Cada execução da função `task` dentro do arquivo `task.py`, carrega os módulos de crawler para cada site dinamicamente através da função `load_class_brand`; por isso, é importante seguir o padrão de criação de novas extrações.
