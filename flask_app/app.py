from flask import Flask, render_template, make_response, jsonify, request
import fasttext
import re
from fasttext.FastText import _FastText



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    title = request.args.get('title')

    report = model.predict(title) # 모델 예측
    label = re.sub(r"[^가-힣]", "", str(report)) # 분류 카테고리명

    # 가장 가까운 예측 결과 5개 출력
    sim_list = model.get_nearest_neighbors(title, k=5)

    return render_template('report.html',title=title, report=label, sim_list=sim_list)

if __name__ == '__main__':
    # 모델 불러오기
    # model = fasttext.load_model('./small.bin')
    MODEL_PATH = '/Users/badro97/Section3/sprint3/project/Project3/model/model.bin'
    model = _FastText(model_path=MODEL_PATH)
    app.run(host='0.0.0.0', port=8000, debug=True)