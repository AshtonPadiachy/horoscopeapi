import requests

#prompt user for star sign
print("Welcome to the Horoscope API!")
starsignname = input("Enter your star sign: \n").strip().lower()

api_url = 'https://api.api-ninjas.com/v1/horoscope?zodiac={}'.format(starsignname)

#GET request to the Horoscope API with the required API key
response = requests.get(api_url, headers={'X-Api-Key': 'yourspecialapikeymustbeputhere'})

#uncomment below to test raw API response for debugging
#if response.status_code == requests.codes.ok:
 #   print(response.text)
#else:
 #   print("Error:", response.status_code, response.text)

#check if the response is OK
if response.status_code == requests.codes.ok:
    data = response.json()   
    
    #extract and display the date from the response
    date_today = data.get('date', 'N/A')
    print(f"Today's date is: {date_today}\n")

    #extract and display the zodiac sign from the response
    #note: some responses may use 'zodiac' instead of 'sign'
    zodiac_sign = data.get('zodiac') or data.get('sign', 'N/A')
    print(f'Your zodiac sign is: {zodiac_sign}\n')

    #extract and display the horoscope text
    horoscope_text = data.get('horoscope', 'N/A')
    print(f'Your horoscope is: {horoscope_text}\n')

else:
    #print error details if the API call was not successful
    print("Error:", response.status_code, response.text)



