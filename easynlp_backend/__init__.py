{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask\
from nlp.remove_punctuation import remove_punctuation_bp\
from nlp.sentiment_analysis import sentiment_analysis_bp\
from nlp.word_cloud import word_cloud_bp\
from nlp.ner import ner_bp\
\
app = Flask(__name__)\
\
app.register_blueprint(remove_punctuation_bp)\
app.register_blueprint(sentiment_analysis_bp)\
app.register_blueprint(word_cloud_bp)\
app.register_blueprint(ner_bp)\
\
if __name__ == '__main__':\
    app.run(debug=True)\
}