import requests

API_KEY = "54fea08f5ee2198740a7eb4c5f738248"
def get_date(place, forcast_days=None, kind=None):
	url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
	response = requests.get(url)
	data = response.json()
	filtered_data = data['list']
	nr_values = 8 * forcast_days
	filtered_data = filtered_data[:nr_values]
	if kind == 'Temperature':
		filtered_data = [dict['main']['temp'] for dict in filtered_data]
	if kind == 'Sky':
		filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
	return filtered_data

if __name__ == "__main__":
    print(get_date(place='Tokoyo', forcast_days=2, kind='Temperature'))