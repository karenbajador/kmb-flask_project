# project/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment, Bundle


################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
assets = Environment(app)


###################
### blueprints ####
###################

from project.user.views import user_blueprint
from project.main.views import main_blueprint
from project.fuzzy.views import fuzzy_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(fuzzy_blueprint, url_prefix="/fuzzy")

print ('app.url_map: {}'.format(app.url_map)) 



###################
### assets     ####
###################

bower = Bundle('js/bower_components/angular/angular.min.js', \
	# 'js/angular-route.min.js', \
	'js/bower_components/ng-file-upload/ng-file-upload-shim.min.js', \
	'js/bower_components/ng-file-upload-shim/ng-file-upload.min.js', \
	'js/bower_components/angucomplete-alt/angucomplete-alt.js', \
    'js/bower_components/angular-bootstrap/ui-bootstrap.js', \
    'js/bower_components/angular-bootstrap/ui-bootstrap-tpls.js', \
            filters='jsmin', output='gen/bower.js')
assets.register('bower_all', bower)

    

tags = Bundle('js/bower_components/ng-tags-input/ng-tags-input.js', \
               filters='jsmin', output='gen/tags.js')
assets.register('tags', tags)

# tags_css = Bundle('js/bower_components/ng-tags-input/ng-tags-input.css', \
#     'js/bower_components/ng-tags-input/ng-tags-input.bootstrap.css', \
#                 filters='jsmin', output='gen/tags.js')
# assets.register('tags_css', tags_css)

 

main_factory = Bundle('js/factory/territories.js', \
	'js/factory/countries.js', \
            filters='jsmin', output='gen/factory.js')
assets.register('factory_all', main_factory)

main_app = Bundle('js/app.module.js', \
            filters='jsmin', output='gen/app.js')
assets.register('app_core', main_app)

fuzzy_app = Bundle('js/fuzzy/fuzzy.controller.js', \
            filters='jsmin', output='gen/fuzzy.js')
assets.register('app_fuzzy', fuzzy_app)



main_css = Bundle('css/main.css', \
	'js/bower_components/angucomplete-alt/angucomplete-alt.css', \
    'js/bower_components/angular-bootstrap/ui-bootstrap-csp.css', \
               filters='jsmin', output='gen/main.css')
assets.register('css_all', main_css)





###################
### flask-login ####
###################

from project.models import User

login_manager.login_view = "user.login"
login_manager.login_message_category = 'danger'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
