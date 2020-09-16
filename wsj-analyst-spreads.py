from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#open ticker file
f = open("stock-names.txt", "r")
ratings_dict_all = {}
extremes = {}
for ticker in f:
    whitelist = set('$0123456789. ')

    need = str(ticker.strip())
    url = "https://www.wsj.com/market-data/quotes/" + need + "/research-ratings"
    # tries to find url...if it can't, exception: add to no urls list
    try:
        driver.get(url)
            # tries to find chart...if it can't, exception: add to no charts list
            # data-module-zone="rr_stockprice"

        try:
            ratings = driver.find_element_by_xpath("//*[contains(@data-module-zone, 'rr_stockprice')]")
            current_text = ratings.text.strip("\n")
            numbers_string = ''.join(filter(whitelist.__contains__, current_text))
            split = numbers_string.split("$")
            new_list = []

            for item in split:
                if(len(item.strip(" "))==0):
                    new_list.append("N/A")
                else:
                    new_list.append(float(item))
            ratings_dict_all[need] = {}
            ratings_dict_all[need]["high"] = new_list[1]
            ratings_dict_all[need]["median"] = new_list[2]
            ratings_dict_all[need]["low"] = new_list[3]
            ratings_dict_all[need]["average"] = new_list[4]
            ratings_dict_all[need]["current price"] = new_list[5]
            if(new_list[4] >= new_list[5]*3):
                extremes[need] = {}
                extremes[need]["average"] = new_list[4]
                extremes[need]["current price"] = new_list[5]

        except:
            print("\nNo analyst ratings for " + need + ".\n")
            ratings_dict_all[need] = {}
            ratings_dict_all[need]["error"] = "No analyst ratings recorded."

    except:
        print("\nNo url for " + need + ".\n")
        ratings_dict_all[need] = {}
        ratings_dict_all[need]["error"] = "No url recorded."
g = open("ratings_dict_all.pkl", "wb")
pickle.dump(ratings_dict_all, g)
g.close()
g = open("extremes.pkl", "wb")
pickle.dump(extremes, g)
g.close()
