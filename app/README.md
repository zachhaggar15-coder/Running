# Race Fieldnotes site

The static site contains 400 source-linked UK race and run-challenge profiles, a searchable directory, an interactive map with 400 clickable pins, six decision guides and a sitemap. Race records live in `data/races.json` and the `data/race-expansion*.json` files; individually reviewed updates to older records live in `data/verified-updates.json`. `node scripts/rebuild-profiles.js` regenerates the profile HTML, catalogue data, directory, map and sitemap. `python scripts/assemble-race-map.py` rebuilds the map locations from the reviewed organizer coordinate file, gazetteer draft and explicit area anchors.

Missing race facts remain labelled as unconfirmed. Organiser pages are linked for entry and final race-day instructions. The illustrations are original editorial artwork, not official course photographs.

Map pins are marked as organizer directions locations or approximate areas; neither is a substitute for the final start-line instructions. Map tiles are from OpenStreetMap and approximate gazetteer areas are credited to GeoNames GB.
