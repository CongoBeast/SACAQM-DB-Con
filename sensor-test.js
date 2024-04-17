const fs = require('fs');

function processSensorData(sensorId) {
  const filename = `${sensorId}.json`;  // Construct filename using sensor ID

  const data = fs.readFileSync(filename, "utf8");  // Synchronous file reading
  const parsedData = JSON.parse(data);

  // Array to hold processed data
  const processedData = {
    dates: [],
    pm1p0: [],
    pm2p5: [],
    pm4p0: [],
    pm10p0: [],
    nox: [],
    voc: [],
    humidity: [],
    temperature: [],
  };

  // Loop through the parsed JSON data
  for (const p of parsedData) {
    // Extract and format date
    const formattedDate = new Date(p["timestamp"]);

    // Populate processedData arrays
    processedData.dates.push(p["timestamp"]);
    processedData.pm1p0.push({ x: formattedDate.getTime(), y: parseFloat(p["pm1p0"]) });
    // ... (Similarly push other data for pm2p5, pm4p0, etc.)
  }

  return processedData;
}

// Example usage
const sensorId = "350457790675308";
const processedData = processSensorData(sensorId);


if (processedData) {
  console.log("Processed data:");
} else {
  console.error("Failed to process data for sensor", sensorId);
}
