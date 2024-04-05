from flask import Flask,jsonify,render_template,request
from urllib.parse import quote as url_quote
from function import CarPrediction
import numpy as np
import config

app = Flask(__name__)

car_brands = [
    "Audi", "BMW", "Chevrolet", "Daewoo", "Datsun", "Fiat", "Force",
    "Ford", "Honda", "Hyundai", "Isuzu", "Jaguar", "Jeep", "Kia", "Land",
    "MG", "Mahindra", "Maruti", "Mercedes-Benz", "Mitsubishi", "Nissan",
    "OpelCorsa", "Renault", "Skoda", "Tata", "Toyota", "Volkswagen", "Volvo"]

@app.route('/')
def home():
    return render_template("index.html",car_brands=car_brands)

@app.route('/predict',methods=['POST'])
def Predict_car_price():

    data = request.form

    year =         eval(data['year'])
    km_driven=     eval(data['km_driven'])
    fuel =         data['fuel']
    seller_type =  data['seller_type']
    transmission = data['transmission']
    owner =        data['owner']
    car_brand_name = data['car_brand_name']

    # print('year,km_driven,fuel,seller_type,transmission,owner,car_brand_name >>',year,km_driven,fuel,seller_type,transmission,owner,car_brand_name)

    car_price =  CarPrediction(year,km_driven,fuel,seller_type,transmission,owner,car_brand_name)
    charges = car_price.get_predict_chagres()
    return f'Your Estimated Car Price is = ₹ {np.round(charges[0],2)}'

if __name__ == '__main__':
    app.run(port = config.PORT_NUMBER,debug = False,host='0.0.0.0' ) # Server Start