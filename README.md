## Exchange rate application
The goal of the project is to query data from the [Narodowy Bank Polski's public APIs](http://api.nbp.pl/
) and return relevant information.
There are three type of functions:
1. Given a date (formatted YYYY-MM-DD) and a [currency code](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/), provides its average exchange rate.
2. Given a currency code and the number of last quotations N (1 <= N <= 255), provides the max and min average value.
3. Given a currency code and the number of last quotations N (1 <= N <= 255), provides the major difference between the buy and ask rate.

### Installation
Clone the repository with `git clone https://github.com/Riklia/gdn-internship-2023.git`  
Navigate to the project directory.  
Install dependencies with `pip install -r requirements.txt`  

### Usage
To start the server, run `python app.py`. The server will be available at http://localhost:5000.

### Endpoints
* `/exchanges/{code}/{date}`  

Returns the average exchange rate for a given currency code and date.

{code}: a 3-letter currency code (e.g., USD, EUR, AUD)  
{date}: the date for which to retrieve the exchange rate in format YYYY-MM-DD  
<b>Example:</b> `curl http://localhost:5000/exchanges/aud/2023-04-24` should have 2.8024 value in the response.

* `/minmax/{code}/{N}`  
  
Returns the minimum and maximum exchange rates for a given currency code over the last N days.

{code}: A 3-letter currency code (e.g., USD, EUR, AUD)  
{N}: The number of days to retrieve exchange rates for (must be between 1 and 255)  
<b>Example:</b> `curl http://localhost:5000/minmax/USD/10` should return min and max exchange rates for USD over the last 10 days

* `/difference/{code}/{int:N}`  

Returns the maximum difference between the ask and bid prices for a given currency code over the last N days.

{code}: A 3-letter currency code (e.g., USD, EUR, AUD)  
{N}: The number of days to retrieve exchange rates for (must be between 1 and 255)  
<b>Example:</b> `curl http://localhost:5000/difference/EUR/30` which should return max difference between the ask and bid prices for EUR over the last 30 days.

### Testing
To run the test suite, run `python test_app.py`. This will run a series of unit tests to ensure the API endpoints are working correctly.
