import falcon

# import custom routes for different modules
from src.tokenization import Tokenization 
from src.visualization import Visualization
from src.lemmatization import Lemmatization

# init app
app = falcon.App()

# add modules to app
app.add_route('/token/list', Tokenization())
app.add_route('/token/visualization', Visualization())
app.add_route('/lemma', Lemmatization())