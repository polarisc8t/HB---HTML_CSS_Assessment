from flask import render_template

@app.route('/application')
def application():

    return render_template("application-form.html")
