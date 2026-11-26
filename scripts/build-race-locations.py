"""Build a static, reviewable map index using the GeoNames GB gazetteer.

The map is deliberately an area finder: venue-level matches are marked as
approximate, while town matches say so explicitly. No visitor geocoding runs.
"""
import json
import pathlib
import re
import sys
import unicodedata
import zipfile

root=pathlib.Path(__file__).resolve().parents[1]
zipped=pathlib.Path(sys.argv[1])
data=root/'app/data'
records=json.loads((data/'races.json').read_text(encoding='utf-8'))
for p in data.glob('race-expansion*.json'):
    records.extend(json.loads(p.read_text(encoding='utf-8')))

def norm(text):
    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().lower()
    text=text.replace('&',' and ')
    return re.sub(r'[^a-z0-9]+',' ',text).strip()

index={}
with zipfile.ZipFile(zipped) as archive:
    for line in archive.read('GB.txt').decode('utf-8').splitlines():
        row=line.split('\t')
        if len(row)<15:continue
        name=row[1]; feature=row[6]; code=row[7]
        if feature not in 'PLSHV':continue
        entry=(float(row[4]),float(row[5]),name,feature,code,int(row[14] or 0))
        for key in {norm(name),norm(row[2])}:
            if key:index.setdefault(key,[]).append(entry)

def parts(place):
    place=re.sub(r'\b(?:to|towards)\b',' , ',place,flags=re.I)
    pieces=[p.strip() for p in place.split(',')]
    out=[]
    for p in pieces:
        p=re.sub(r'\b(?:England|Scotland|Wales|Northern Ireland|UK)\b','',p,flags=re.I).strip()
        if p:out.append(p)
    return out

def choose(candidates,point,all_parts):
    # Prefer park/venue/settlement over bus stops and incidental landmarks.
    rank={'PRK':7,'EST':6,'STDM':5,'PPLA':5,'PPLA2':5,'PPLA3':5,'PPL':4,'PPLX':3,'MTRO':0}
    nearby=[]
    for other in all_parts:
        if norm(other)==norm(point):continue
        nearby.extend(index.get(norm(other),[]))
    anchor=max(nearby,key=lambda e:e[5],default=None)
    def score(e):
        proximity=0
        if anchor:
            d=(e[0]-anchor[0])**2+(e[1]-anchor[1])**2
            proximity=max(-20,4-20*d)
        return rank.get(e[4],1)+min(e[5]/100000,5)+proximity
    return max(candidates,key=score)

locations={};unmatched=[]
for r in records:
    components=parts(r['place'])
    found=None
    for j,part in enumerate(components):
        options=index.get(norm(part),[])
        if options:
            entry=choose(options,part,components)
            found=(entry,j,part)
            break
    if not found:
        unmatched.append((r['slug'],r['place']))
        continue
    (lat,lon,name,feature,code,population),j,part=found
    locations[r['slug']]={'lat':round(lat,5),'lon':round(lon,5),'label':name,'precision':'venue' if j==0 and feature in ('S','L','V') else 'area','source':'GeoNames GB gazetteer'}

out=data/'race-locations-draft.json'
out.write_text(json.dumps(locations,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('matched',len(locations),'unmatched',len(unmatched),'unique unmatched',len(set(p for _,p in unmatched)))
for slug,place in unmatched:print(slug,'|',place)
