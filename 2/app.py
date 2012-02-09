from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

# Init plug-ins
assets = Environment(app)

assets.register('lib.js',
	Bundle('underscore.js', 'bootstrap.js',
		filters='jsmin',
		output='lib.js'
	)
)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)