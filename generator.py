import pathlib  #where we are?
from pathlib import Path
import os       #catalogs and files support
from shutil import copyfile

#variables
source_path = pathlib.Path().absolute()
source_index_file = source_path / "index.html"
source_images_path = source_path / "/images"
source_content_path = source_path / "/content"
source_favicon_path = source_path / "./content/images/" / "favicon.png"
source_texts_files_path = source_path / "content/texts"

public_path = str(source_path) + "/" + "public"
public_file_path = ''
public_index_file = public_path + "/" + "index.html"
public_styles_file = public_path + "/" + "style.css"
public_images_path = public_path + "/" + "images"
public_content_path = public_path + "/" + "content"
public_texts_path = public_content_path + "/" + "texts"
public_favicon_path = public_images_path + "/content" + "favicon.png"
public_texts_files_path = public_path + "/content/texts"
public_categories_files_path = public_path + "/" + "content/texts/"


filename = ''
filePath = "public"
meta = str(open('index.html', 'r').read())
header = str(open('header.html', 'r').read())
nav = str(open('nav.html', 'r').read())
aside = str(open('aside.html', 'r').read())
content = str(open('index-content.html', 'r').read())
footer = str(open('footer.html', 'r').read())

#functions
## generowanie plików html dla content bez kategorii
def htmlGen(filename, filePath, fileType, meta, header, nav, aside, content, footer):
    if (filename == "index.html"):
        public_file_path = filePath
    else:
        public_file_index = filePath.find('/content/')
        public_file_path = filePath[:public_file_index] + '/public' + filePath[public_file_index:] ##tutaj jest dodawany folder public do ścieżki
    #zlepianie części składowych w jedną zmienną i zapis do pliku
    with open(public_file_path,'wt') as f:
        f.write(meta)
        f.write(header)
        f.write(nav)
        f.write(aside)
        f.write(content)
        f.write(footer)
        f.close()

#files and folders creation
os.makedirs((public_path))
os.makedirs((public_images_path))
os.makedirs((public_content_path))
os.makedirs((public_texts_path))
os.mknod(public_index_file)
os.mknod(public_styles_file)

# favicon copied
copyfile(source_favicon_path, public_favicon_path)

# # create index.html (meta-header)
# htmlGen("index.html", public_path, "site", meta, header, nav, aside, content, footer)

#html creations
for subdir, dirs, files in os.walk(source_texts_files_path):
    for filename in files:
        print("przejście pętli")
        filePath = subdir + os.sep + filename
        #jeżeli pliki są w głównym katalogu texts
        if os.path.dirname(filePath).endswith("texts") and (filePath.endswith(".md") or filePath.endswith(".html") or filePath.endswith(".htm")):
            fileType = "site"
            content = str(open(filePath, 'r').read())
            print("pierwszy if sie wykonuje")
            #w tym miejscu zmienna filePath którą przekażę do funkcji htmlGen musi zawierać ścieżkę z PUBLIC katalogie a nie bez
            htmlGen(filename, filePath, fileType, meta, header, nav, aside, content, footer)
        #jeżeli pliki są głębiej, w katalogu categories to zrób tego ifa a nie wyższego
        elif os.path.dirname(public_texts_path).endswith("texts") == False and (filePath.endswith(".md") or filePath.endswith(".html") or filePath.endswith(".htm")):
            fileType = "category"
            content = str(open(filePath, 'r').read())
            print("drugi if sie wykonuje")
            #w tym miejscu zmienna filePath którą przekażę do funkcji htmlGen musi zawierać ścieżkę z PUBLIC katalogie a nie bez
            htmlGen(filename, filePath, fileType, meta, header, nav, aside, content, footer)


# generowanie nav i aside może być przydatna biblioteka https://www.crummy.com/software/BeautifulSoup/   podobno można nią też robić xmle więc rss i sitemapy może też da radę
# albo po prostu na podstawie skanowania z tworzenia plików zrobić pętle która dla typu site robi wpisy do słownika który stworzy potem nav i osobno wpisy dla typu typu category robi wpisy do słownika który potem zrobi aside
#w każdym razie musi to zostać wygenerowane przed rozpoczęciem tworzenia plików html żeby przy generowani podstron kategorii i stron już generowały się one z dobrym nav i aside

# skan stylów css
# for subdir, dirs, files in os.walk(source_path):
#     for filename in files:
#         filepath = subdir + os.sep + filename

#         if filepath.endswith(".css"):
#             print (filepath)

# skan zdjęć
# for subdir, dirs, files in os.walk(source_path):
#     for filename in files:
#         filepath = subdir + os.sep + filename

#         if filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".png") or filepath.endswith(".gif"):
#             print (filepath)


# skan content log
# for subdir, dirs, files in os.walk("source_path/content/log"):
#     for filename in files:
#         filepath = subdir + os.sep + filename

#         if filepath.endswith(".md") or filepath.endswith(".html"):
#             print (filepath)


# pętla która generuje stronę (markdown html import export) md-to-html pip
# sklejenie i generacja plikówcssów
# skan wszystkich jsów i sklejenie jako jeden js
# ładne dopracowanie html css i md i js też pod mobilki!
# poczyszczenie skeletonowych plików żeby było tylko to co ważne???
# tworzenie podstrony typu news/logs????
# go to up w stopce, go to down u góry gdzieś? logo klikalne
# trim htmlów i cssów i jsów

# tworzenie unikalnego kodu na podstawie zawartości całego katalogu (md5?) i wrzucanie tego razem z datą do komentarza na samej górze strony + dopisanie funkcji w skrypcie która porównuje czy jest to to samo co na stronie za pomocą curla? curl http://www.stomski.pl | head -n3 > example.html albo pythonowe requests resp = req.get("http://www.webcode.me")The get() method returns a response object.  print(resp.text) http://zetcode.com/python/requests/ i w zależności od parametru, generowanie kodu z datą, generowanie tylko kodu, generowanie tylko daty, sprawdzanie kodu, sprawdzanie daty, sprawdzanie i kodu i daty, wyświetlenie tylko jaka data i kod zostałby wygenerowany teraz przy odpaleniu skryptu
# utworzenie .htaccess
# kilka gotowych skinów: white, white solarized, gray, gray solarized, dark, dark solarized zmiana tylko p,a,background wybieralne parametrem
# poprawiony osobny css do druku? i jakieś knefle do drukowania do pdf i drukarką?
# stworzenie pliku readme
#może jakiś meta plik z tytułem strony, autorem, description, ustawieniem htaccess i komentarzem? calość niech wpł←wa na to jak się wykona skrypt

# generacja rss PyRSS2Gen-1.1
# generacja sitemapy sitemap-generator
# opytymalizacja zdjęć? możnaby ją załączać dodatkowym parametrem przy odpalaniu skryptu -rekursywnie całość, rekursywnie to co nie istnieje w public/images, kopiowanie, i nie robienie nic w zależności od parametru

# funckaj któ©a sprawdza czy win/lin/mac i podmienia w skrypcie to co nie działa na to co działa w zależności od systemu. może nie jest to konieczne?

# dodanie emoji i ionnych czcionek
# dodanie w podstrony/ikony/stopki cokolwiek do kontaktu z autorem? email czy też youtube twitter cokolwiek na podstawie metadanych przy generowaniu w osobny pliku?
# dodanie tej fajnej opcji dodawania strony jako apka pod androidem?
# generowanie spisów treści dla h1 h2 h3 h4 dla każdej podstrony? jako prawy aside albo jako klikane wyjeżdżalne menu? co z mobilkami?

# obsługa sass less?
