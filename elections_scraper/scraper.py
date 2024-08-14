"""
scraper.py: Elections Scraper

author: Vasyl Burov
email: vasylburov@gmail.com
discord: vasylburov
"""

import sys
import requests
from bs4 import BeautifulSoup as bs
import csv

def get_soup(url):
    """Get BeautifulSoup object from URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        return bs(response.content, "html.parser")
    except requests.RequestException as e:
        sys.exit(f"Error fetching the URL: {url} - {e}")

def parse_obec_list(soup):
    """Parse the list of municipalities (obec) from the territorial unit soup."""
    obec_codes = [tag.text for tag in soup.select("td.cislo") if tag.find("a") is not None]
    obec_names = [tag.text for tag in soup.select("td.overflow_name")]
    obec_urls = [tag.find("a")["href"] for tag in soup.select("td.cislo") if tag.find("a") is not None]

    if not obec_names or not obec_urls or not obec_codes:
        sys.exit("Failed to parse municipalities from the given URL.")

    return list(zip(obec_codes, obec_names, obec_urls))

def parse_kandidujici_strany_names(soup):
    """Parse the names of political parties from the soup."""
    kandidujici_strany_names_tags = soup.find_all("td", headers="t1sa1 t1sb2")
    return [party.text for party in kandidujici_strany_names_tags]

def parse_obec_data(soup):
    """Parse voting data for a municipality from its soup."""
    def parse_cell(class_name, header_name):
        tag = soup.find('td', class_=class_name, headers=header_name)
        return tag.text.strip().replace(u"\xa0", "") if tag else "N/A"

    volici_v_seznamu = parse_cell('cislo', 'sa2')
    vydane_obalky = parse_cell('cislo', 'sa3')
    platne_hlasy = parse_cell('cislo', 'sa6')

    kandidujici_strany_votes_tags = soup.find_all('td', class_='cislo', \
                                    headers=lambda h: 't1sb3' in h or 't2sb3' in h)
    kandidujici_strany_votes = [data.text.strip().replace(u"\xa0", "") \
                               for data in kandidujici_strany_votes_tags]

    return [volici_v_seznamu, vydane_obalky, platne_hlasy] + kandidujici_strany_votes

def write_csv_header(csv_writer, kandidujici_strany_names):
    """Write the CSV header with party names."""
    csv_header = ["code", "location", "registered", "envelopes", "valid"]
    csv_header.extend(kandidujici_strany_names)
    csv_writer.writerow(csv_header)

def scrape_elections_data(uzemni_celek_url, vystupni_soubor_name):
    """Scrape elections data and write it to a CSV file."""
    home_directory = uzemni_celek_url.rsplit('/', 1)[0] + "/"
    
    soup_uzemni_celek = get_soup(uzemni_celek_url)
    obci = parse_obec_list(soup_uzemni_celek)

    prvni_obec_url = home_directory + obci[0][2]
    
    soup_kandidujici_strany = get_soup(prvni_obec_url)
    kandidujici_strany_names = parse_kandidujici_strany_names(soup_kandidujici_strany)

    with open(vystupni_soubor_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        write_csv_header(csv_writer, kandidujici_strany_names)

        for obec_code, obec_name, obec_url in obci:
            soup_obec = get_soup(home_directory + obec_url)
            csv_row = [obec_code, obec_name] + parse_obec_data(soup_obec)
            csv_writer.writerow(csv_row)

def main():
    """Main entry point of the script."""
    if len(sys.argv) != 3:
        sys.exit("Usage: python scraper.py <uzemni_celek_url> <vystupni_soubor_name>")

    uzemni_celek_url = sys.argv[1]
    vystupni_soubor_name = sys.argv[2]
    
    scrape_elections_data(uzemni_celek_url, vystupni_soubor_name)

if __name__ == "__main__":
    main()
