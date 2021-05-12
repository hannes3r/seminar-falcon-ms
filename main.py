import falcon

# import custom routes for different modules
from src.tokenization import Tokenization 
from src.lemmatization import Lemmatization
from src.entities import EntityRecognition

from src.visualization import Dependency_Visualization, EntityRecognition_Visualization

# init app
app = falcon.App()

# add modules to app
app.add_route('/token', Tokenization())
app.add_route('/lemma', Lemmatization())
app.add_route('/entities', EntityRecognition())

app.add_route('/visualization/dependencies', Dependency_Visualization())
app.add_route('/visualization/entities', EntityRecognition_Visualization())