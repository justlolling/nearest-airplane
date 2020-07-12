#This uses the opensky api which can be found: https://github.com/openskynetwork/opensky-api
from opensky_api import OpenSkyApi
import math

#get distance of plane
def get_distance(plane_lat,plane_long):
    distance = math.sqrt((plane_lat - latitude)**2 + (plane_long - longitude)**2)
    return distance


#get a list of all planes within a certain proximity
latitude=float(input("please enter your latitude>> "))
longitude=float(input("please enter your longitude>> "))
api = OpenSkyApi()
states = api.get_states(bbox=(latitude-5, latitude+5, longitude-5, longitude+5))


#loop and find the minimum distance
minimum_distance=int(200)
for s in states.states:
    distance=get_distance(s.latitude, s.longitude)
    if distance < minimum_distance:
        minimum_distance = distance
        closest_plane=s
print("The closest plane is:\n "+closest_plane.callsign+"\nThe details about this plane: " +str(closest_plane))
print("The plane is " + str(minimum_distance * 111.111)+ " km away")




