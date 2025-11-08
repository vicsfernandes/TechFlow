from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Vic'

ESTOQUE_MOCK = {
    "RTX-4090": {"quantity": 150, "serials": ["SN-A1", "SN-A2", "SN-A3"]},
    "SSD-1TB":  {"quantity": 400, "serials": ["SN-B1", "SN-B2"]},
    "CPU-I9":   {"quantity": 220, "serials": ["SN-C1"]},
    "RAM-32GB": {"quantity": 1000, "serials": ["SN-D1", "SN-D2"]}
}

def buscar_sku_por_serial(serial_num):
    for sku, dados in ESTOQUE_MOCK.items():
        if serial_num in dados["serials"]:
            return sku, dados["quantity"]
    return None, None

@app.route('/', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        sku_form = request.form.get('sku')
        serial_form = request.form.get('serial_number')
        
        sku_encontrado = None
        qtd_encontrada = None

        if serial_form:
             sku_encontrado, qtd_encontrada = buscar_sku_por_serial(serial_form)
        elif sku_form:
            if sku_form in ESTOQUE_MOCK:
                sku_encontrado = sku_form
                qtd_encontrada = ESTOQUE_MOCK[sku_form]["quantity"]

        if sku_encontrado:
            mensagem = f"SKU: {sku_encontrado} | Quantidade Total em Estoque: {qtd_encontrada} unidades."
            flash(mensagem, 'success')
        else:
            mensagem = "Item nao encontrado (SKU ou Numero de Serie invalido)."
            flash(mensagem, 'error')
        
        return redirect(url_for('estoque'))

    return render_template('estoque.html')

if __name__ == '__main__':
    app.run(debug=True)