from webassets import Environment, Bundle

assets = Environment('static', 'static')

assets.register('template',
	Bundle('template.html',
		filters='jst',
		output='template.js'
	)
)

# Issue: Doesn't process the templates at all
#assets.debug = True 
# or 
#assets.debug = 'merge'

# Generate
print assets['template'].urls()