import connexion

app = connexion.FlaskApp(__name__, specification_dir='../swagger/')
app.add_api('data.yaml')
app.run(port=8080)