# PythonPayAPI
Methods to consume BitcoinToYou's PayDoc API in Python

## Javascript

Metodos para consumir a api bitcointoyou via javascript (web) com angularjs **em desenvolvimento**

Requisitos

* bower `npm i -g bower`
* live-server `npm i -g live-server`

Uso

* `bower install`
* `live-server`


## Python

Na pasta python, existe o módulo `api.py`, onde foi elaborado a classe `TradeApi`

Requisitos

* requests = `pip install requests`

### Metodos da Classe

```python
    # Construtor
    __init__(api_key, api_secret)
    # Gerar Cabeçalho
    generate_header()
    # Receber Invoices
    get(id)
    # Adicionar Invoice
    add(total, redirect_url, notifocation_emal, digital_currency,custom_id)
    # Deletar Invoice
    delete(id)
    # Gerar Assinatura
    def generate_signature(nonce):
    # Gerar Nonce
    def generate_nonce(self):
```

Exemplo de uso

```python
    from algumlugar/api.py import TradeApi

    api = TradeApi(api_key='Sua Key', api_secret='Sua Secret')

    # Listar determinada invoice
    listar = api.get(id=1234)
    # ou listar todas invoices
    listar = api.get()
    # Recebendo dados
    status = listar.status_code # 200 ou 301
    response = listar.content.decode('utf-8') # json

    # Adicionar Inoice
    novo = api.add(total=0.01)
    # Total é obrigatorio, os outros opcionais
    '''
        redirect_url URL de redirect após pagamento da invoice com sucesso [Opcional]
        notifocation_emal Email que irá receber informações da invoice [Opcional]
        digital_currency Moeda digital que será utilizada como pagamento. BTC para Bitcoin e LTC para Litecoin. Como padrão já fica definido BTC [Opcional]
        custom_id Campo disponível para identificação do seu cliente [Opcional]
    '''
    # exempo
    novo = api.add(total=0.01, redirect_url='http://minha/aeee', notifocation_emal='cliente@email.com', digital_currency='BRL', custom_id='3213214')

    # Remover Invoice
    delete = api.delete(id=123)
```
