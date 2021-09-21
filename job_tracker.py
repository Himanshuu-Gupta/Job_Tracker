from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

cardgroups = [

    [
        {
            'header': 'Microsoft 2',
            'title': 'SDE II',
            'description':'This is an example. Some comment can be included here',
            'color':'light'  
        },

        {
            'header': 'Google',
            'title': 'SDE',
            'description':'This is an example. Some comment can be included here',
            'color':'warning'
        },

        {
            'header': 'Uber',
            'title': 'Data Analyst',
            'description':'This is an example. Some comment can be included here',
            'color':'light'  
        }        

    ]
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, cardgroups=cardgroups)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
