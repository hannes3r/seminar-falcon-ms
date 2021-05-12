import falcon

#import custom routes for different modules
from src.tokenization import Tokenization 
from src.visualization import Visualization

#init app
app = falcon.App()

#add modules to app
app.add_route('/token/list', Tokenization())
app.add_route('/token/visualization', Visualization())