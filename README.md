# Weather Metrics

Poll weather services for current and forecasted weather conditions and store the data in InfluxDB for making pretty graphs.

## Configuration

The application is configured via environment variables.

- `CITY_ID_SET`: Set of city IDs for which to poll weather data. You can find a list of City IDs at [OpenWeatherMap's website](http://openweathermap.org/help/city_list.txt). Example: `(1796236, 1174872, 3448439)`. Default: `()`
- `INFLUXDB_URL`: Base URL of InfluxDB API to write metrics to. Default: `http://localhost:8086`
- `INFLUXDB_DATABASE`: InfluxDB database to write metrics to. Default: `weather`
- `INFLUXDB_USERNAME`: Username to use to connect to InfluxDB. The user should have write privileges. Default: `poller`
- `INFLUXDB_PASSWORD`: Password to use to connect to InfluxDB. Default: undefined.
- `OPENWEATHERMAP_API_KEY`: API key for OpenWeatherMap API. You can get a free key at [http://openweathermap.org/appid](OpenWeatherMap's website). Default: undefined.

## How to Develop

Install Docker and Docker Compose. Note that `docker-compose` typically must be run with root privileges.

Run `sudo docker-compose up` to launch InfluxDB and Grafana.

Navigate to [https://localhost:3000](http://localhost:3000) and log into Grafana with username 'admin' and password 'admin'.

Add an InfluxDB datasource with the following settings:

```
Name: <anything>
Default: true
Type: InfluxDB
Url: http://localhost:8086
Access: <anything>
HTTP Auth: <everything false>
Database: weather
User: grafana
Password: grafana
```

There are two ways of polling for data: running the `poll.py` script directly or running the script inside a container. Either way, you may run the poller inside of `watch` to gather data continuously. In production, the intent is for the polling script to be run at regular intervals in a serverless environment such as AWS Lambda.

### How to Run Directly

Install dependencies with `pip install -r requirements.txt`.

Run the poller with `./poll.py`.

### How to Run in a Container

Build an image using `sudo docker-compose build`.

Run `sudo docker-compose run poll`. 

