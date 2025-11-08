import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_sku_valido(client):
    response = client.post('/', data={'sku': 'RTX-4090'}, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'SKU: RTX-4090 | Quantidade Total em Estoque: 150 unidades.' in response.data

def test_busca_por_serial(client):
    response = client.post('/', data={
        'sku': '', 
        'serial_number': 'SN-C1'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'SKU: CPU-I9 | Quantidade Total em Estoque: 220 unidades.' in response.data

def test_item_invalido(client):
    response = client.post('/', data={
        'sku': 'SKU-FALSO',
        'serial_number': 'SN-FALSO'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Item nao encontrado (SKU ou Numero de Serie invalido).' in response.data