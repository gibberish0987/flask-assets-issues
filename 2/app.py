from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

# Init plug-ins
assets = Environment(app)

assets.register('lib.js',
	Bundle('bootstrap.min.js',
		filters='jsmin',
		output='lib.js'
	)
)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)