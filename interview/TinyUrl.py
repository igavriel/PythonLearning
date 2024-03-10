import random
import string

class Url:
    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url

class UrlService:
    def __init__(self):
        self.urls = {}

    def create_url(self, original_url):
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        url = Url(original_url, short_url)
        self.urls[short_url] = url
        return url

    def get_url_by_short_url(self, short_url):
        return self.urls.get(short_url)

url_service = UrlService()

original_url = input("Enter the original URL: ")
url = url_service.create_url(original_url)
print(f"Short URL: http://tinyurl.com/{url.short_url}")
