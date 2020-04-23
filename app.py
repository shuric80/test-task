import click
from flask import Flask, jsonify, redirect, render_template, request, url_for

import database
from form import AnimalForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'dfsafas'


@app.route('/details/', methods=['GET'])
def show_details():
    id = request.args.get('id')
    detail = database.get_animal(int(id))
    return render_template('index.html', detail=detail)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/personal/<name>', methods=['GET'])
def get_personal(name):
    ret = database.get_personal(name)
    return jsonify(ret)


@app.route('/animal', methods=['POST', 'GET'])
def add_animal():
    form = AnimalForm()
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        database.add_animal(data)
        return redirect(url_for('add_animal'))

    return render_template('animal.html', form=form)


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    database.create_db()
    database.create_classes()
    click.echo("Initialized the database")


@cli.command()
def drop_db():
    pass


@cli.command()
def runserver():
    app.run()


if __name__ == '__main__':
    cli()
