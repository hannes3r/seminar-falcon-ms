import spacy
import falcon
import json

nlp = spacy.load('de_core_news_sm')

class EntityRecognition:
    def on_get(self, req, resp):
        text = "";

        for key, value in req.params.items():
            if key=="text":
                text = str(value)

        if text != "":
            doc = nlp(text)
            response = []
            for ent in doc.ents:
                response.append({
                    "text": ent.text,
                    "label": ent.label_,
                    "start_position": ent.start_char,
                    "end_position": ent.end_char
                })
            resp.status = falcon.HTTP_200
            resp.text = json.dumps(response)
        else:
            response = {"error":"Error while converting, please check your input"}
            resp.status = falcon.HTTP_200
            resp.text = json.dumps(response)