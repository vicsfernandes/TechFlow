from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'vics'

ESTOQUE_MOCK = {
    "RTX-4090": 150,
    "SSD-1TB": 400,
    "CPU-I9": 220,
    "RAM-32GB": 1000
}

@app.route('/', methods=['GET', 'POST'])
def estoque():
    if request.method == 'POST':
        sku_form = request.form.get('sku')

        if sku_form in ESTOQUE_MOCK:
            quantidade = ESTOQUE_MOCK[sku_form]
            mensagem = f"SKU: {sku_form} | Quantidade em Estoque: {quantidade} unidades."
            flash(mensagem, 'success')
        else:
            mensagem = f"SKU {sku_form} nao encontrado no inventario."
            flash(mensagem, 'error')
        
        return redirect(url_for('estoque'))

    return render_template('estoque.html')

if __name__ == '__main__':
    app.run(debug=True)