import requests
import json


base_url = "https://api.thecatapi.com/v1/images/search?"
limit = "limit=2"
api_key = open(r"\Users\asus\Desktop\vcs codes\Module3\key.txt").read()
breed = "&has_breeds=1"

url = base_url + limit + "&api_key=" + api_key + breed

response = requests.get(url).json()
print(response)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response)

#first_cat = response[0]

#if "breeds" in first_cat:
    # Access the "id" of the breed from the first breed in the list
#    id = first_cat["breeds"][0]["id"]
#    print("Breed ID:", id)
#else:
#    print("No breed information found in the response.")


# Check if the response contains any data
if response:
    # Create a list to store the ids
    breed_ids = []

    # Iterate through each cat in the response
    for cat in response:
        # Check if "breeds" key is present in the current cat
        if "breeds" in cat:
            # Access the "id" of the breed from the first breed in the list
            breed_id = cat["breeds"][0]["id"]
            print("Breed ID:", breed_id)

            # Append the breed_id to the list
            breed_ids.append(breed_id)
        else:
            print("No breed information found for this cat.")
else:
    print("Empty response received from the API.")

# Now breed_ids contains the ids of all the breeds
print("All Breed IDs:", breed_ids)