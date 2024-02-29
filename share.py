# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def load_data(url, download_folder='images'):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # print(soup)

#     if not os.path.exists(download_folder):
#         os.makedirs(download_folder)


#     img_tags = soup.find_all('img')

#     for img_tag in img_tags:
#         img_url =  img_tag.get('src')
#         if img_url:
#             img_url = urljoin(url, img_url)
#             img_data = requests.get(img_url).content

#             img_name = os.path.join(download_folder, os.path.basename(img_url))
            

#             with open(img_name, 'wb') as img_file:
#                 img_file.write(img_data)
#                 print(f"Downloaded: {img_name}")


# for i in range(50):
#     i += 1
#     url = f"https://cspromogame.ru/avatars?page={i}"
#     print(url)
#     load_data(url)
        