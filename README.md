Elections Scraper

Elections Scraper is a Python tool designed to scrape election results from the volby.cz website. Given the URL of a territorial unit, this script retrieves the voting results for all municipalities within that unit and saves them into a CSV file.

Features

- Scrape election results for a specified territorial unit.
- Automatically retrieves and aggregates results for all municipalities within the unit.
- Outputs the results to a CSV file for easy analysis.

Requirements

- Python 3.7+
- requests library
- beautifulsoup4 library

Installation

1. Clone the repository:

   git clone https://github.com/vasburov/project

2. Navigate to the project directory:

   cd elections_scraper

3. Create a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:

   pip install -r requirements.txt

Usage

To use the Elections Scraper, run the script from the command line with the URL of a territorial unit and the desired output CSV file name.

Example Command

scraper "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky_benesov.csv

This command will scrape the election results for the specified territorial unit and save them in a CSV file named vysledky_benesov.csv.

Command-Line Arguments

- URL: The URL of the territorial unit to scrape.
- Output File: The name of the CSV file where the results will be saved.

Example CSV Output

The output CSV file will be structured as follows:

code,location,registered,envelopes,valid,Party1,Party2,...

Each row represents a municipality within the specified territorial unit, with columns containing the election results for each political party.

License

This project is licensed under the MIT License.

Contact

For questions or suggestions, feel free to contact the author:

- Author: Vasyl Burov
- Email: vasylburov@gmail.com
- GitHub: https://github.com/vasylburov
