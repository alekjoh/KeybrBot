from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = "https://www.keybr.com/"
url2 = "https://www.keybr.com/multiplayer"
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
browser = webdriver.Chrome("D:\\Haks\\chromedriver.exe", chrome_options=opts)
browser.set_window_size(1200, 800)
browser.get(url2)

delay = 6 # seconds

load_div_name = "Ticker"

try:
    popup = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, load_div_name)))
except TimeoutException:
    print("Loading took too much time!")


while True:
    ready_text = browser.find_element_by_class_name(load_div_name)
    while ready_text != "GO!":
        ready_text = browser.find_element_by_class_name(load_div_name).text

    text_div = browser.find_element_by_class_name("TextInput-fragment")
    text = text_div.text

    actions = ActionChains(browser)

    prev_char = "f" # Needed to stop bot from trying to type a \n character.
    for c in text:
        print("Char = {}".format(c))
        if prev_char == "↵" and c == "\n":
            continue

        if c == "↵":
            actions.send_keys(Keys.ENTER)  # press enter.
        elif c == "␣":
            actions.send_keys(Keys.SPACE)
        else:
            actions.send_keys(c)
        prev_char = c

    actions.perform()
