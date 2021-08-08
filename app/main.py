import numpy as np
import matplotlib as plt
import pandas as pd
import re

import json
from sklearn.feature_extraction.text import TfidfVectorizer

pd.set_option('display.max_columns', None)

df=pd.read_csv("train.csv",error_bad_lines=False,encoding="ISO-8859-1")
hp=df[df['Sentiment']==1]["SentimentText"]
sd=df[df['Sentiment']==0]["SentimentText"]

happy=[]
sad=[]

for index, line in sd.items():
	line = re.sub(r'http\S+', '', line)
	line = re.sub(r'@\S+', '', line)
	line = re.sub('\W+',' ', line )
	line=line.replace("#","")
	line=line.replace("\n","")
	for i in range(10):
		line=line.replace(str(i),'' )
	sad.append(line.lower())


for index, line in hp.items():
	line = re.sub(r'http\S+', '', line)
	line = re.sub(r'@\S+', '', line)
	line = re.sub('\W+',' ', line )
	line=line.replace("#","")
	line=line.replace("\n","")
	for i in range(10):
		line=line.replace(str(i),'' )
	happy.append(line.lower())


data = happy+sad

from sklearn.model_selection import train_test_split
vec=TfidfVectorizer(stop_words='english')
X=vec.fit_transform(data)
Y=np.append(np.zeros(len(happy)),np.ones(len(sad)))
xtr,xts,ytr,yts=train_test_split(X,Y,test_size=0.33)


from sklearn.linear_model import LogisticRegression
bnb=LogisticRegression()
bnb.fit(xtr,ytr)


from flask import Flask, render_template,send_from_directory

app = Flask(__name__, static_url_path='/static',template_folder="../static")
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/api/<sentence>")
def hello(sentence):
	vect=vec.transform([sentence.lower()]).toarray()
	r=bnb.predict_proba(vect)
	a = {'happiness':r[0][0], 'sadness':r[0][1] }
	return json.dumps(a)
@app.route("/statique/<path:path>")
def static_dir(path):
    return send_from_directory("../static", path)
