import requests


class IftttNotification:
    def __init__(self,event,api_key,jd = None):
        self.event = event
        self.api_key = api_key


    def notify(self,jd = {}):
        #create url
        url = f"https://maker.ifttt.com/trigger/{self.event}/json/with/key/{self.api_key}"

        try:
            print("Sending.....")
            response = requests.post(url,jd)
            #debug response
        
            if response.status_code == 200:
                print("request sent successfully")
            else:
                print("request send not successfull")
        except ConnectionError:
            print("Offline")
