from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Função para converter números com vírgula para ponto
def converter_numero(numero):
    return numero.replace(',', '.')

# Função para realizar as operações matemáticas
def calcular(num1, num2, operacao):
    try:
        num1 = float(converter_numero(num1))
        num2 = float(converter_numero(num2))
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                return {"resultado": "Erro: Divisão por zero!", "erro": True}
            resultado = num1 / num2
        else:
            return {"resultado": "Operação inválida!", "erro": True}
        
        # Verificar número de casas decimais
        str_resultado = str(resultado)
        partes = str_resultado.split('.')
        
        # Se tem parte decimal e é maior que 10 dígitos
        truncado = False
        if len(partes) > 1 and len(partes[1]) > 10:
            resultado = round(resultado, 10)
            truncado = True
        
        # Formatar o resultado com vírgula
        resultado_formatado = str(resultado).replace('.', ',')
        
        return {
            "resultado": resultado_formatado, 
            "erro": False, 
            "truncado": truncado
        }
    except ValueError:
        return {"resultado": "Erro: Por favor, insira números válidos!", "erro": True}
    except Exception as e:
        return {"resultado": f"Erro: {str(e)}", "erro": True}

# Template HTML com Bootstrap para a interface da calculadora
template = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Web</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            padding-top: 50px;
        }
        .calculator-container {
            max-width: 500px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #f0f0f0;
            border-radius: 5px;
            text-align: center;
        }
        h1 {
            color: #343a40;
            margin-bottom: 30px;
            text-align: center;
        }
        .btn-calculate {
            width: 100%;
            margin-top: 10px;
        }
        .error {
            color: #dc3545;
        }
        .success {
            color: #28a745;
        }
        .warning {
            color: #dc3545;
            font-size: 0.9rem;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="calculator-container">
            <h1>Calculadora Web</h1>
            <form method="POST">
                <div class="mb-3">
                    <label for="numero1" class="form-label">Primeiro Número:</label>
                    <input type="text" class="form-control" id="numero1" name="numero1" value="{{ numero1 }}" required onInput="limitarCasasDecimais(this)">
                </div>
                <div class="mb-3">
                    <label for="operacao" class="form-label">Operação:</label>
                    <select class="form-select" id="operacao" name="operacao" required>
                        <option value="+" {% if operacao == '+' %}selected{% endif %}>Adição (+)</option>
                        <option value="-" {% if operacao == '-' %}selected{% endif %}>Subtração (-)</option>
                        <option value="*" {% if operacao == '*' %}selected{% endif %}>Multiplicação (*)</option>
                        <option value="/" {% if operacao == '/' %}selected{% endif %}>Divisão (/)</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="numero2" class="form-label">Segundo Número:</label>
                    <input type="text" class="form-control" id="numero2" name="numero2" value="{{ numero2 }}" required onInput="limitarCasasDecimais(this)">
                </div>
                <button type="submit" class="btn btn-primary btn-calculate">Calcular</button>
            </form>
            
            {% if resultado != None %}
            <div class="result {% if erro %}error{% else %}success{% endif %}">
                <h4>Resultado:</h4>
                <p class="fs-3">{{ resultado }}</p>
            </div>
            {% endif %}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function limitarCasasDecimais(input) {
            // Substitui a vírgula por ponto para processamento
            let valor = input.value.replace(',', '.');
            let negativo = false;
            
            // Verifica se é um número negativo e remove o sinal para processar
            if (valor.startsWith('-')) {
                negativo = true;
                valor = valor.substring(1);
            }
            
            // Verifica se contém um ponto decimal
            if (valor.includes('.')) {
                let partes = valor.split('.');
                let inteiro = partes[0];
                let decimal = partes[1];
                
                // Se tiver mais de 10 dígitos antes da vírgula, trunca para 10
                if (inteiro.length > 10) {
                    inteiro = inteiro.substring(0, 10);
                }
                
                // Se tiver mais de 10 casas decimais, trunca para 10
                if (decimal.length > 10) {
                    decimal = decimal.substring(0, 10);
                }
                
                // Adiciona o sinal negativo de volta se necessário
                let resultado = (negativo ? '-' : '') + inteiro + ',' + decimal;
                input.value = resultado;
            } else {
                // Caso seja apenas um número inteiro
                if (valor.length > 10) {
                    valor = valor.substring(0, 10);
                }
                
                // Adiciona o sinal negativo de volta se necessário
                input.value = (negativo ? '-' : '') + valor;
            }
        }
        
        // Aplicar limitação inicial quando a página carregar
        window.onload = function() {
            const inputs = document.querySelectorAll('input[type="text"]');
            inputs.forEach(input => limitarCasasDecimais(input));
        }
    </script>
</body>
</html>
'''

# Rota principal (Interface Web)
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    numero1 = ""
    numero2 = ""
    operacao = "+"
    erro = False
    truncado = False
    
    if request.method == 'POST':
        numero1 = request.form.get('numero1', '')
        numero2 = request.form.get('numero2', '')
        operacao = request.form.get('operacao', '+')
        
        res = calcular(numero1, numero2, operacao)
        resultado = res["resultado"]
        erro = res["erro"]
        truncado = res.get("truncado", False)
        
    return render_template_string(
        template, 
        resultado=resultado, 
        numero1=numero1, 
        numero2=numero2, 
        operacao=operacao,
        erro=erro,
        truncado=truncado
    )

# API REST com corpo JSON
@app.route('/api/calcular', methods=['POST'])
def api_calcular():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"erro": "Dados JSON não fornecidos"}), 400
            
        numero1 = data.get('numero1')
        numero2 = data.get('numero2')
        operacao = data.get('operacao')
        
        if None in [numero1, numero2, operacao]:
            return jsonify({"erro": "Parâmetros incompletos"}), 400
            
        res = calcular(numero1, numero2, operacao)
        
        if res["erro"]:
            return jsonify({"erro": res["resultado"]}), 400
        
        resposta = {
            "numero1": numero1,
            "numero2": numero2,
            "operacao": operacao,
            "resultado": res["resultado"]
        }
        
        if res.get("truncado", False):
            resposta["aviso"] = "O resultado foi limitado a 10 casas decimais."
            
        return jsonify(resposta)
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# API REST com parâmetros na URL
@app.route('/api/calcular/<numero1>/<operacao>/<numero2>', methods=['GET'])
def api_calcular_url(numero1, operacao, numero2):
    try:
        res = calcular(numero1, numero2, operacao)
        
        if res["erro"]:
            return jsonify({"erro": res["resultado"]}), 400
        
        resposta = {
            "numero1": numero1,
            "numero2": numero2,
            "operacao": operacao,
            "resultado": res["resultado"]
        }
        
        if res.get("truncado", False):
            resposta["aviso"] = "O resultado foi limitado a 10 casas decimais."
            
        return jsonify(resposta)
        
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
