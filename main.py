from pyscript import document

# Predetermined dictionary of weather instruments from the dataset
weather_instruments = {
    "Thermometer": (
        "Air Temperature",
        "Degrees Celsius (°C)",
        "Measures how hot or cold the air is."
    ),
    "Barometer": (
        "Atmospheric Pressure",
        "Hectopascals (hPa)",
        "Measures air pressure to help monitor weather changes."
    ),
    "Anemometer": (
        "Wind Speed",
        "Kilometers per hour (km/h)",
        "Measures how fast the wind is blowing."
    ),
    "Hygrometer": (
        "Relative Humidity",
        "Percent (%)",
        "Measures the amount of moisture in the air."
    ),
    "Rain Gauge": (
        "Rainfall",
        "Millimeters (mm)",
        "Measures the amount of rainfall in an area."
    ),
    "Wind Vane": (
        "Wind Direction",
        "Cardinal Directions",
        "Identifies the direction from which the wind is blowing."
    ),
    "Weather Balloon": (
        "Atmospheric Conditions",
        "Varies",
        "Collects atmospheric data at different altitudes."
    ),
    "Pyranometer": (
        "Solar Radiation",
        "Watts per square meter (W/m²)",
        "Measures incoming solar radiation."
    )
}

# Default tuple returned by .get() when an instrument is not in the dataset
not_found_info = (
    "Not included in the dataset",
    "Not included in the dataset",
    "This instrument is not included in the predetermined dataset."
)

def search_instrument(event):
    # Read user input and format words in Title Case
    raw_name = document.getElementById("instrument_input").value.strip().title()

    # Retrieve information using .get() with a default fallback
    measures, unit, purpose = weather_instruments.get(raw_name, not_found_info)

    # Display all required fields in the output container
    document.getElementById("instrument_output").innerHTML = f"""
        <p class="mb-1"><strong>Weather Instrument Name:</strong> {raw_name if raw_name else "-"}</p>
        <p class="mb-1"><strong>What It Measures:</strong> {measures}</p>
        <p class="mb-1"><strong>Unit of Measurement:</strong> {unit}</p>
        <p class="mb-0"><strong>Purpose:</strong> {purpose}</p>
    """