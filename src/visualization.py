import falcon
import spacy
import json
from spacy import displacy

nlp = spacy.load('de_core_news_sm')

class Dependency_Visualization:
    def on_get(self, req, resp):
        text = "";

        for key, value in req.params.items():
            if key=="text":
                text = str(value)

        if text!="": 
            doc = nlp(text)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_HTML
            resp.text = displacy.render(doc, style="dep")

class EntityRecognition_Visualization:
    def on_get(self, req, resp):
        text = "";

        for key, value in req.params.items():
            if key=="text":
                text = str(value)

        if text != "":
            doc = nlp(text)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_HTML
            resp.text = displacy.render(doc, style="ent")
        else:
            response = {"error":"Error while converting, please check your input"}
            resp.status = falcon.HTTP_200
            resp.text = json.dumps(response)