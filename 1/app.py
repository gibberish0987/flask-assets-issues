from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

# Init plug-ins
assets = Environment(app)

assets.register('template.js',
	Bundle('template.html',
		filters='jst',
		output='template.js'
	)
)

# Case 1: Doesn't process the templates at all
#assets.debug = True #or #assets.debug = 'merge'

# Case 2: Breaks the template file after first refresh, appends broken templates
#assets.updater = 'always'
#assets.cache = False
# Need to delete .webassets-cache, Bundle output AND restart server to recover

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)