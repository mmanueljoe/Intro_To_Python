from geopy import distance
from geopy import Nominatim
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_coordinates(point):
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(point)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None

def geodesicDistanceMiles(point1,point2):
    a = distance.distance(point1,point2.miles)
    return a

def greatCircleDistanceMiles(point1,point2):
    a = distance.great_circle(point1,point2.miles)
    return a


def distanceUsingModelMiles(point1,point2,model):
    a = distance.geosidic(point1,point2,ellipsoid='model').miles
    return a


def geodesicDistanceKm(point1,point2):
    a = distance.distance(point1,point2.km)
    return a



def main():
    point1 = input("Enter the first city: ")
    point2 = input("Enter the second city: ")

    coordinates1 = get_coordinates(point1)
    coordinates2 = get_coordinates(point2)
    
    print("Choose an option to calculate distance \n1.Geodesic Distance in Miles \2.Great Circle Distance in Miles \3.Geodesic Distance in Km")

    option = int(input())

    if option == 1:           
        distance = geodesicDistanceMiles(coordinates1, coordinates2)
        if distance is not None:
            print(f"The distance between {point1} and {point2} is approximately {distance:.2f} miles.")
        else:
            print("Unable to calculate distance.")
    elif option == 2:
        distance = greatCircleDistanceMiles(coordinates1, coordinates2)
        if distance is not None:
            print(f"The distance between {point1} and {point2} is approximately {distance:.2f} miles.")
        else:
            print("Unable to calculate distance.")
    elif option == 3:
        distance = geodesicDistanceKm(coordinates1, coordinates2)
        if distance is not None:
            print(f"The distance between {point1} and {point2} is approximately {distance:.2f} kilometers.")
        else:
            print("Unable to calculate distance.")

# if __name__ == "__main__":
#     main()


main()
