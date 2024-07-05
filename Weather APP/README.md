Weather Web App

This Python-based web application fetches and displays current weather information using the OpenWeatherMap API. Users can input a city name to get real-time weather details including temperature, weather conditions, humidity, and wind speed.
## Directory Structure
weather_app/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **sign up at Openweathermap to get your api key**. 

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Replace 'your_openweathermap_api_key' in app.py with your API key**


## Installation
Clone or download the repository.

## Run Locally

Clone the project

Open a terminal and navigate to the weather_app directory.

```bash
 python app.py

```
Access the app in your web browser at http://127.0.0.1:5000/.

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Features

Input Form: Allows users to enter any city name to fetch weather details.

Weather Display: Shows temperature in Celsius, weather conditions, humidity percentage, and wind speed.

Error Handling: Displays appropriate messages if the city is not found or if there's an issue with the API.
## Technologies Used
Flask: Python web framework for backend development.

HTML/CSS: Frontend design and structure.

OpenWeatherMap API: Provides weather data for cities worldwide.
## Screenshots

![App Screenshot](C:\Users\kathi\OneDrive\Pictures\Screenshots\Screenshot 2024-07-04 151721.png)


## Summary
 Executing the application on your local machine for development and testing.