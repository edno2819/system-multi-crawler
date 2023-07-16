from flask import Flask, request, jsonify
from dotenv import load_dotenv
from tasks import runSite

load_dotenv()

app = Flask(__name__)


@app.route('/crawler', methods=['POST'])
def get_sites():
    data = request.get_json()
    sites = data["sites"]
    if not sites or not isinstance(sites, list):
        return jsonify({'error': 'O corpo da requisição deve conter uma lista de sites'}), 400

    for site in sites:
        runSite.delay(site)

    return jsonify({'message': 'Sites processados com sucesso!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)