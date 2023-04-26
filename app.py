import requests
from flask import Flask

app = Flask(__name__)


def handle_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            return None, 'Data not found'
        elif err.response.status_code == 400:
            return None, 'Invalid input or Exceeded the limit'
        else:
            return None, f'Request failed with HTTP error: {err}'


@app.route('/exchanges/<string:code>/<string:date>')
def get_rate_date(code, date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json'
    exchange_rate, error = handle_request(url)
    if error:
        return error
    average = exchange_rate['rates'][0]['mid']
    return f"Code: {code}\nDate: {date}\nAverage: {average}"


@app.route('/minmax/<string:code>/<int:N>')
def get_rate_minmax(code, N):
    if not (0 < N <= 255):
        return "Error: N value must be between 1 and 255 only."
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/last/{N}/?format=json'
    exchange_rate, error = handle_request(url)
    if error:
        return error
    rates = [exchange_rate['rates'][i]['mid'] for i in range(len(exchange_rate['rates']))]
    return f"min rate: {min(rates)}, max rate: {max(rates)}"


@app.route('/difference/<string:code>/<int:N>')
def get_rate_max_difference(code, N):
    url = f'https://api.nbp.pl/api/exchangerates/rates/c/{code}/last/{N}/?format=json'
    exchange_rate, error = handle_request(url)
    if error:
        return error
    differences = [exchange_rate['rates'][i]['ask']-exchange_rate['rates'][i]['bid'] for i in range(len(exchange_rate['rates']))]
    return f"max difference: {max(differences):.4f}"


if __name__ == '__main__':
    app.run()
