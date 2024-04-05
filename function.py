import json
import pickle
import config
import numpy as np
import datetime


class CarPrediction():
    def __init__(self,year,km_driven,fuel,seller_type,transmission,owner,car_brand_name):
        self.year = datetime.datetime.today().year - year
        self.km_driven= km_driven
        self.fuel=fuel
        self.seller_type=seller_type
        self.transmission=transmission
        self.owner=owner
        self.car_brand_name= 'car_brand_name_' + car_brand_name


    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predict_chagres(self):
        self.load_model()

        car_brand_name_index = self.json_data["columns"].index(self.car_brand_name)
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.year
        test_array[1] = self.km_driven
        test_array[2] = self.json_data['fuel'][self.fuel]
        test_array[3] = self.json_data['seller_type'][self.seller_type]
        test_array[4] = self.json_data['transmission'][self.transmission]
        test_array[5] = self.json_data['owner'][self.owner]
        test_array[car_brand_name_index] = 1

        # print('Test_array',test_array)

        predict_charges  = np.expm1(self.model.predict([test_array]))

        return predict_charges

    # km_driven= 70000
    # fuel = 'Petrol'
    # seller_type = "Individual"
    # transmission = 'Manual'
    # owner = 'First Owner'
    # car_brand_name = 'Maruti'  

    # car_price =  CarPrediction(year,km_driven,fuel,seller_type,transmission,owner,car_brand_name)
    # car_price.get_predict_chagres()
   
        