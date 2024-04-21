import threading

from flask import render_template, Flask
import MainFlowLib as mfl

__flaskDummyApp = Flask(__name__)
__flaskDummyAppTestDict : dict[str, mfl.LinkTestCase] = dict()

@__flaskDummyApp.route('/<id>')
def index(id):
    case = __flaskDummyAppTestDict.get(id)
    if case is not None:
        case.isClicked = True

    return render_template('index.html')

def RunFlask() -> threading.Thread:
    __flaskDummyApp.debug = False
    thread = threading.Thread(target=__flaskDummyApp.run)
    thread.start()
    return thread