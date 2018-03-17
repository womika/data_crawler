from bs4 import BeautifulSoup
import requests
import pickle

doctor = 'ortopeda'
location = 'warszawa'

url = f'https://www.znanylekarz.pl/{doctor}/{location}'

r = requests.get(url)

with open('request_dump', 'wb') as file:
    pickle.dump(r, file)


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
