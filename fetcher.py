import requests
import json

def fetch_and_save_json(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()

        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"✅ Data successfully saved to '{output_file}'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as e:
        print(f"Error parsing JSON: {e}")

if __name__ == "__main__":
    url = "https://api.wstw.at/gateway/WL_WIENMOBIL_API/1/station_status.json"
    output_file = "data.json"
    fetch_and_save_json(url, output_file)
