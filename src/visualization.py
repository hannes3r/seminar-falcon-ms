import falcon
import spacy
from spacy import displacy

nlp = spacy.load('de_core_news_sm')

def visualizeDependencies(s):
    doc = nlp(s)
    svg = displacy.render(doc, style="dep")
    return svg

class Visualization:
    def on_get(self, req, resp):
        text = "";

        for key, value in req.params.items():
            if key=="text":
                text = str(value)

        if text!="": 
            svg_data = visualizeDependencies(text)
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_HTML
            resp.text = svg_data
