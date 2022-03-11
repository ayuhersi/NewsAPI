from flask import render_template
from . import main 

@main.app_errorhandler(404)
def not_found(error):
    """
    fuction to rendr our 404 page

    """
    
    return render_template("notfound.html")