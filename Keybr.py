address = 'https://www.keybr.com/login/xxxxxxx'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import uniform
options = webdriver.ChromeOptions()
from time import sleep

url = "https://www.keybr.com/"
url2 = "https://www.keybr.com/multiplayer"
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
options.add_argument('--proxy-server=socks5://localhost:1080')
browser = webdriver.Chrome(chrome_options=options)
browser.set_window_size(1200, 800)
browser.get(address)
browser.get(url2)

delay = 30 # seconds

load_div_name = "Ticker"

try:
    popup = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, load_div_name)))
except TimeoutException:
    print("Loading took too much time!")

previous_kata_text = ''
current_kata_text = ''

while True:
    WebDriverWait(browser, 120, poll_frequency=0.5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, load_div_name),"Start in"))

    text_div = browser.find_element_by_class_name("TextInput-fragment")
    text = text_div.text

    actions = ActionChains(browser)

    prev_char = "f" # Needed to stop bot from trying to type a \n character.
    for c in text:
        print(c, end='')
        if prev_char == "↵" and c == "\n":
            continue

        if c == "↵":
            actions.send_keys(Keys.ENTER)  # press enter.
        elif c == "␣":
            actions.send_keys(Keys.SPACE)
        else:
            actions.send_keys(c)
        prev_char = c
        actions.pause(uniform(0.01,0.2))
    WebDriverWait(browser, 120, poll_frequency=0.3).until(EC.text_to_be_present_in_element((By.CLASS_NAME, load_div_name),"GO!"))
    actions.perform()
