import feedparser

sanat = ""

# Yle
yle = feedparser.parse("https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss")
for feed in yle['entries']:
    sanat += feed['title']+" "

#HS
hs = feedparser.parse("https://www.hs.fi/rss/teasers/etusivu.xml")
for feed in hs['entries']:
    sanat += feed['title']+" "

# IS
iss = feedparser.parse("https://www.is.fi/rss/tuoreimmat.xml")
for feed in iss['entries']:
    sanat += feed['title']+" "

# IL
il = feedparser.parse("https://www.iltalehti.fi/rss/uutiset.xml")
for feed in il['entries']:
    sanat += feed['title']+" "

# Kauppalehti
kl = feedparser.parse("https://feeds.kauppalehti.fi/rss/main")
for feed in kl['entries']:
	sanat += feed['title']+" "

# some cleanup
poista = ['0','1','2','3','4','5','6','7','8','9','[',']','(',')',',','\'','.','!','?','—','–','|','\"','„','“','‟','”','”','”','\xad']
t=""
for i in sanat:
 if i not in poista:
  t+=i

# transform to list, and then to set
sanat = t.lower().split()
uniikit_sanat = set(sanat)

# opens the existing corpus as string, transform it into a wordlist, and then into a set
f = open('corpus.txt', encoding='utf-8' ).read()
f = f.split()
f = set(f)

# create a new union of sets (removes duplicates between them)
g = uniikit_sanat.union(f)
g = sorted(g)

# replaces the contents of the corpus.txt with the new set
g = ' '.join(g) 
wr = open('corpus.txt', 'w', encoding='utf-8')
wr.write(g)
