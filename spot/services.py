import requests
from dataclasses import dataclass

@dataclass
class APIClient:
    # API Configuration
    BASE_URL = "https://spot-dj8q.onrender.com/"
    ENDPOINT = "/api/get_info_tracks"
    

    def get_tracks_info(self,track_id):
        """
        Fetch tracks information from the specified API endpoint.
        
        Returns:
        - dict: JSON response from the API
        - None: If there's an error during the API call
        """
        try:
            # Construct the full URL
            full_url = f"{self.BASE_URL.rstrip('/')}{self.ENDPOINT}"
            
            params = {
                "track_id": track_id
            }
            
            # Send GET request to the API
            response = requests.get(full_url, params=params)
            
            # Check if the request was successful
            response.raise_for_status()
            
            # Return the JSON response
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching tracks information: {e}")
            return None

    def get_tracks(self ):
        try:
            full_url = f"{self.BASE_URL.rstrip('/')}/api/get_tracks" 

            params = {
                "skip": 1,
                "limit": 100,
            }

            response = requests.get(full_url, params=params)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching tracks information: {e}")
            return None


# print(json.dumps(get_tracks_info(1)))
# def main():
#     # Fetch tracks information
#     tracks_data = get_tracks_info(1)
#
#     # Check if data was successfully retrieved
#     if tracks_data:
#         print("Tracks Information:")
#         # Pretty print the retrieved data
#         import json
#         print(json.dumps(tracks_data, indent=2))
#     else:
#         print("Failed to retrieve tracks information.")
#
# if __name__ == "__main__":
#     main()
