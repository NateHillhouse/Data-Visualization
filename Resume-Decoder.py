from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def parse_data():
    url = input('Please Enter The URL For the Google Doc with the Code, or Enter "ex" for an Example: ').strip()
    while not url.startswith("http") and not url == ("ex"):
        print("Invalid URL. Please ensure it starts with 'https://' or 'http://'.")
        url = input("Please Enter The URL For the Google Doc with the Code: ").strip()
    if url == 'ex':
            print('url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"')
            url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub" 
    res = requests.get(url)
    text = bs(res.text, 'html.parser')
    text = text.find_all('table')
    table = pd.read_html(str(text), header=0)
    table = pd.DataFrame(table[0])
    table.sort_values(by=['x-coordinate', 'y-coordinate'], inplace=True, ascending=[True, False])
    return table

def print_message(data):
    yvalues = data['y-coordinate'].unique()
    xvalues = data['x-coordinate'].unique()
    for y in yvalues:
        char = []
        for x in xvalues:
            if x in data['x-coordinate'].values and y in data['y-coordinate'].values:
                try:
                    char.append(data['Character'][data['x-coordinate'] == x][data['y-coordinate'] == y].values[0])
                except Exception as e:
                    char.append(' ')
        print(''.join(char))
                

if __name__ == "__main__":
    data = parse_data()
    print_message(data)



    
    url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub" 