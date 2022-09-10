import random
import requests

def bring_verse(verse):
    url = 'http://api.alquran.cloud/ayah/'+str(verse)+'/editions/quran-uthmani,en.pickthall'
    json_data = requests.get(url).json()
    verse_a = json_data['data'][0]['text']
    verse_en = json_data['data'][1]['text']
    sura = json_data['data'][0]['surah']['englishName']+\
           '('+str(json_data['data'][0]['surah']['number'])+'):'+\
           str(json_data['data'][0]['numberInSurah'])
    return [verse_a,verse_en,sura]

while True:
    verse = input(">>press enter for a random verse (press 'q' to quit): ")
    if verse == 'q':
        print('Thank you, come again')
        break
    
    aya = random.randint(1,6237)
    link = bring_verse(aya)
    print('----------------')
    print(link[0])
    print('\n')
    print(link[1])
    print('\n')
    print(link[2])
    print('----------------')
    

