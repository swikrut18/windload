from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np


# Create your views here.

def home(request):
    return render(request,'a.html',{'titles':'Django','link':'http://127.0.0.1:8000/'})

def city(request):
    basic_wind_speed=(request.GET['city'])
    building_life_for_design=int((request.GET['building_life_design']))
    terrain_category=int((request.GET['terrain_category']))
    length=float((request.GET['length']))
    width=float((request.GET['width']))
    height=float((request.GET['height']))
    
    wind_speed = {
    'Agra': '47', 'Ahmedabad': '39', 'Ajmer': '47',
    'Almora': '47', 'Amritsar': '47', 'Asansol': '47',
    'Aurangabad': '39', 'Bahraich': '47', 'Bengaluru': '33',
    'Barauni': '47', 'Bareilly': '47', 'Bhatinda': '47',
    'Bhilai': '39', 'Bhopal': '39', 'Bhubaneshwar': '50',
    'Bhuj': '50', 'Bikaner': '47', 'Bokaro': '47', 
    'Chandigarth': '47', 'Chennai': '50', 'Coimbatore': '39',
    'Cuttak': '50', 'Darbhanga': '55', 'Darjeeling': '47',
    'Dehradun': '47', 'Delhi': '47', 'Durgapur': '47',
    'Gangtok': '47', 'Guwahati': '50', 'Gaya': '39',
    'Gorakhpur': '39', 'Hyderabad': '47', 'Imphal': '44',
    'Jabalpur': '47', 'Jaipur': '47', 'Jamshedpur': '47',
    'Jhansi': '47', 'Jodhpur': '47', 'Kanpur': '47',
    'Kohima': '47', 'Kolkata': '44', 'Kozhikode': '50',
    'Kurnool': '39', 'lakshadweep': '47', 'Lucknow': '47', 
    'Ludhiana': '39', 'Madurai': '39', 'Mandi': '39',
    'Manglore': '47', 'Muradabad': '44', 'Mumbai': '33',
    'Mysore': '44', 'Nagpur': '47', 'Nainital': '39',
    'Nasik': '50', 'Nellore': '39', 'Panjim': '47',
    'Patiala': '47', 'Patna': '50', 'Puducherry': '44',
    'Port Blair': '39', 'Pune': '39', 'Raipur': '39',
    'Rajkot': '39', 'Ranchi': '39', 'Roorkee': '39', 
    'Rourkela': '39', 'Simla': '39','Srinager': '44',
    'Surat': '47', 'Tiruchirapalli': '39',
    'Trivandrum': '47', 'Udaipur': '44', 'Vadodara': '47',
    'Varanasi': '50', 'Vijaywada': '50',
    'Visjakhapatnam': '50'
    }
   
    wind_speed_1 = float(wind_speed[basic_wind_speed])
   
    df = pd.DataFrame({'33': ['1', '0.82', '0.94', '1.05'],
                   '39': ['1', '0.76', '0.92', '1.06'],
                   '44': ['1', '0.73', '0.91', '1.07'],
                   '47': ['1', '0.71', '0.9', '1.07'],
                   '50': ['1', '0.7', '0.9', '1.08'],
                   '55': ['1', '0.67', '0.89', '1.08']
                   })
   
    # if building_life_for_design == 50:
        # global k1
        # k1 = df.iat[0, 0]

    # elif wind_speed_1 == 33 and building_life_for_design == 5:
        # k1 = df.iat[1, 0]
    
    # elif wind_speed_1 == 33 and building_life_for_design == 25:
        # k1 = df.iat[2, 0]    
    
    # elif wind_speed_1 == 33 and building_life_for_design == 100:
        # k1 = df.iat[3, 0]    
    
    # elif wind_speed_1 == 39 and building_life_for_design == 5:
        # k1 = df.iat[1, 1]    

    # elif wind_speed_1 == 39 and building_life_for_design == 25:
        # k1 = df.iat[2, 1]   

    # elif wind_speed_1 == 39 and building_life_for_design == 100:
        # k1 = df.iat[3, 1]    

    # elif wind_speed_1 == 44 and building_life_for_design == 5:
        # k1 = df.iat[1, 2]    

    # elif wind_speed_1 == 44 and building_life_for_design == 25:
        # k1 = df.iat[2, 2]   

    # elif wind_speed_1 == 44 and building_life_for_design == 100:
        # k1 = df.iat[3, 2]   

    # elif wind_speed_1 == 47 and building_life_for_design == 5:
        # k1 = df.iat[1, 3]    

    # elif wind_speed_1 == 47 and building_life_for_design == 25:
        # k1 = df.iat[2, 3]   

    # elif wind_speed_1 == 47 and building_life_for_design == 100:
        # k1 = df.iat[3, 3]   

    # elif wind_speed_1 == 50 and building_life_for_design == 5:
        # k1 = df.iat[1, 4]    

    # elif wind_speed_1 == 50 and building_life_for_design == 25:
        # k1 = df.iat[2, 4]   

    # elif wind_speed_1 == 50 and building_life_for_design == 100:
        # k1 = df.iat[3, 4]   

    # elif wind_speed_1 == 55 and building_life_for_design == 5:
        # k1 = df.iat[1, 5]    

    # elif wind_speed_1 == 55 and building_life_for_design == 25:
        # k1 = df.iat[2, 5]   

    # elif wind_speed_1 == 55 and building_life_for_design == 100:
        # k1 = df.iat[3, 5]   
    
    
    
    global k1
    
    if building_life_for_design == 50:
        k1 = df.iat[0, 0]

    elif wind_speed_1 == 33 and building_life_for_design == 5:
        k1 = df.iat[1, 0]
    
    elif wind_speed_1 == 33 and building_life_for_design == 25:
        k1 = df.iat[2, 0]    
    
    elif wind_speed_1 == 33 and building_life_for_design == 100:
        k1 = df.iat[3, 0]    
    
    elif wind_speed_1 == 39 and building_life_for_design == 5:
        k1 = df.iat[1, 1]    

    elif wind_speed_1 == 39 and building_life_for_design == 25:
        k1 = df.iat[2, 1]   

    elif wind_speed_1 == 39 and building_life_for_design == 100:
        k1 = df.iat[3, 1]    

    elif wind_speed_1 == 44 and building_life_for_design == 5:
        k1 = df.iat[1, 2]    

    elif wind_speed_1 == 44 and building_life_for_design == 25:
        k1 = df.iat[2, 2]   

    elif wind_speed_1 == 44 and building_life_for_design == 100:
        k1 = df.iat[3, 2]   

    elif wind_speed_1 == 47 and building_life_for_design == 5:
        k1 = df.iat[1, 3]    

    elif wind_speed_1 == 47 and building_life_for_design == 25:
        k1 = df.iat[2, 3]   

    elif wind_speed_1 == 47 and building_life_for_design == 100:
        k1 = df.iat[3, 3]   

    elif wind_speed_1 == 50 and building_life_for_design == 5:
        k1 = df.iat[1, 4]    

    elif wind_speed_1 == 50 and building_life_for_design == 25:
        k1 = df.iat[2, 4]   

    elif wind_speed_1 == 50 and building_life_for_design == 100:
        k1 = df.iat[3, 4]   

    elif wind_speed_1 == 55 and building_life_for_design == 5:
        k1 = df.iat[1, 5]    

    elif wind_speed_1 == 55 and building_life_for_design == 25:
        k1 = df.iat[2, 5]   

    elif wind_speed_1 == 55 and building_life_for_design == 100:
        k1 = df.iat[3, 5]   
        
        
    k1_1 = float(k1)
    
    df = pd.DataFrame({
    'Terrain Category 1': ['1.05', '1.09', '1.12', '1.15', '1.2',
    '1.26', '1.3', '1.32', '1.34', '1.35', '1.35', '1.35', '1.35', 
    '1.35'],
    'Terrain Category 2': ['1', '1.05', '1.07', '1.12', '1.17',
    '1.24', '1.28', '1.3', '1.32', '1.34', '1.35', '1.35', '1.35',
    '1.35'],
    'Terrain Category 3': ['0.91', '0.97', '1.01', '1.06', '1.12',
    '1.2', '1.24', '1.27', '1.29', '1.31', '1.32', '1.34', '1.35',
    '1.35'],
    'Terrain Category 4': ['0.8', '0.8', '0.8', '0.97', '1.1', 
    '1.2', '1.24', '1.27', '1.28', '1.3', '1.31', '1.32', '1.33',
    '1.34']
    })
    
    if terrain_category == 1 and height <= 10:
        global k2
        k2 = df.iat[0,0]
    elif terrain_category == 1 and 10.001 < height <= 15:
        k2 = df.iat[1,0]
    elif terrain_category == 1 and 15.001 < height <= 20:
        k2 = df.iat[2,0]
    elif terrain_category == 1 and 20.001 < height <= 30:
        k2 = df.iat[3,0]
    elif terrain_category == 1 and 30.001 < height <= 50:
        k2 = df.iat[4,0]
    elif terrain_category == 1 and 50.001 < height <= 100:
        k2 = df.iat[5,0]
    elif terrain_category == 1 and 100.001 < height <= 150:
        k2 = df.iat[6,0]
    elif terrain_category == 1 and 150.001 < height <= 200:
        k2 = df.iat[7,0]
    elif terrain_category == 1 and 200.001 < height <= 250:
        k2 = df.iat[8,0]
    elif terrain_category == 1 and 250.001 < height <= 300:
        k2 = df.iat[9,0]
    elif terrain_category == 1 and 300.001 < height <= 350:
        k2 = df.iat[10,0]
    elif terrain_category == 1 and 350.001 < height <= 400:
        k2 = df.iat[11,0]
    elif terrain_category == 1 and 400.001 < height <= 450:
        k2 = df.iat[12,0]
    elif terrain_category == 1 and 450.001 < height <= 500:
        k2 = df.iat[13,0]
    elif terrain_category == 2 and height <= 10:
        k2 = df.iat[0,1]
    elif terrain_category == 2 and 10.001 < height <= 15:
        k2 = df.iat[1,1]
    elif terrain_category == 2 and 15.001 < height <= 20:
        k2 = df.iat[2,1]
    elif terrain_category == 2 and 20.001 < height <= 30:
        k2 = df.iat[3,1]
    elif terrain_category == 2 and 30.001 < height <= 50:
        k2 = df.iat[4,1]
    elif terrain_category == 2 and 50.001 < height <= 100:
        k2 = df.iat[5,1]
    elif terrain_category == 2 and 100.001 < height <= 150:
        k2 = df.iat[6,1]
    elif terrain_category == 2 and 150.001 < height <= 200:
        k2 = df.iat[7,1]
    elif terrain_category == 2 and 200.001 < height <= 250:
        k2 = df.iat[8,1]
    elif terrain_category == 2 and 250.001 < height <= 300:
        k2 = df.iat[9,1]
    elif terrain_category == 2 and 300.001 < height <= 350:
        k2 = df.iat[10,1]
    elif terrain_category == 2 and 350.001 < height <= 400:
        k2 = df.iat[11,1]
    elif terrain_category == 2 and 400.001 < height <= 450:
        k2 = df.iat[12,1]
    elif terrain_category == 2 and 450.001 < height <= 500:
        k2 = df.iat[13,1]
    elif terrain_category == 3 and height <= 10:
        k2 = df.iat[0,2]
    elif terrain_category == 3 and 10.001 < height <= 15:
        k2 = df.iat[1,2]
    elif terrain_category == 3 and 15.001 < height <= 20:
        k2 = df.iat[2,2]
    elif terrain_category == 3 and 20.001 < height <= 30:
        k2 = df.iat[3,2]
    elif terrain_category == 3 and 30.001 < height <= 50:
        k2 = df.iat[4,2]
    elif terrain_category == 3 and 50.001 < height <= 100:
        k2 = df.iat[5,2]
    elif terrain_category == 3 and 100.001 < height <= 150:
        k2 = df.iat[6,2]
    elif terrain_category == 3 and 150.001 < height <= 200:
        k2 = df.iat[7,2]
    elif terrain_category == 3 and 200.001 < height <= 250:
        k2 = df.iat[8,2]
    elif terrain_category == 3 and 250.001 < height <= 300:
        k2 = df.iat[9,2]
    elif terrain_category == 3 and 300.001 < height <= 350:
        k2 = df.iat[10,2]
    elif terrain_category == 3 and 350.001 < height <= 400:
        k2 = df.iat[11,2]
    elif terrain_category == 3 and 400.001 < height <= 450:
        k2 = df.iat[12,2]
    elif terrain_category == 3 and 450.001 < height <= 500:
        k2 = df.iat[13,2]
    elif terrain_category == 4 and height <= 10:
        k2 = df.iat[0,3]
    elif terrain_category == 4 and 10.001 < height <= 15:
        k2 = df.iat[1,3]
    elif terrain_category == 4 and 15.001 < height <= 20:
        k2 = df.iat[2,3]
    elif terrain_category == 4 and 20.001 < height <= 30:
        k2 = df.iat[3,3]
    elif terrain_category == 4 and 30.001 < height <= 50:
        k2 = df.iat[4,3]
    elif terrain_category == 4 and 50.001 < height <= 100:
        k2 = df.iat[5,3]
    elif terrain_category == 4 and 100.001 < height <= 150:
        k2 = df.iat[6,3]
    elif terrain_category == 4 and 150.001 < height <= 200:
        k2 = df.iat[7,3]
    elif terrain_category == 4 and 200.001 < height <= 250:
        k2 = df.iat[8,3]
    elif terrain_category == 4 and 250.001 < height <= 300:
        k2 = df.iat[9,3]
    elif terrain_category == 4 and 300.001 < height <= 350:
        k2 = df.iat[10,3]
    elif terrain_category == 4 and 350.001 < height <= 400:
        k2 = df.iat[11,3]
    elif terrain_category == 4 and 400.001 < height <= 450:
        k2 = df.iat[12,3]
    elif terrain_category == 4 and 450.001 < height <= 500:
        k2 = df.iat[13,3]
    
        
    k2_2 = float(k2)    

    k3 = float(1.0)

    k4 = float(1.0)
    
    vz = wind_speed_1 * k1_1 * k2_2 * k3 * k4
    
    pz = 0.6 * vz ** 2
    
    area = width * height
    
    if area <= 10:
        ka = float(1)
    elif 10.001 < area <= 100:
        ka = float(0.9)
    else:
        ka = float(0.8)

    kc = float(0.9)

    vz_1 = float(pz * ka * kc)
    
    cpe = pd.DataFrame({
                    'cpe': ['0.7', '0.7', '0.7', '0.7', '0.8', '0.8',
                            '1.85', '1.25', '0.85']})

    bhr = height / width

    bpr = length / width

    if bhr <= 0.5 and 1 < bpr <= 1.5:
        cpe2 = cpe.iat[0,0]
    elif bhr <= 0.5 and 1.5 < bpr <= 4:
        cpe2 = cpe.iat[1,0]
    elif 0.5 < bhr <= 1.5 and 1 <= bpr <= 1.5:
        cpe2 = cpe.iat[2,0]
    elif 0.5 < bhr <= 1.5 and 1.5 <= bpr <= 4:
        cpe2 = cpe.iat[3,0]
    elif 1.5 < bhr <= 6 and 1 < bpr <= 1.5  :
        cpe2 = cpe.iat[4,0]
    elif 1.5 < bhr <= 6 and 1.5 <= bpr < 4:
        cpe2 = cpe.iat[5,0]
    elif bhr >= 6 and bpr <= 1.5:
        cpe2 = cpe.iat[3,0]
    elif 1.5 < bhr <= 6 and 1 < bpr <= 1.5  :
        cpe2 = cpe.iat[4,0]
    elif 1.5 < bhr <= 6 and 1.5 <= bpr < 4:
        cpe2 = cpe.iat[5,0]

    cpe1 = float(cpe2)
    cpi = float(2)

    c = cpe1 + cpi

    vz_2 = vz_1 * c

    
    
    
   
    
    return render(request,'city.html',{'city':vz_2})