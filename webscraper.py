import requests
from bs4 import BeautifulSoup
from datetime import date

def get_current_date() -> date:  
    current_date = date.today()
    current_date = current_date.replace(day = current_date.day-1)
    return current_date

def form_url(date:str) -> str:
    return f"https://spotifycharts.com/regional/global/daily/{date}"

def get_content(URL:str) -> BeautifulSoup:
    web_page = requests.get(URL)
    content = BeautifulSoup(web_page.content,'html.parser')
    return content

def get_title_results(content:BeautifulSoup,sections:str,class_of_title:str,element:str) -> [str]:
    title_results = content.find_all(sections,class_=class_of_title)
    text_title_results = [title.find(element).get_text() for title in title_results]
    return text_title_results

def get_stream_results(content:BeautifulSoup,sections:str,class_of_streams:str) -> [str]:
    stream_results = content.find_all(sections,class_=class_of_streams)
    text_stream_results = [stream.get_text() for stream in stream_results]
    return text_stream_results

def combine_results(titles:[str],streams:[str]) -> [{int:(str,str)}]:
    results = []
    ranking = 1
    for title,stream in zip(titles,streams):
        results.append({ranking:(title,stream)})
        ranking+=1
    return results

def output_results(results:[{int:(str,str)}]):
    for result in results:
        for key,value in result.items():
            print(f"{key}. Track: {value[0]} Number of Streams: {value[1]}")


def main():
    today = get_current_date()
    URL = form_url(today)
    content = get_content(URL)
    stream_results = get_stream_results(content,'td','chart-table-streams')
    title_results = get_title_results(content,'td','chart-table-track','strong')
    results = combine_results(title_results,stream_results)
    output_results(results)

if __name__ == '__main__':
    main()

