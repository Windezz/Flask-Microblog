from flask import render_template
from app import app,db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)      # 500 error could be invoked after a database error.
def internal_error(error):  
    db.session.rollback()   # to make sure any failed database sessions do not interfere with any database accesses triggered by the template.
    return render_template('500.html'), 500