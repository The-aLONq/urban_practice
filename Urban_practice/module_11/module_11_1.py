from PIL import Image
from PIL import ImageGrab
import requests

#экран рабочего стола
screenshot = ImageGrab.grab()
screenshot.show()
screenshot.save('screenshot.png')

#развернуть на 180
with Image.open('screenshot.png') as im:
    im.rotate(180).show()
    im = im.resize((1280,720))
    im.show()

#сделать чб
screenshot = screenshot.convert('L')
screenshot.show()

#код ответа сервера
response = requests.get('https://api.github.com')
print(f"Status Code: {response.status_code}")

#проверка метода post
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

#узнаём cookies
url = 'https://github.com'
response = requests.get(url)
cookies = response.cookies
for cookie in cookies:
    print(f"Cookie Name: {cookie.name}, Value: {cookie.value}")
