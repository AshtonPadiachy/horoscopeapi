# Horoscope API CLI

This is a simple Python command-line application that fetches and displays your daily horoscope using the [API Ninjas Horoscope API](https://api-ninjas.com/api/horoscope).

## Features

- Prompts the user for their zodiac/star sign
- Fetches the daily horoscope from the API
- Displays the date, zodiac sign, and horoscope message

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/horoscopeapi.git
    cd horoscopeapi
    ```

2. **(Optional) Create a virtual environment:**
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**
    ```sh
    pip install requests
    ```

## Usage

1. Run the program:
    ```sh
    python main.py
    ```

2. When prompted, enter your zodiac/star sign (e.g., `virgo`, `gemini`, `leo`, etc.).

3. The program will display:
    - Today's date
    - Your zodiac sign
    - Your daily horoscope

## Important  
➡ Replace `'yourspecialapikeymustbeputhere'` in the code with your actual API key:

```python
response = requests.get(api_url, headers={'X-Api-Key': 'yourspecialapikeymustbeputhere'})
```

## Example

```
Welcome to the Horoscope API!
Enter your star sign: 
virgo
Today's date is: 2025-07-21

Your zodiac sign is: Virgo

Your horoscope is: Today is a day for careful planning and attention to detail, Virgo. ...
```

---

## License  

This project is for educational and personal use. Please respect API Ninjas' [terms of use](https://api-ninjas.com/tos).
