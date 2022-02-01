from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ekb')
def ekb():
    return render_template('ekb_heat_map.html')


@app.route('/msc')
def msc():
    return render_template('msc_heat_map.html')


@app.route('/spb')
def spb():
    return render_template('spb_heat_map.html')


if __name__ == '__main__':
    app.run()
