# INCXLNXVLCJAQ7ERAFUL
# headers = {
#     'Authorization': 'Bearer INCXLNXVLCJAQ7ERAFUL'
# }

# params = {
#     'location.address': 'Berlin',
#     'location.within': '10km'
# }

# import requests

# # url = 'https://www.eventbriteapi.com/v3/events/search/'
# # url = f'https://www.eventbriteapi.com/v3/events/{2342342}/structured_content/?purpose=listing'
# url = f'https://www.eventbriteapi.com/v3/users/me/organizations/'

# print(url)
# response = requests.get(url, headers=headers, params=params)
# events = response.json()
# print(events)

# for event in events['events']:
# 	print(f"Event: {event['name']['text']}")
# 	print(f"Date: {event['start']['local']}")
# 	print(f"Venue: {event['venue']['name']}")
# 	print("---")
import requests

# Replace with your Eventbrite API key
API_KEY = 'INCXLNXVLCJAQ7ERAFUL'

# Base URL for Eventbrite API
BASE_URL = 'https://www.eventbriteapi.com/v3/'

# Function to get events
def get_events(location=None, query=None, page=1):
    """
    Fetch events from Eventbrite API.
    
    :param location: A string representing the location for the search (e.g., 'San Francisco').
    :param query: A string to search for specific events (e.g., 'music', 'tech').
    :param page: The page number for paginated results.
    :return: A dictionary containing the events.
    """
    # Define API endpoint and parameters
    url = f'{BASE_URL}events/search/'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    # Define query parameters
    params = {
        'location.address': location,  # Specify location for the event (optional)
        'q': query,  # Search term (optional)
        'page': page,  # Pagination page number (optional)
        'expand': 'venue'  # Expand to include venue details
    }
    
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        # Print an error message if something went wrong
        print(f'Error: {response.status_code} - {response.text}')
        return None

# Example usage
if __name__ == '__main__':
    # Fetch events in New York related to "technology"
    location = 'New York'
    query = 'technology'
    events_data = get_events(location=location, query=query)
    
    if events_data:
        # Print event details
        for event in events_data['events']:
            print(f"Event: {event['name']['text']}")
            print(f"Start: {event['start']['local']}")
            print(f"Venue: {event['venue']['name'] if 'venue' in event else 'N/A'}")
            print('-' * 40)

