from flask import Flask, render_template, send_file



application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = './downloads'



@application.route('/main')
@application.route('/')
def index():
    return render_template('index.html')



@application.route('/download')
def download():
    return send_file("антивирус.txt", as_attachment=True)


@application.route('/faq')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    application.run(host="127.0.0.1", port=80)