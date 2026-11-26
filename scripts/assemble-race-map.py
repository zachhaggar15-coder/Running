"""Assemble reviewed race map pins from organizer directions and area fallbacks.

The fallback coordinates are town/route area anchors, not asserted start lines.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'app' / 'data'
records = json.loads((root / 'races.json').read_text(encoding='utf-8'))
for path in sorted(root.glob('race-expansion*.json')):
    records += json.loads(path.read_text(encoding='utf-8'))
organizer = json.loads((root / 'organiser-locations.json').read_text(encoding='utf-8'))
draft = json.loads((root / 'race-locations-draft.json').read_text(encoding='utf-8'))

# Explicit area anchors correct ambiguous gazetteer names and cover route regions.
# Each is shown as an approximate area pin in the interface.
areas = {
 'maverick-peak-district-x-trail': (53.21338,-1.67481,'Bakewell area'),
 'race-to-the-stones': (51.535,-1.57,'The Ridgeway start area'),
 'great-north-run': (54.97328,-1.61396,'Newcastle upon Tyne area'),
 'inverness-half-marathon': (57.467,-4.237,'Inverness Bught Park area'),
 'snowdonia-trail-ultra-eryri': (53.11809,-4.12923,'Llanberis / Eryri area'),
 'beacons-way-ultra-100': (51.88,-3.44,'Bannau Brycheiniog area'),
 'norn-iron-100-half-marathon': (54.6,-6.7,'Northern Ireland route area'),
 'skyline-scotland-utmb': (56.86,-4.98,'Nevis Range area'),
 'devil-o-the-highlands-footrace': (56.735,-4.96,'West Highland Way area'),
 'chester-ultra-50': (53.279,-2.897,'Ellesmere Port area'),
 'chester-ultra-100': (53.279,-2.897,'Ellesmere Port area'),
 'ultra-scotland-50': (55.10,-4.16,"St John's Town of Dalry area"),
 'ultra-scotland-100': (55.10,-4.16,"St John's Town of Dalry area"),
 'maverick-new-forest-gravel': (50.77,-1.69,'Holmsley / New Forest area'),
 'anglesey-trail-half-10k': (53.16,-4.36,'Newborough Forest area'),
 'maverick-hampshire-trail': (51.04,-1.25,'Matterley Basin area'),
 'maverick-south-downs-trail': (50.96,-0.98,'Queen Elizabeth Country Park area'),
 'wendover-woods-50': (51.77,-0.75,'Wendover Woods area'),
 'newport-half': (51.58774,-2.99835,'Newport area'),
 'lake-district-challenge-2027': (54.32681,-2.74757,'Kendal area'),
 'cotswold-way-challenge-2027': (51.71927,-1.97145,'Cirencester area'),
 'north-yorks-challenge-2027': (54.27966,-0.40443,'Scarborough area'),
 'south-coast-challenge-2027': (50.76871,0.28453,'Eastbourne area'),
 'high-lodge-thetford-trail-runs-2027': (52.43,0.67,'High Lodge / Thetford Forest area'),
 'beyond-bristol-trail-runs-2027': (51.45523,-2.59665,'Central Bristol area'),
 'beyond-newcastle-trail-runs-2027': (54.97328,-1.61396,'Newcastle Quayside area'),
 'beyond-nottingham-trail-runs-2027': (52.9536,-1.15047,'Central Nottingham area'),
 'the-earl-s-backyard-ultra-2027': (54.86,-1.51,'Lambton Estate area'),
 'lambton-estate-summer-trail-runs-2027': (54.86,-1.51,'Lambton Estate area'),
 'the-derwent-60k-trail-ultra-2027': (54.86,-1.96,'Derwent Reservoir, County Durham area'),
 'derwent-reservoir-runs-2027': (54.86,-1.96,'Derwent Reservoir, County Durham area'),
 'draycote-water-may': (52.33,-1.32,'Draycote Water area'),
 'hundred-hills-50km': (51.6,-0.94,'Stonor Park area'),
 'north-downs-way-50': (51.21444,-0.80054,'Farnham start area'),
 'north-downs-way-100': (51.21444,-0.80054,'Farnham start area'),
 'south-downs-way-100': (51.04,-1.25,'Matterley Estate area'),
 'south-downs-way-50km': (51.04,-1.25,'Matterley Bowl area'),
 'south-downs-way-10km': (51.04,-1.25,'Matterley Estate area'),
 'south-downs-way-5km': (51.04,-1.25,'Matterley Estate area'),
 'chiltern-wonderland-50': (51.52322,-1.13342,'Goring area'),
 'autumn-100': (51.52322,-1.13342,'Goring and Streatley area'),
 'ultra-wales-50': (52.82,-3.88,'Coed-y-Brenin area'),
 'yr-wyddfa-ultra-100': (53.11809,-4.12923,'Eryri route area'),
 'yr-wyddfa-ultra-50': (53.092,-3.801,'Betws-y-Coed area'),
 'cheshire-ring-ultra-100': (53.48095,-2.23743,'Manchester route area'),
 'ultra-england-50': (54.59947,-3.13256,'Keswick area'),
 'belfast-24-hour-festival': (54.61,-5.87,'Victoria Park, Belfast area'),
 'nick-beer-llandudno-10k': (53.32498,-3.83148,'Llandudno area'),
 'anglesey-road-half-10k': (53.25075,-4.37484,'Mona Showground area'),
 'newport-10k': (51.58774,-2.99835,'Newport city centre area'),
 'barry-island-10k': (51.39979,-3.2838,'Barry Island area'),
 'cdf-10k': (51.48,-3.18,'Cardiff city centre area'),
 'mens-10k-glasgow': (55.86515,-4.25763,'Glasgow Riverside Museum area'),
 'gibside-new-year-trail-runs-2027': (54.921,-1.729,'Gibside area'),
 'gibside-evening-wild-trail-runs-2027': (54.921,-1.729,'Gibside area'),
 'harewood-house-new-year-trail-runs-2027': (53.897,-1.444,'Harewood House area'),
 'salcey-forest-new-year-trail-runs-2027': (52.15,-0.84,'Salcey Forest area'),
 'druridge-bay-beach-trail-runs-2027': (55.26,-1.58,'Druridge Bay area'),
 'rivington-wild-trail-runs-2027': (53.63,-2.56,'Rivington area'),
 'grasmere-wild-trail-runs-2027': (54.46,-3.025,'Grasmere area'),
 'bramham-park-yorkshire-trail-runs-2027': (53.88,-1.38,'Bramham Park area'),
 'clumber-park-wild-trail-runs-2027': (53.27,-1.06,'Clumber Park area'),
 'whinlatter-forest-trail-runs-2027': (54.61,-3.23,'Whinlatter Forest area'),
 'moors-valley-wild-trail-runs-2027': (50.81,-1.88,'Moors Valley area'),
 'margam-park-wild-trail-runs-2027': (51.56,-3.73,'Margam Park area'),
 'wentworth-castle-gardens-evening-trail-runs-2027': (53.52,-1.51,'Wentworth Castle Gardens area'),
 'chopwell-woods-summer-trail-runs-2027': (54.9,-1.82,'Chopwell Woods area'),
 'alice-holt-forest-wild-trail-runs-2027': (51.17,-0.83,'Alice Holt Forest area'),
 'sheffield-urban-trail-runs-2027': (53.4,-1.48,'Parkwood Springs area'),
 'slaley-hall-and-forest-trail-runs-2027': (54.92,-2.02,'Slaley Hall area'),
}

out = {}
for race in records:
    slug = race['slug']
    if slug in organizer:
        item = organizer[slug]
        out[slug] = {'lat':item['lat'],'lon':item['lon'],'label':race['place'], 'precision':'organiser location','source':item['source']}
    elif slug in areas:
        lat, lon, label = areas[slug]
        out[slug] = {'lat':lat,'lon':lon,'label':label,'precision':'approximate area','source':'Editorial area anchor'}
    elif slug in draft:
        item = draft[slug]
        out[slug] = {'lat':item['lat'],'lon':item['lon'],'label':item['label']+' area','precision':'approximate area','source':'GeoNames GB gazetteer'}
    else:
        raise SystemExit(f'Missing map point: {slug}')
    point = out[slug]
    if not (49.8 < point['lat'] < 59 and -8.5 < point['lon'] < 2.5):
        raise SystemExit(f'Invalid GB coordinate: {slug} {point}')
if len(out) != len(records) or len(out) != len(set(out)):
    raise SystemExit('Map coverage mismatch')
(root / 'race-locations.json').write_bytes((json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(f'Wrote {len(out)} race locations: {len(organizer)} organiser points and {len(out)-len(organizer)} area pins')
