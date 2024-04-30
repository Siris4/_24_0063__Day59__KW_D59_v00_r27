from flask import Flask, render_template, jsonify
import datetime as dt
import requests

app = Flask(__name__)

MY_NAME = 'Gavin "Siris" Martin'  # defined globally for reuse in routes and/or functions

@app.route('/')
def home():
    current_year = dt.datetime.now().year
    copyright = f'Copyright {current_year} {MY_NAME}. All Rights Reserved.'
    return render_template('index.html', CURRENT_YEAR=copyright, page='home')

@app.route('/about')
def about():
    current_year = dt.datetime.now().year
    copyright = f'Copyright {current_year} {MY_NAME}. All Rights Reserved.'
    return render_template('about.html', CURRENT_YEAR=copyright, page='about')

@app.route('/contact')
def contact():
    current_year = dt.datetime.now().year
    copyright = f'Copyright {current_year} {MY_NAME}. All Rights Reserved.'
    return render_template('contact.html', CURRENT_YEAR=copyright, page='contact')

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    try:
        blog_response = requests.get(blog_url)
        blog_response.raise_for_status()  # Ensures we proceed only if the response was successful
        all_posts = blog_response.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve blog data: {e}")
        return jsonify({"error": "Unable to fetch blog posts", "details": str(e)}), 500
    current_year = dt.datetime.now().year
    copyright = f'Copyright {current_year} {MY_NAME}. All Rights Reserved.'
    return render_template("index.html", posts=all_posts, CURRENT_YEAR=copyright, page='home')

if __name__ == "__main__":
    app.run(debug=True)
