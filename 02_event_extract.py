import requests
import json

headers = {
    "accept": "application/json",
    "apikey": "INSERT YOU API KEY"
}

# The json file without information has this information

specific_content = {"code": 200, "status": "success", "data": None}

for i in range(0, 200000):
    try:
		# insert the folder directory when you saved the event_list json file
		
        with open(f"INSERT THE PATH OF YOUR FOLDER/event_list_{i}.json", "r") as file:
            data = json.load(file)

		# check if the file have information or not
		
        if data == specific_content:
            print(f"{i} it's not available")
            continue

		# if the file have information about program id and event id, dowload all information
		
        info = data["data"]
        for item in info:
            prog_id = item["prog_id"]
            event_id = item["event_id"]

            url = f"https://api.triathlon.org/v1/events/{event_id}/programs/{prog_id}/results"
            response = requests.get(url, headers=headers, timeout=None)

			#insert the directory when you want to save the json file
			
            with open(f"INSERT THE PATH OF YOUR FOLDER/{prog_id}.json", "w") as writeFile:
                writeFile.write(response.text)

            print(f"Event {i} in elaboration ... {prog_id} completed")

    except Exception as e:
        print(f"Error in the file number {i}: {e}")

    percentage = (i / 200000) * 100
    print(f"completed percentage {percentage}%")