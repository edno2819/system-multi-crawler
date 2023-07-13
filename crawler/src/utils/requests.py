import requests
import logging
from random import choice

class RequestInterface:
    def __init__(self):
        self.user_agents = [""]
        self.current_user_agent = choice(self.user_agents)

        # Configuração do log
        logging.basicConfig(filename='requests.log', level=logging.INFO)

    def send_request(self, url: str):
        headers = {'User-Agent': self.current_user_agent}
        
        try:
            response = requests.get(url, headers=headers)
            # Se o User-Agent for bloqueado, supomos que recebemos um 403
            if response.status_code == 403:
                logging.info(f"User-Agent {self.current_user_agent} foi bloqueado.")
                self.switch_user_agent()
            else:
                logging.info(f"Solicitação bem-sucedida com User-Agent {self.current_user_agent}.")
                return response
        except requests.RequestException as e:
            logging.error(f"Erro ao enviar a solicitação: {str(e)}")

    def switch_user_agent(self):
        new_agent = choice(self.user_agents)
        if new_agent != self.current_user_agent:
            self.current_user_agent = new_agent
            logging.info(f"Alternando para um novo User-Agent: {self.current_user_agent}")
