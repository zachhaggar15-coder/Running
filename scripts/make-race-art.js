const fs=require('fs');
const path=require('path');
const races=[...require('../app/data/races.json'),...require('../app/data/race-expansion.json')];
const out=path.resolve(__dirname,'../app/assets/races');
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const hash=s=>[...s].reduce((h,c)=>(Math.imul(h,31)+c.charCodeAt(0))>>>0,2166136261);
const palette=[['#102d31','#236369','#d2a174'],['#1a2d45','#446179','#df955f'],['#192f29','#466a56','#e5a76d'],['#252c3e','#66617b','#d6a56d'],['#273b34','#617967','#dda17f']];
for(const r of races){
  if(!r.slug||r.image?.src?.endsWith('.jpg'))continue;
  const target=path.join(out,r.slug+'.svg');if(fs.existsSync(target))continue;
  const seed=hash(r.slug),[dark,mid,light]=palette[seed%palette.length];
  const peaks=Array.from({length:9},(_,i)=>`${i*220-90},${295+((seed>>>((i%4)*7))%165)}`).join(' ');
  const lower=Array.from({length:9},(_,i)=>`${i*220-90},${390+((seed>>>((i%4)*5))%145)}`).join(' ');
  const name=esc(r.name),place=esc(r.place),distance=esc(r.distance);
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="728" viewBox="0 0 1600 728" role="img" aria-label="Illustrated landscape for ${name}"><defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="${dark}"/><stop offset="1" stop-color="${mid}"/></linearGradient><linearGradient id="land" x2="0" y2="1"><stop stop-color="${mid}"/><stop offset="1" stop-color="${dark}"/></linearGradient></defs><rect width="1600" height="728" fill="url(#sky)"/><circle cx="${1080+(seed%330)}" cy="${105+(seed%120)}" r="112" fill="${light}" opacity=".55"/><path d="M0 455 L${peaks} L1600 520 L1600 728 H0Z" fill="${light}" opacity=".3"/><path d="M0 560 L${lower} L1600 560 L1600 728 H0Z" fill="url(#land)"/><path d="M-100 685 Q400 580 850 720 T1700 630" fill="none" stroke="${light}" stroke-width="42" opacity=".4"/><path d="M-100 685 Q400 580 850 720 T1700 630" fill="none" stroke="#f2e7ca" stroke-width="4" opacity=".65" stroke-dasharray="25 18"/><rect x="58" y="54" width="336" height="47" rx="4" fill="#07140f" opacity=".72"/><text x="78" y="86" fill="#fff" font-family="Arial,sans-serif" font-size="26" font-weight="700" letter-spacing="4">RACE FIELDNOTES</text><text x="72" y="510" fill="#fff" font-family="Arial,sans-serif" font-size="64" font-weight="700" textLength="1450" lengthAdjust="spacingAndGlyphs">${name}</text><text x="76" y="562" fill="#ffe3c5" font-family="Arial,sans-serif" font-size="29">${place} · ${distance}</text><text x="78" y="614" fill="#fff" font-family="Arial,sans-serif" font-size="20" opacity=".82">Original illustrative artwork · not a course photograph</text></svg>`;
  fs.writeFileSync(target,svg);
}
