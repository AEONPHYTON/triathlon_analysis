import requests

headers = {
    "accept": "application/json",
    "apikey": "INSERT YOU API KEY"
}

# to download all file 


for n in range(0, 200000):

    url = f"https://api.triathlon.org/v1/events/{n}/programs?is_race=true"

    response = requests.get(url, headers=headers, timeout=None)

    # save file as json file
    writeFile = open(f'INSERT THE PATH OF YOUR FOLDER/event_list_{n}.json', 'w')
    writeFile.write(response.text)
    writeFile.close()

    percentage = float(n/200000)*100
    print(f"Downloaded the file number {n}, you are at {percentage}%")
