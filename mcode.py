if __name__ == "__main__":
    print("Googling.....")
    url = "https://www.google.com/search?q=" + " ".join(sys.argv[1:])
    res = requests.get(url, headers={"UserAgent": UserAgent().random})
    # res.raise_for_status()
    with open("project1a.html", "wb") as out_file:  # only for knowing the class
        for data in res.iter_content(10000):
            out_file.write(data)
    soup = BeautifulSoup(res.text, "html.parser")
    links = list(soup.select(".eZt8xd"))[:5]

def stock_price(symbol: str = "AAPL") -> str:
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    yahoo_finance_source = requests.get(url, headers={"USER-AGENT": "Mozilla/5.0"}).text
    soup = BeautifulSoup(yahoo_finance_source, "html.parser")
    specific_fin_streamer_tag = soup.find("fin-streamer", {"data-test": "qsp-price"})
