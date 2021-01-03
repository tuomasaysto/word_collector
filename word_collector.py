# skripti, joka kerää oman korpuksen suomea.
# 1. lukee uutisten rss-fiidien otsikot sanalistaksi (DONE)
# 2. kerää uniikit sanat setiksi (DONE)
# 3. avaa vanhemman sanalistan (txt) ja vertaa löytyykö uusia sanoja siitä. Ellei, lisää ne sinne.
# 4. Skripti pyörii päivittäin klo 12 cron-työnä

import feedparser



sanat = ""

# Ylen otsikot
yle = feedparser.parse("https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss")
for feed in yle['entries']:
    sanat += feed['title']+" "

#HS:n otsikot
hs = feedparser.parse("https://www.hs.fi/rss/teasers/etusivu.xml")
for feed in hs['entries']:
    sanat += feed['title']+" "

# IS:n otsikot
iss = feedparser.parse("https://www.is.fi/rss/tuoreimmat.xml")
for feed in iss['entries']:
    sanat += feed['title']+" "


# IL:n otsikot
il = feedparser.parse("https://www.iltalehti.fi/rss/uutiset.xml")
for feed in il['entries']:
    sanat += feed['title']+" "

#kauppalehden otsikot
kl = feedparser.parse("https://feeds.kauppalehti.fi/rss/main")
for feed in kl['entries']:
	sanat += feed['title']+" "


# siivousta

poista = ['0','1','2','3','4','5','6','7','8','9','[',']','(',')',',','\'','.','!','?','—','–','|','\"','„','“','‟','”','”','”','\xad']

t=""
for i in sanat:
 if i not in poista:
  t+=i


# sanat listaksi ja isot kirjaimet pois
sanat = t.lower().split()


#lista setiksi (poistaa duplikaatit)
uniikit_sanat = set(sanat)

'''
print (sorted(uniikit_sanat))
print (len(uniikit_sanat))
print (len(sanat))
'''

#avaa korpuksen stringinä f, muuntaa sen sanalistaksi, ja sen jälkeen setiksi
f = open('corpus.txt', encoding='utf-8' ).read()
f = f.split()
f = set(f)

#print (f)

# luo uuden ja vanhan setin unionin, josta duplikaatit jäävät pois
g = uniikit_sanat.union(f)
g = sorted(g)

# korvaa tekstitiedoston corpus.txt sisällön setillä g
g = ' '.join(g) 

#print (g)

wr = open('corpus.txt', 'w', encoding='utf-8')
wr.write(g)







