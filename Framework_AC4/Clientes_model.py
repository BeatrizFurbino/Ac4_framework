from flask import Flask, request, jsonify, make_response
import json

tasks = [
    {
        'id_cliente': 1,
        'nome_cliente': 'Beatriz'
    },
    {
        'id_cliente': 2,
        'nome_cliente': 'Fabricio'
    },
    {
        'id_cliente': 3,
        'nome_cliente': 'Guilherme'
    },
    {
        'id_cliente': 4,
        'nome_cliente': 'Rafael'
    },
    {
        'id_cliente': 5,
        'nome_cliente': 'Theo'
    }
]

listclientes = json.dumps(tasks)

class Clientes_model:
    def clientes():
        return listclientes

