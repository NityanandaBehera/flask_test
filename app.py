from flask import Flask,render_template
app = Flask(__name__)
JOBS= [
        {
        'id':1,
        'title':"Data Analyst",
        'Location':"Odisha",
        'salary':'Rs 300000'
        },{
        'id':2,
        'title':" Software developer",
        'Location':"Odisha",
        'salary':'Rs 500000'
        },
        {
        'id':3,
        'title':"Django developer",
        'Location':"Odisha",
        'salary':'Rs 500000'
        },
        {
        'id':4,
        'title':"Data Analyst",
        'Location':"Bangalur",

        'salary':'Rs 400000'
        }
    ]
@app.route("/")
def hello_world():
    return render_template('index.html',jobs=JOBS)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)