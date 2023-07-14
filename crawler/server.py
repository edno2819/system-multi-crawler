from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.utils import config
from tasks import runSite
import logging


load_dotenv()
config.setup_logging()
log = logging.getLogger("Server")

app = Flask(__name__)


@app.route('/crawler', methods=['POST'])
def get_sites():
    sites = request.get_json()
    if not sites or not isinstance(sites, list):
        return jsonify({'error': 'O corpo da requisição deve conter uma lista de sites'}), 400

    for site in sites:
        log.debug(f"Processando o site: {site}")
        runSite.delay(site)

    return jsonify({'message': 'Sites processados com sucesso!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)