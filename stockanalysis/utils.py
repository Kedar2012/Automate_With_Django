from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol, exchange):

    
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        if response.status_code == 200:
            current_price = soup.find('span', {'data-testid': 'qsp-price'}).text
            price_changed = soup.find('span', {'data-testid': 'qsp-price-change'}).text
            percentage_changed = soup.find('span', {'data-testid': 'qsp-price-change-percent'}).text
            previous_close = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'}).text
            week_52_range = soup.find('fin-streamer', {'data-field': 'fiftyTwoWeekRange'}).text
            week_52_high , week_52_low = week_52_range.split(' - ')
            market_cap = soup.find('fin-streamer', {'data-field': 'marketCap'}).text
            pe_ratio = soup.find('fin-streamer', {'data-field': 'trailingPE'}).text

            dividend_yield = get_dividend_yield(soup)

            stock_response = {
                'current_price' : current_price,
                'price_changed' : price_changed,
                'percentage_changed' : percentage_changed,
                'previous_close' : previous_close,
                'week_52_low' : week_52_low,
                'week_52_high' : week_52_high,
                'market_cap' : market_cap,
                'pe_ratio' : pe_ratio,
                'dividend_yield' : dividend_yield
            }

            return stock_response

    except Exception as e:
        print(f'Error Scraping the Data ; {e}')
        return None


def get_dividend_yield(soup):
    labels = soup.find_all('span', class_='label yf-6myrf1')
    values = soup.find_all('span', class_='value yf-6myrf1')

    for label, value in zip(labels, values):
        if 'Forward Dividend & Yield' in label.text:
            return value.text
    return "N/A"


