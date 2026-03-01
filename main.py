# import os
# import joblib
# import re
# from model.preprocessing import clean_tokenize
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
# nltk.download('punkt_tab')
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")


# decoder = joblib.load(os.getcwd() + "/model/decoder.joblib")
# model = joblib.load(os.getcwd() + "/model/NB_model.joblib")



# @app.get('/predict')
# def infrence(text:str):

#     text = model.predict([text])
#     decodded = decoder.inverse_transform(text)
#     return decodded[0]
