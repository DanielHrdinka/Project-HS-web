import requests

class CurrencyAPIClient:
    def __init__(self, base_currency) -> None:
        self.base_currency = base_currency
        self.__url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    def get_rate(self, currency: str) -> float:
        response = requests.get(self.__url)
        response.raise_for_status()
        data = response.json()
        return data["rates"][currency]

    def convert_to_czk(self, amount: float) -> str:
        rate = self.get_rate("CZK")
        converted = amount * rate
        return f"{amount} {self.base_currency} = {converted:.2f} CZK"

eur_client = CurrencyAPIClient(base_currency="EUR")
eur_to_czk = eur_client.get_rate("CZK")

usd_client = CurrencyAPIClient(base_currency="USD")
usd_to_czk = usd_client.get_rate("CZK")

print("1 EUR =", eur_to_czk, "CZK")
print("1 USD =", usd_to_czk, "CZK")
print(eur_client.convert_to_czk(10))
print(usd_client.convert_to_czk(10))