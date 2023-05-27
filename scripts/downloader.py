import os
import datetime
import mimetypes
import requests

# Log to file
def log(logfile, message):
    if not os.path.isfile(logfile):
        with open(logfile, 'w', encoding='utf-8'):
            pass
    with open(logfile, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp} - {message}\n')

# Download file from an URL to destination dir
def download_file(url, dest_dir):
    print(f"Downloading from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.basename(url)
        base, extension = os.path.splitext(filename)
        # Prevent empty filename
        if filename == '':
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            filename = timestamp
        # Guess extension from mimetype, default is .pdf
        elif not extension:
            content_type = response.headers.get('Content-Type')
            extension = mimetypes.guess_extension(content_type)
            filename = f"{base}{'.pdf' if not extension else extension}"
        filename = f"{dest_dir}/{filename}"
        with open(filename, 'wb') as f:
            f.write(response.content)
        log('log/success.log', f'{url} - Downloaded successfully: {filename}')
    else:
        log('log/error.log', f'{url} - Error while downloading\n{response}')

url_file = 'workspace/urls_ajmao.txt'

urls = []

# Download from each URL in file
with open(url_file, 'r') as f:
    urls = f.readlines()

for url in urls:
    download_file(url.strip(), 'docs/downloads')
