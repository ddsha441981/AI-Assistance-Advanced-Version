__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import requests
from bs4 import BeautifulSoup
import pandas as pd

from utils.utils import Utils


class CheckingPrices:
    def __init__(self, logger, response, prices_online, command):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.prices_online = prices_online

        # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    # Checking Petrol Prices
    def checking_petrol_prices(self):
        try:
            # link for extract html data
            def getdata(url):
                r = requests.get(url)
                return r.text

            htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
            soup = BeautifulSoup(htmldata, 'html.parser')

            # Declare string var
            # Declare list
            mydatastr = ''
            result = []

            # searching all tr in the html data
            # storing as a string
            for table in soup.find_all('tr'):
                mydatastr += table.get_text()

            # set accourding to your required
            mydatastr = mydatastr[1:]
            itemlist = mydatastr.split("\n\n")

            for item in itemlist[:-5]:
                result.append(item.split("\n"))

            # Calling DataFrame constructor on list
            df = pd.DataFrame(result[:-8])
            print(df)


        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking Petrol Prices
    def checking_diesel_prices(self):
        try:
            # link for extract html data
            def getdata(url):
                r = requests.get(url)
                return r.text

            htmldata = getdata("https://www.goodreturns.in/diesel-price.html")
            soup = BeautifulSoup(htmldata, 'html.parser')

            # Declare string var
            # Declare list
            mydatastr = ''
            result = []

            # searching all tr in the html data
            # storing as a string
            for table in soup.find_all('tr'):
                mydatastr += table.get_text()

            # set accourding to your required
            mydatastr = mydatastr[1:]
            itemlist = mydatastr.split("\n\n")

            for item in itemlist[:-5]:
                result.append(item.split("\n"))

            # Calling DataFrame constructor on list
            df = pd.DataFrame(result[:-8])
            print(df)


        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking CNG Gas Prices
    def checking_cng_prices(self):
        try:
            # link for extract html data
            def getdata(url):
                r = requests.get(url)
                return r.text

            htmldata = getdata("https://www.goodreturns.in/cng-price.html")
            soup = BeautifulSoup(htmldata, 'html.parser')

            # Declare string var
            # Declare list
            mydatastr = ''
            result = []

            # searching all tr in the html data
            # storing as a string
            for table in soup.find_all('tr'):
                mydatastr += table.get_text()

            # set accourding to your required
            mydatastr = mydatastr[1:]
            itemlist = mydatastr.split("\n\n")

            for item in itemlist[:-5]:
                result.append(item.split("\n"))

            # Calling DataFrame constructor on list
            df = pd.DataFrame(result[:-8])
            print(df)



        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking LPG Gas Prices
    def checking_lpg_prices(self):
        try:
            # link for extract html data
            def getdata(url):
                r = requests.get(url)
                return r.text

            htmldata = getdata("https://www.goodreturns.in/lpg-price.html")
            soup = BeautifulSoup(htmldata, 'html.parser')

            # Declare string var
            # Declare list
            mydatastr = ''
            result = []

            # searching all tr in the html data
            # storing as a string
            for table in soup.find_all('tr'):
                mydatastr += table.get_text()

            # set accourding to your required
            mydatastr = mydatastr[1:]
            itemlist = mydatastr.split("\n\n")

            for item in itemlist[:-5]:
                result.append(item.split("\n"))

            # Calling DataFrame constructor on list
            df = pd.DataFrame(result[:-8])
            print(df)


        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking Stock Market
    def checking_stocks_market(self):
        try:
            url = 'https://money.rediff.com/companies/market-capitalisation'
            df = pd.read_html(url)[0]
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            print(df)

        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking Gold Prices
    def checking_gold_prices(self):
        try:
            # The webpage URL whose table we want to extract
            url = "https://www.goodreturns.in/gold-rates/#Weekly+%26+Monthly+Graph+of+Gold+Price+in+India"

            # Assign the table data to a Pandas dataframe
            table = pd.read_html(url)[0]  # use number which table you want [0],[1] etc
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)

            # Print the dataframe
            print(table)


        except ConnectionError as er:
            self.logger.error(er)

        except Exception as err:
            self.logger.error(err)

    # Checking Sliver Prices
    def checking_sliver_prices(self):
        try:
            # The webpage URL whose table we want to extract
            url = "https://www.goodreturns.in/silver-rates/#Indian+Major+Cities+Silver+Rates+Today"

            # Assign the table data to a Pandas dataframe
            table = pd.read_html(url)[0]  # use number which table you want [0],[1] etc
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)

            # Print the dataframe
            print(table)

        except ConnectionError as er:
            self.logger.error(er)
        except Exception as err:
            self.logger.error(err)

    # Checking cryptocurrency Prices
    def checking_bitcoin_prices(self):
        try:
            # url = 'https://cryptocurrencyprices.stockmaster.in/cryptocurrency-prices-in-inr-india/'
            # url = 'https://coinmarketcap.com/coins/views/all/'
            url = 'https://coinranking.com/'
            df = pd.read_html(url)[0]
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            print(df)

        except ConnectionError as er:
            self.logger.error(er)
        except Exception as err:
            self.logger.error(err)

    # get key from voice input
    def get_path_prices(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is ', key + " command is " + self.command)

                for web_price_online in self.prices_online:
                    print("in for sysactivity is ", web_price_online, "path is : ", web_price_online)
                    if key in web_price_online:
                        return self.prices_online[web_price_online]

        except IndexError as e:
            self.logger.error(e)
        except Exception:
            pass

    def checking_online_prices(self):
        path = self.get_path_prices()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'bitcoin':
                self.response_speak(self.response)
                self.checking_bitcoin_prices()

            elif path in 'petrol':
                self.response_speak(self.response)
                self.checking_petrol_prices()

            elif path in 'diesel':
                self.response_speak(self.response)
                self.checking_diesel_prices()

            elif path in 'cng':
                self.response_speak(self.response)
                self.checking_cng_prices()

            elif path in 'lpg':
                self.response_speak(self.response)
                self.checking_lpg_prices()

            elif path in 'sliver':
                self.response_speak(self.response)
                self.checking_sliver_prices()

            elif path in 'gold':
                self.response_speak(self.response)
                self.checking_gold_prices()

            elif path in 'stock':
                self.response_speak(self.response)
                self.checking_stocks_market()
        print(str(path))
