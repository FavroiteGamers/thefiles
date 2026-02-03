import requests
from bs4 import BeautifulSoup
url = 'https://example.com'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
download_links = soup.find_all('a', href=True)
file_urls = [link['href'] for link in download_links if link['href'].endswith(('.zip', '.pdf'))
for file_url in file_urls:
    file_response = requests.get(file_url)
    print(file_response)
