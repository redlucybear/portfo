from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('./html/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template('./page_name')

@app.route('/errorpage.html')
def error():
    return render_template('./html/errorpage.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('./html/thankyou.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return render_template('./errorpage.html')

@app.route('/index.html')
def index():
    return render_template('./html/index.html')

@app.route('/home.html')
def home():
    return render_template('./html/home.html')

@app.route('/about.html')
def about():
    return render_template('./html/about.html')

@app.route('/contact.html')
def contact():
    return render_template('./html/contact.html')

@app.route('/services.html')
def services():
    return render_template('./html/services.html')

@app.route('/blog-single.html')
def blog_single():
    return render_template('./html/blog-single.html')

@app.route('/blog.html')
def blog():
    return render_template('./html/blog.html')