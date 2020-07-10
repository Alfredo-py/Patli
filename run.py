from Rocho_app import app

#app.config.from_pyfile('config.py')
#app.config.from_object('configuration.ProductionConfig')

app.run(host='0.0.0.0', port=80)#debug=True
#app.config['debug']=True
#app.debug=True