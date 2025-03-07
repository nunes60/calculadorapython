# Calculadora Web com Python e Flask

Uma calculadora web completa com interface gráfica e API REST, desenvolvida em Python utilizando Flask e Bootstrap.

## Sobre o Projeto

Este sistema implementa uma calculadora web com interface gráfica amigável e APIs REST para integração com outros sistemas. O projeto foi desenvolvido em Python com Flask, utilizando Bootstrap para a interface, e oferece suporte a operações matemáticas básicas com formatação adequada para números no formato brasileiro (vírgula como separador decimal).

## Recursos

- **Interface Web Responsiva**
  - Design moderno com Bootstrap
  - Compatível com dispositivos móveis e desktop
  - Feedback visual para erros e resultados

- **Operações Matemáticas**
  - Adição
  - Subtração
  - Multiplicação
  - Divisão (com proteção contra divisão por zero)

- **Tratamento de Dados**
  - Suporte a números com vírgula (formato brasileiro)
  - Conversão automática entre vírgula e ponto
  - Limitação inteligente de casas decimais
  - Validação de entradas

- **API REST Completa**
  - Endpoint para cálculos via JSON
  - Endpoint para cálculos via parâmetros de URL
  - Respostas formatadas em JSON
  - Tratamento de erros adequado

- **Segurança e Robustez**
  - Validação de entradas
  - Tratamento de exceções
  - Feedback amigável em caso de erros

## Começando

### Pré-requisitos

- Python 3.6 ou superior
- Flask

### Instalação

1. Clone o repositório ou baixe os arquivos para seu computador
   ```
   git clone https://github.com/nunes60/calculadorapython.git
   ```

2. Navegue até o diretório do projeto
   ```
   cd calculadorapython
   ```

3. Instale as dependências
   ```
   pip install flask
   ```

4. Execute a aplicação
   ```
   python calculadora_web.py
   ```

5. Acesse a calculadora no navegador
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

```
Calculadora em Python/
├── calculadora_web.py       # Código principal da aplicação
└── README.md                # Este arquivo
```

## Bibliotecas Utilizadas

Este projeto utiliza algumas bibliotecas Python:

- `Flask`: Framework web leve e flexível para Python
- `urllib.parse`: Para decodificar caracteres especiais na URL da API
- Bibliotecas padrão do Python

Para o frontend:
- `Bootstrap 5.3.0`: Framework CSS para interface responsiva
- JavaScript para manipulação do DOM e validação de entradas

## Como Usar

### Interface Web

1. Acesse a calculadora no navegador através do endereço `http://localhost:5000`
2. Insira o primeiro número (aceita vírgula como separador decimal)
3. Selecione a operação desejada (adição, subtração, multiplicação ou divisão)
4. Insira o segundo número
5. Clique em "Calcular" para ver o resultado

### API REST com JSON

Para realizar cálculos programaticamente, envie uma requisição POST para `/api/calcular`:

```
POST /api/calcular
Content-Type: application/json

{
    "numero1": "10,5",
    "operacao": "+",
    "numero2": "5,3"
}
```

Exemplo de resposta:

```json
{
    "numero1": "10,5",
    "numero2": "5,3",
    "operacao": "+",
    "resultado": "15,8"
}
```

### API REST com parâmetros na URL

Também é possível realizar cálculos via GET utilizando parâmetros na URL:

```
GET /api/calcular/10,5/+/5,3
```

Exemplo de resposta:

```json
{
    "numero1": "10,5",
    "numero2": "5,3",
    "operacao": "+",
    "resultado": "15,8"
}
```

## Detalhes de Implementação

### Formatação de Números

- A calculadora aceita números no formato brasileiro (com vírgula como separador decimal)
- Internamente, os números são convertidos para o formato com ponto, para processamento correto
- Os resultados são exibidos com vírgula como separador decimal
- Há limitação de 10 dígitos antes e 10 dígitos após a vírgula

### Tratamento de Erros

O sistema trata os seguintes erros:
- Divisão por zero
- Entrada de valores não numéricos
- Operações inválidas

### Limitação de Casas Decimais

Para evitar resultados com muitas casas decimais, o sistema:
- Limita automaticamente a exibição a 10 casas decimais
- Utiliza JavaScript para limitar a entrada do usuário
- Exibe aviso quando o resultado é truncado

## Customização

A interface utiliza Bootstrap, o que facilita a personalização. Você pode modificar a aparência editando a seção CSS no template HTML dentro do arquivo `calculadora_web.py`.
