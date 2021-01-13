import os
import urllib.request


def save_page(url, title, path):
    print(url)
    file_name = title + '.html'
    try:
        urllib.request.urlretrieve(url, f"{path}\\{file_name}")
    except:
        print("Ups... Cofam")
        exit()


pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}
]

path = os.getcwd()
print("The current working directory is %s" % path)

try:
    os.mkdir(path + "/pages")
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

path = path + r'\pages'

for page in pages:
    save_page(page['url'], page['name'], path)
else:
    print("Wszystkie strony zostały pobrane!")

