""" 
Luke Russell 
Wind Chill Calculator
4/3/21
"""
import math

def temp_celsius(user_temp):
    user_celsius = user_temp * 9/5 + 32
    return user_celsius

def wind_chill (T,V):
    TempFinal = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.42275*T*(V**0.16) 
    return TempFinal

user_temp = float(input("What is the temperature? "))
temp_type = (input("Is it Fahienheit or Celsius? Please input F or C: ").upper())
if temp_type == "C":
    user_temp = temp_celsius(user_temp)
wind_speed = 5
while wind_speed <= 60:
    ad_temp = wind_chill(user_temp,wind_speed)
    print(f"At {user_temp} degrees and wind speed {wind_speed}, the wind chill factor is: {ad_temp:.2f} degrees F.")
    wind_speed += 1