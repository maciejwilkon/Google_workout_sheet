import requests
import datetime

# Insert your data below as provided #
GENDER = None
WEIGHT_KG = None
HEIGHT_CM = None
AGE = None
# Insert your data above as provided#

# Use your own app ID and apikey#
nutri_api_id = "YOU_APP_ID"
nutri_api_key = "YOUR_API_KEY"

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
endpoint_get = 'https://trackapi.nutritionix.com/v2/search/item'
jwt_token = {
    'x-app-id': nutri_api_id,
    'x-app-key': nutri_api_key,
}
exercise = input('What exercise did you do?: \n')
parameters = {
    'query': exercise,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}
response = requests.post(url=endpoint, headers=jwt_token, json=parameters)
results = response.json()
print(results)  # This line is just for code testing measures, you can delete it if you want #

# Insert your own apikey from sheety below #
sheety_post_api = "YOUR_API_FROM_SHEETY"

now = datetime.datetime.now()
today = now.strftime("%Y/%m/%d")

time = now.strftime("%X")
ex_params = {
    "nix_item_id": "exercise time calories"

}
for exercise in results["exercises"]:
    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(url=sheety_post_api, json=sheety_params)
    print(sheet_response.text) # This line is just for code testing measures, you can delete it if you want #




