# project/fuzzy/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint


################
#### config ####
################

fuzzy_blueprint = Blueprint('fuzzy', __name__,)


################
#### routes ####
################


@fuzzy_blueprint.route('/fuzzy/')
def fuzzy():
    return render_template('fuzzy/home.html')



