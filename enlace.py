from os import link

import requests
import pandas 
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
from datetime import date
import json
url='https://laboratorio5-c5ee8-default-rtdb.firebaseio.com/documentos.json'

payload={'password':'valorant','IP':'x1.x1.x1.x1','OS':'MACOS','version':'4.6'}
#response = requests.post(url, json = payload)

response2=requests.get(url)
print(response2.text)