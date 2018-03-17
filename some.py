from bs4 import BeautifulSoup
import requests
import pickle
import json

doctor = 'ortopeda'
location = 'warszawa'

url = f'https://www.znanylekarz.pl/{doctor}/{location}'

# r = requests.get(url)

with open('request_dump', 'rb') as file:
    r = pickle.load(file)

soup = BeautifulSoup(r.content, "html.parser")

search_results = soup.find(attrs={'data-id':"search-results-container"})

# search_results.ul.find_all(attrs={'itemprop':'name'})

# [tag.attrs for tag in search_results.ul.find_all(class_="rank-element")]


for tag in search_results.ul.find_all(class_="rank-element"):
    name = tag.find(attrs={'itemprop':'name'})
    tag.attrs.update({'name': name.text})
    # print(name.text)
    nearest_date = tag.find(class_="rank-element-nearest-date")
    tag.attrs.update(nearest_date.attrs)
    print(json.dumps(tag.attrs, indent=4))
    # print(tag.attrs)


# def get_chapter(url, chapter_no):
#     response = requests.get(url)
#     chapter_html = BeautifulSoup(response.content, "html.parser")
#     return chapter_html


# # soup = get_chapter(url, chapter_no)


# def get_chapter_text(chapter_html):
#     story_text = chapter_html.find(class_="storytext")
#     return story_text


# # story = get_chapter_text(soup)


# def save_chapter(chapter, chapter_no, file):
#     chapter_prefix = f"""Chapter {chapter_no}

#     """

#     if chapter_no == 1:
#         print(title_top, file=file)
#     print(chapter_prefix, file=file)
#     for tag in chapter.descendants:
#         if tag.name == 'p':  # text
#             print(tag.get_text(), file=file)
#     print(chapter_suffix, file=file)


# with open(f'{title}.txt', mode='w+', buffering=10000) as f:
#     for chapter_no in range(1, 69):
#         url = url
#         chapter = get_chapter_text(get_chapter(url, chapter_no))
#         save_chapter(chapter, chapter_no, file=f)
