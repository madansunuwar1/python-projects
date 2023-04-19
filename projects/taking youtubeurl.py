
from flask import Flask,request,render_template,session
from pytube import YouTube
# from comment_extraction.ipynb import scrap_comment

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY']="never guess"

@app.route("/",methods=("GET","POST"))
def home():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        try:
            url = YouTube[session['link']]
            url.check_availability()
        except:
            return render_template('sentiment.html')
        return render_template('sentiment.html')
    return render_template('home.html')
    # result =scrap_comment()
    # return result
@app.route("/sentiment",methods=("GET","POST"))
def comment_analysis():
    pass

if __name__=='__main__':
    app.run(debug = True)