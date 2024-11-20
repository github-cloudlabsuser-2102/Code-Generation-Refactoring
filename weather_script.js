const apiKey = 'YOUR_API_KEY';
const city = 'London';
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    const weatherDescription = data.weather[0].description;
    const temperature = data.main.temp;
    const humidity = data.main.humidity;
    const windSpeed = data.wind.speed;

    console.log(`Weather in ${city}:`);
    console.log(`Description: ${weatherDescription}`);
    console.log(`Temperature: ${temperature}°C`);
    console.log(`Humidity: ${humidity}%`);
    console.log(`Wind Speed: ${windSpeed} m/s`);
  })
  .catch(error => console.error('Error fetching the weather data:', error));