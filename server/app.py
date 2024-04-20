


from flask import render_template, Flask

app = Flask(__name__)

@app.route('/<id>')
def index(id):
    #update_test(id)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)