import json
import falcon
import spacy
import src.spacy_load

nlp = src.spacy_load.get_nlp_object()

class Tokenization:
    def on_get(self, req, resp):

        text = "";

        for key, value in req.params.items():
            if key=="text":
                text = str(value)

        if text != "":
            doc = nlp(text)
            response = []
            for token in doc:
                response.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "position": token.pos_,
                    "dependencies": token.dep_
                })
            resp.status = falcon.HTTP_200
            resp.text = json.dumps(response)
        else:
            response = {"error":"Error while converting, please check your input"}
            resp.status = falcon.HTTP_400
            resp.text = json.dumps(response)

        

       