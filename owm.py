from pyowm import OWM
from  pyowm.utils import config
from pyowm.utils import timestamps

# observation = mgr.weather_at_place('Ghana,Africa')
# w = observation.weather

# print(w.detailed_status)
# print(w.humidity)
# print(w.temperature('celsius'))
# print(w.rain)
# print(w.heat_index)
# print(w.clouds)



def weatherCondition(place):
    owm = OWM('64cf3ae476e9d82677c0fb12030df926')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    print(w.detailed_status)
    print(w.humidity)
    print(w.temperature('celsius'))
    print(w.rain)
    print(w.heat_index)
    print(w.clouds)
    print(w.wind())
    

print('Hong Kong,China')
weatherCondition('Hong Kong,China')

print('\nTokyo,China')
weatherCondition('Tokyo,Japan')

print('\nKoforidua,Ghana')
weatherCondition('Koforidua,Ghana')

print('\nHo,Ghana')
weatherCondition('Ho,Ghana')

print('\nAccra,Ghana')
weatherCondition('Accra,Ghana')


# forecast = mgr.forecast_at_place('Milan,IT','daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())

# print(answer)