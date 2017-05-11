import hmac
import hashlib
import uuid
import base64
'''pip install requests'''
import requests

class TradeApi():

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def generate_header(self):
        """Gerar Cabeçalho de Autenticação"""
        nonce = self.generate_nonce()
        return {
            'Key': self.api_key,
            'Signature': self.generate_signature(nonce),
            'Nonce': nonce,
        }

    def get(self, id=None):
        """Get invoices"""
        url = 'https://www.bitcointoyou.com/Payments/getInvoices.aspx'
        headers = self.generate_header()
        data = {
            'Id': id
        }
        data = None if id is None else data
        return requests.post(url,headers=headers, data=data)

    def delete(self, id):
        """
            Autenticação
                Sim
            Parâmetros:
                id Identificação (id) da fatura que deseja cancelar;
            Campos de retorno:
                Status Status da incoice sendo: NEW, PAID, UNDERPAID, OVERPAID,COMPLETED, CANCELED, EXPIRED;
                Currency BRL (sempre)
                CurrencyTotal Valor total da fatura.
                DigitalCurrency : Moeda digital da invoice (Bitcoin ou Litecoin);
                DigitalCurrencyQuotation Cotação da moeda digital para conversão no momento da criação da invoice;
                DigitalCurrencyAddress Endereço para pagamento da invoice;
                DigitalCurrencyAmount Quantidade de moedas necessárias para pagamento da invoice;
                DigitalCurrencyAmountPaid Quantidade de moedas efetivamente pagas para invoce;
                ConfirmationTransferDate Data e Hora da confirmação da transferência;
                ConfirmationTransferTimestamp Timestamp da confirmação da transferência;
                ExpirationDate Data e Hora da expiração da invoice;
                ExpirationTimestamp : Timestamp da expiração da invoice;
                TransferToAccountEstimateDate Data e Hora estimada para transferência da invoice para conta bancaria;
                TransferToAccountEstimateTimestamp Timestamp estimado para transferência da invoice para conta bancaria;
                TransferToAccountDate Data e Hora da realização da transferência bancaria;
                TransferToAccountTimestamp Timestamp da realização da transferência bancaria;
                DateCreated Data e Hora da criação da invoice;
                DateCreatedTimestamp Timestamp da criação da invoice;
                CustomId Campo disponível para controle do cliente;
                RedirectUrl URL de redirect após pagamento da invoice com sucesso;
                RedirectUrlReturn Retorno armazenado contendo o resultado retornado da RedirectUrl;
                NotificationEmail Email que irá receber informações da invoice;
        """
        url = 'https://www.bitcointoyou.com/Payments/deleteInvoices.aspx'
        headers = self.generate_header()
        data = {
            'Id': id
        }

        return requests.post(url,headers=headers, data=data)

    def add(self, total, redirect_url=None, notifocation_emal=None, digital_currency=None, custom_id=None):
        """ 
            Autenticação
                Sim
            Parâmentros:
                Total Valor total da venda
                RedirectUrl URL de redirect após pagamento da invoice com sucesso [Opcional]
                NotificationEmail Email que irá receber informações da invoice [Opcional]
                DigitalCurrency Moeda digital que será utilizada como pagamento. BTC para Bitcoin e LTC para Litecoin. Como padrão já fica definido BTC [Opcional]
                CustomId Campo disponível para identificação do seu cliente [Opcional]
            Campos de retorno:
                Status Status da incoice sendo: NEW, PAID, UNDERPAID, OVERPAID,COMPLETED, CANCELED, EXPIRED;
                Currency BRL (sempre)
                CurrencyTotal Valor total da fatura.
                DigitalCurrency : Moeda digital da invoice (Bitcoin ou Litecoin);
                DigitalCurrencyQuotation Cotação da moeda digital para conversão no momento da criação da invoice;
                DigitalCurrencyAddress Endereço para pagamento da invoice;
                DigitalCurrencyAmount Quantidade de moedas necessárias para pagamento da invoice;
                DigitalCurrencyAmountPaid Quantidade de moedas efetivamente pagas para invoce;
                ConfirmationTransferDate Data e Hora da confirmação da transferência;
                ConfirmationTransferTimestamp Timestamp da confirmação da transferência;
                ExpirationDate Data e Hora da expiração da invoice;
                ExpirationTimestamp : Timestamp da expiração da invoice;
                TransferToAccountEstimateDate Data e Hora estimada para transferência da invoice para conta bancaria;
                TransferToAccountEstimateTimestamp Timestamp estimado para transferência da invoice para conta bancaria;
                TransferToAccountDate Data e Hora da realização da transferência bancaria;
                TransferToAccountTimestamp Timestamp da realização da transferência bancaria;
                DateCreated Data e Hora da criação da invoice;
                DateCreatedTimestamp Timestamp da criação da invoice;
                CustomId Campo disponível para controle do cliente;
                RedirectUrl URL de redirect após pagamento da invoice com sucesso;
                RedirectUrlReturn Retorno armazenado contendo o resultado retornado da RedirectUrl;
                NotificationEmail Email que irá receber informações da invoice;
        """
        url = 'https://www.bitcointoyou.com/Payments/invoices.aspx'
        headers = self.generate_header()
        data = {
            'Total': total,
            'RedirectUrl': redirect_url,
            'NotificationEmail': notifocation_emal,
            'DigitalCurrency': digital_currency,
            'CustomId': custom_id,
        }

        return requests.post(url, headers=headers, data=data)

    def generate_signature(self, nonce):
        """Generate Signature"""
        msg = '{}{}'.format(nonce,self.api_key)
        digest = hmac.new(str.encode(self.api_secret), msg=msg.encode('utf-8'), digestmod=hashlib.sha256).digest()
        return base64.b64encode(digest).decode()

    def generate_nonce(self):
        """Generate pseudo-random number and seconds since epoch (UTC)."""
        nonce = uuid.uuid1()
        return str(nonce.time)
