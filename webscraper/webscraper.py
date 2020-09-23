import requests
from bs4 import BeautifulSoup
from datetime import date

def get_current_date() -> date:
    """Gets the most recent date for Spotify's Global Top 200 and returns it as a Date object"""  
    current_date = date.today()
    current_date = current_date.replace(day = current_date.day-1)
    return current_date

def form_url(date:str) -> str:
    """Creates a URL given a date object"""
    return f"https://spotifycharts.com/regional/global/daily/{date}"

def get_content(URL:str) -> BeautifulSoup:
    """Retrieves the HTML content of the webpage and returns the content as a BeautifulSoup object"""
    web_page = requests.get(URL)
    content = BeautifulSoup(web_page.content,'html.parser')
    return content

def get_title_results() -> [str]:
    """Gets the song titles"""
    content = create_url_and_get_content()
    title_results = content.find_all('td',class_='chart-table-track')
    text_title_results = [title.find('strong').get_text() for title in title_results]
    return text_title_results

def get_stream_results() -> [int]:
    """Gets the number of streams"""
    content = create_url_and_get_content()
    stream_results = content.find_all('td',class_='chart-table-streams')
    text_stream_results = [stream.get_text() for stream in stream_results]
    int_stream_results = [int(result.replace(',','')) for result in text_stream_results]
    return int_stream_results

def combine_results(titles:[str],streams:[str]) -> [{int:(str,str)}]:
    """Combines title and stream results; Because the data is already sorted in the HTML content, the data is zipped together"""
    results = []
    ranking = 1
    for title,stream in zip(titles,streams):
        results.append({ranking:(title,stream)})
        ranking+=1
    return results

def output_results(results:[{int:(str,str)}]):
    """Prints combined results"""
    for result in results:
        for key,value in result.items():
            print(f"{key}. Track: {value[0]} Number of Streams: {value[1]}")

def create_url_and_get_content():
    """Returns a BeautifulSoup object containing the webpage's content"""
    today = get_current_date()
    URL = form_url(today)
    content = get_content(URL)
    return content



