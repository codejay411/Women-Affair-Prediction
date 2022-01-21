from flask import Flask, escape, request, render_template
import pickle
import pandas as pd
from patsy import dmatrices

model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        try:
            if request.form:
                # print("jadu")
                rate_marriage = request.form['rate_marriage']
                # print(rate_marriage)
                age = request.form['age']
                yrs_married = request.form['yrs_married']
                children = request.form['children']
                religious = request.form['religious']
                educ = request.form['educ']
                occupation = str(request.form['occupation'])
                occupation_husb = str(request.form['occupation_husb'])

                Intercept = 1

                # occupation
                if(occupation=='2'):
                    occ_2 = 1
                    occ_3 = 0
                    occ_4 = 0
                    occ_5 = 0
                    occ_6 = 0
                elif(occupation=='3'):
                    occ_2 = 0
                    occ_3 = 1
                    occ_4 = 0
                    occ_5 = 0
                    occ_6 = 0
                elif(occupation=='4'):
                    occ_2 = 0
                    occ_3 = 0
                    occ_4 = 1
                    occ_5 = 0
                    occ_6 = 0
                elif(occupation=='5'):
                    occ_2 = 0
                    occ_3 = 0
                    occ_4 = 0
                    occ_5 = 1
                    occ_6 = 0
                elif(occupation=='6'):
                    occ_2 = 0
                    occ_3 = 0
                    occ_4 = 0
                    occ_5 = 0
                    occ_6 = 1
                else:
                    occ_2 = 0
                    occ_3 = 0
                    occ_4 = 0
                    occ_5 = 0
                    occ_6 = 0
                
                # husband occupation
                if(occupation_husb=='2'):
                    occ_husb_2 = 1
                    occ_husb_3 = 0
                    occ_husb_4 = 0
                    occ_husb_5 = 0
                    occ_husb_6 = 0
                elif(occupation_husb=='3'):
                    occ_husb_2 = 0
                    occ_husb_3 = 1
                    occ_husb_4 = 0
                    occ_husb_5 = 0
                    occ_husb_6 = 0
                elif(occupation_husb=='4'):
                    occ_husb_2 = 0
                    occ_husb_3 = 0
                    occ_husb_4 = 1
                    occ_husb_5 = 0
                    occ_husb_6 = 0
                elif(occupation_husb=='5'):
                    occ_husb_2 = 0
                    occ_husb_3 = 0
                    occ_husb_4 = 0
                    occ_husb_5 = 1
                    occ_husb_6 = 0
                elif(occupation_husb=='6'):
                    occ_husb_2 = 0
                    occ_husb_3 = 0
                    occ_husb_4 = 0
                    occ_husb_5 = 0
                    occ_husb_6 = 1
                else:
                    occ_husb_2 = 0
                    occ_husb_3 = 0
                    occ_husb_4 = 0
                    occ_husb_5 = 0
                    occ_husb_6 = 0


                response = model.predict([[Intercept, occ_2, occ_3, occ_4, occ_5, occ_6, occ_husb_2, occ_husb_3, occ_husb_4, occ_husb_5, occ_husb_6, rate_marriage, age, yrs_married, children, religious, educ]])[0]
                # print(response)

                if(response=='1.0'):
                    response="YES"
                else:
                    response="NO"
                return render_template("prediction.html", prediction_text="Affair of Women - >"+str(response))

        except Exception as e:
            # print(e)
            # error = {"error": "Something went wrong!! Try again later!"}
            # error = {"error": e}
            return render_template("prediction.html", prediction_text=error)



    else:
        return render_template("prediction.html")


if __name__ == '__main__':
    app.debug = True
    app.run()