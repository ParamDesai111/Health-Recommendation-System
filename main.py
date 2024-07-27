from flask import Flask, request, jsonify, render_template


app = Flask(__name__)





# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
# return about



# Python main function
if __name__ == '__main__':
    app.run(debug=True)