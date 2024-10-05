from flask import Flask, request, jsonify
from data_loader import LoaderFactory
from replication import Replication


app = Flask(__name__)


@app.route('/seq', methods=['GET'])
def get_dna_seq():
    loader = LoaderFactory.initialize_loader('Files')
    id = request.args.get('id')
    
    try:
        dna_seq_1 = loader.collect(f"./data/{id}_son1.dna")
        dna_seq_2 = loader.collect(f"./data/{id}_son2.dna")

    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    
    return jsonify({'son1': dna_seq_1, 'son2': dna_seq_2})


@app.route('/replicate', methods=['POST'])
def replicate():
    dna_seq = request.json['dna']
    rate = request.json.get('rate', 0.005)
    scale = request.json.get('scale', 20)

    loader = LoaderFactory.initialize_loader('Files')
    id = request.args.get('id')
    dna_seq = loader.collect(f'{id}.dna')
    replication = Replication().execute(dna_seq, rate=rate, scale=scale)
    return jsonify({'text': replication, 'son1': replication[0], 'son2': replication[1]})


if __name__ == '__main__':
    app.run()

