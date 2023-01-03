from flask import Flask, render_template, make_response, jsonify, request
import requests
import json

api_key = "c26fa0071da7b967b63f653f790038444f28b8b5632804011e513113824153ba"
api_html = "http://211.237.50.150:7080/openapi/"+api_key+"/json/Grid_20150827000000000226_1/1/5"

response = requests.get(api_html)
parsed_data = json.loads(response.text)

print(parsed_data)

# 나중에 완성할 것
# 농림수산식품교육문화정보원 공공데이터API
# 입력한 음식/재료명과 관련된 레시피 정보 보여주기