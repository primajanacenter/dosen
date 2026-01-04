from scholarly import scholarly
import json, sys, re

url = sys.argv[1]

user_id = re.findall(r'user=([^&]+)', url)
if not user_id:
    print("Scholar ID tidak ditemukan")
    exit()

author = scholarly.search_author_id(user_id[0])
author = scholarly.fill(author, sections=['publications'])

publications = []

for pub in author['publications']:
    p = scholarly.fill(pub)
    publications.append({
        "title": p['bib'].get('title'),
        "year": p['bib'].get('year'),
        "journal": p['bib'].get('venue'),
        "citations": p.get('num_citations', 0)
    })

with open("publications.json", "w") as f:
    json.dump(publications, f, indent=2)

print("Berhasil ambil publikasi")
