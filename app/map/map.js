(async()=>{
  const count=document.getElementById('count');
  try{
    const response=await fetch('/map/races.json');if(!response.ok)throw Error('Race data could not be loaded');
    const races=await response.json();
    const map=L.map('map',{scrollWheelZoom:false}).setView([54.2,-3.3],6);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    const cluster=L.markerClusterGroup({spiderfyOnMaxZoom:true,showCoverageOnHover:false,maxClusterRadius:45});map.addLayer(cluster);
    const search=document.getElementById('search'),nation=document.getElementById('nation'),type=document.getElementById('type'),results=document.getElementById('results');
    const markerBySlug=new Map();
    for(const race of races){
      const marker=L.marker([race.lat,race.lon]);const wrap=document.createElement('div');
      const title=document.createElement('strong');title.textContent=race.name;wrap.append(title,document.createElement('br'));
      const detail=document.createElement('span');detail.textContent=`${race.date} · ${race.place}`;wrap.append(detail,document.createElement('br'));
      const precision=document.createElement('small');precision.textContent=race.precision==='organiser location'?'Organizer directions location; check final start instructions':`Approximate pin: ${race.label}`;wrap.append(precision,document.createElement('br'));
      const link=document.createElement('a');link.href=`/races/${encodeURIComponent(race.slug)}/`;link.textContent='Open race profile →';wrap.append(link);
      marker.bindPopup(wrap);markerBySlug.set(race.slug,marker);
    }
    function render(){
      const term=search.value.trim().toLocaleLowerCase('en-GB');const matched=races.filter(r=>(!term||`${r.name} ${r.place} ${r.date}`.toLocaleLowerCase('en-GB').includes(term))&&(!nation.value||r.nation===nation.value)&&(!type.value||r.type===type.value));
      cluster.clearLayers();cluster.addLayers(matched.map(r=>markerBySlug.get(r.slug)));
      count.textContent=`Showing ${matched.length} of ${races.length} races. Select a pin to open its race profile.`;
      results.replaceChildren();const ul=document.createElement('ul');for(const race of matched.slice(0,80)){const li=document.createElement('li'),a=document.createElement('a');a.href=`/races/${encodeURIComponent(race.slug)}/`;a.textContent=`${race.name} · ${race.date}`;li.append(a);ul.append(li)}results.append(ul);
      if(matched.length&&matched.length<races.length){const bounds=L.latLngBounds(matched.map(r=>[r.lat,r.lon]));map.fitBounds(bounds.pad(.12),{maxZoom:11});}
    }
    for(const input of [search,nation,type])input.addEventListener(input===search?'input':'change',render);
    const selected=new URLSearchParams(location.search).get('race');
    if(selected&&markerBySlug.has(selected)){
      const race=races.find(r=>r.slug===selected);search.value=race.name;render();map.setView([race.lat,race.lon],12);cluster.zoomToShowLayer(markerBySlug.get(selected),()=>markerBySlug.get(selected).openPopup());
    }else render();
  }catch(error){count.textContent='The map is unavailable right now. Browse the linked race directory below.';const a=document.createElement('a');a.href='/races/';a.textContent='Browse all races';document.getElementById('results').append(a);}
})();
