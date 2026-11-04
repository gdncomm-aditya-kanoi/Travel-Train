---
title: Gokarna & Murudeshwar
state: Karnataka
date: 2024-01-01            # used to sort trips, newest first (approximate: only the year, 2024, is known)
summary: "Beaches and a cliff trek in Gokarna, a fort, a waterfall and caves by scooty, then the giant Shiva of Murudeshwar."
month: "2024"
days_count: 3
best_season: "Oct – May"
cost_note: "per person"
stay_short: "Zostel Gokarna"
art: coast                  # which line-art banner tools/build_assets.py draws

cover: /assets/images/gokarna-murudeshwar/cover.jpg
cover_alt: "Two of us on a Gokarna beach"
card: /assets/images/gokarna-murudeshwar/card.jpg
banner: /assets/images/gokarna-murudeshwar/banner.svg
gallery: []

map_pdf: /assets/maps/gokarna-murudeshwar-guide.pdf

instagram:
  - https://www.instagram.com/p/DeRvoWdCSMe/?img_index=1
  - https://www.instagram.com/p/C6xsS7-SSr7/

expenses:                   # rupees per person (the trip was for 2, split in half, from the expense sheet)
  - category: Getting there
    note: "Overnight train both ways, RAC: Bengaluru to Gokarna, Murudeshwar to Bengaluru"
    amount: 905
  - category: Stay
    note: "Zostel Gokarna, 2 nights"
    amount: 2462
  - category: Food
    note: "Cafés, local breakfasts, train dinner, and chai, soda and snacks on the way"
    amount: 1635
  - category: Scooty and petrol
    note: "2 days of hire (about ₹350 a day) and fuel"
    amount: 615
  - category: Buses, autos and metro
    note: "Gokarna to Honnavar to Murudeshwar, beach autos, Bengaluru buses and metro"
    amount: 357
  - category: Entry and fees
    note: "Yana parking and caves, temple cave, gopuram lift, shoe keeping, baggage counter"
    amount: 90

things_to_do:
  - "Do the beach circuit on Day 1: Belekan, Paradise, Half Moon, Om, Kudle (8–11 km, about 6 hours)"
  - "Hire a scooty for Day 2: the fort, falls and caves are far apart"
  - "Take the Harlur Road route to reach Yana Caves"
  - "Stock up on water and snacks at Paradise Beach before the hard stretch"
  - "Leave your bag in the Murudeshwar temple clock room or baggage counter if you go back the same day"
  - "Go up the gopuram in the lift (₹20) and see the cave under the statue"
things_to_skip:
  - "Starting the trek late: it takes about 6 hours and gets tough after Paradise"
  - "Going without a scooty: the Day 2 spots are spread out"
  - "Hiring a bike without asking the price first"
  - "Relying on UPI or cards: the internet is poor, so carry cash"
  - "Paying café prices for every meal: local South Indian shops are cheap and good for breakfast"

eat:
  - name: Dolphin Bay Cafe
    note: "Breakfast, cheap, near the cliff · 8 AM–10 PM"
    map: https://maps.app.goo.gl/6CawAekd6i2dPmdMA
  - name: Shankar Cafe
    note: "Cheap, on the beach · 9 AM–9 PM"
    map: https://maps.app.goo.gl/9P9WUkxrujbRk8GQ7
  - name: Sunset Cafe
    note: "Mid-range dinner · 6:30–10:30 PM"
    map: https://maps.app.goo.gl/vMGEAySNV5rLCt9Q7
  - name: Cafe De Mulgudi
    note: "Mid-range dinner, omelette breakfast · 8 AM–10 PM"
    map: https://maps.app.goo.gl/4uh7DzX1D3LC3kfo8
  - name: Mantra Cafe
    note: "Pricey, good ambience, inside Zostel · 9 AM–10 PM"
    map: https://maps.app.goo.gl/9X5E86XMHTmGAmv67
  - name: Namaste Cafe
    note: "Worth a try in Gokarna"

details:
  - label: Getting to Gokarna
    value: "Bengaluru 480 km by road, Karwar 60 km"
  - label: Nearest station
    value: "Gokarna Road, then a ₹17 bus to town (Ankola 20 km, Kumta 32 km)"
  - label: Nearest airport
    value: "Dabolim, Goa (150 km) or Hubballi (168 km)"
  - label: Murudeshwar
    value: "Own station, 16 km from Bhatkal. Best Oct–May"
  - label: Where I stayed
    value: "Zostel Gokarna"
  - label: Scooty hire
    value: "About ₹350 a day"
  - label: Budget level
    value: "Backpacker"

# Coordinates are from OpenStreetMap. Belekan Beach, Murudeshwar Temple and the Zostel are approximate.
# "route" opens in Google Maps with every stop in order.
days:
  - title: The beach trek, Belekan to Kudle
    route: "https://www.google.com/maps/dir/?api=1&origin=14.5165,74.3445&destination=14.5284,74.3158&waypoints=14.5181,74.3376%7C14.5180,74.3309%7C14.5191,74.3254&travelmode=walking"
    stops:
      - name: Belekan Beach
        type: beach
        note: "Start after breakfast"
        lat: 14.5165
        lng: 74.3445
      - name: Paradise Beach
        type: beach
        note: "Shops here: stock up on water"
        lat: 14.5181
        lng: 74.3376
      - name: Half Moon Beach
        type: beach
        lat: 14.518
        lng: 74.3309
      - name: Om Beach
        type: beach
        lat: 14.5191
        lng: 74.3254
      - name: Kudle Beach
        type: beach
        note: "Finish by evening"
        lat: 14.5284
        lng: 74.3158
      - name: Zostel Gokarna
        type: home
        note: "Auto back to your stay"
        lat: 14.5399
        lng: 74.3156
        return: true
  - title: Fort, waterfall and caves by scooty
    route: "https://www.google.com/maps/dir/?api=1&origin=14.5399,74.3156&destination=14.5399,74.3156&waypoints=14.4891,74.4175%7C14.5984,74.5514%7C14.5896,74.5670&travelmode=two-wheeler"
    stops:
      - name: Zostel Gokarna
        type: home
        note: "Start. Pick up the scooty"
        lat: 14.5399
        lng: 74.3156
      - name: Mirjan Fort
        type: fort
        lat: 14.4891
        lng: 74.4175
      - name: Vibhuti Falls
        type: waterfall
        lat: 14.5984
        lng: 74.5514
      - name: Yana Caves
        type: cave
        note: "Take the Harlur Road route"
        lat: 14.5896
        lng: 74.567
      - name: Zostel Gokarna
        type: home
        note: "Back for the night"
        lat: 14.5399
        lng: 74.3156
        return: true
  - title: Bus to Murudeshwar and the night train home
    route: "https://www.google.com/maps/dir/?api=1&origin=14.5440,74.3184&destination=14.1008,74.5054&waypoints=14.2795,74.4438%7C14.0942,74.4855&travelmode=driving"
    stops:
      - name: Gokarna bus stand
        type: bus
        note: "Bus to Honnavar, ₹74"
        lat: 14.544
        lng: 74.3184
      - name: Honnavar bus stand
        type: bus
        note: "Bus to Murudeshwar, ₹30"
        lat: 14.2795
        lng: 74.4438
      - name: Murudeshwar Temple
        type: temple
        note: "Shiva statue, gopuram lift and cave"
        lat: 14.0942
        lng: 74.4855
      - name: Murudeshwar station
        type: train
        note: "Overnight train to Bengaluru"
        lat: 14.1008
        lng: 74.5054
---

Gokarna is a pilgrim town with some of Karnataka's best beaches a short walk (or scooty ride) away, and Murudeshwar is a day trip up the coast to one of the tallest Shiva statues in the world. I did both in 3 days with a friend, using two nights in Gokarna and one long day in Murudeshwar. I found the information scattered all over the place, so I put it here.

<div class="callout"><strong>The short version.</strong> Overnight train from Bengaluru, two nights at Zostel Gokarna, the beach trek on Day 1, a scooty for the fort, falls and caves on Day 2, and a bus to Murudeshwar on Day 3 before the night train home.</div>

<div class="shots">
{% include shot.html file="slide-guide.jpg" class="slide" caption="The Gokarna guide" %}
{% include shot.html file="slide-plan.jpg" class="slide" caption="The overall plan" %}
</div>

### Getting there

I took the overnight train from Bengaluru to Gokarna. Both ways cost me about ₹900 (RAC tickets, so book early or check the chart). Bengaluru is about 480 km by road. The nearest station to Gokarna is Gokarna Road, and from there I took a ₹17 bus into town. I came back on the night train from Murudeshwar.

### Where to stay

Zostel Gokarna. Honestly one of the prettiest Zostels I have stayed at, and one of the cheapest options around. You get the beach and the sea from the window, a pool table and a lovely common area. Mantra Cafe is inside it, but it is the pricey one.

### Getting around

Rent a scooty. I paid about ₹350 a day, and it made Day 2 possible because the spots are so spread out. A beach auto from Belekan to Om Beach cost ₹240 for two. Bike rentals I came across, with their maps, are in the box below.

<details class="ref">
<summary>Bike rentals in Gokarna</summary>
<div class="table-scroll"><table class="timetable"><thead><tr><th>Name</th><th>Notes</th><th>Map</th></tr></thead><tbody>
<tr><td>We Gokarna Bike Rentals</td><td>Top pick</td><td><a href="https://maps.app.goo.gl/Nzht5y6oxRrKWKUf8" target="_blank" rel="noopener">Open</a></td></tr>
<tr><td>Maahasati Bike Rental</td><td>Cheap going by reviews; check the price</td><td><a href="https://maps.app.goo.gl/pwJpsHiJxXD91iPWA" target="_blank" rel="noopener">Open</a></td></tr>
<tr><td>We Gokarna 2</td><td>Top pick; check the price</td><td><a href="https://maps.app.goo.gl/z32x2kz1McS8D2Dr9" target="_blank" rel="noopener">Open</a></td></tr>
<tr><td>Sara Bike Rent</td><td>Second choice</td><td><a href="https://maps.app.goo.gl/58GaKj21Gh1Sd9cS6" target="_blank" rel="noopener">Open</a></td></tr>
<tr><td>Rental Bikes Gokarna, Ibbani</td><td>Second choice</td><td><a href="https://maps.app.goo.gl/moJ4MtAnpSFBaHnw5" target="_blank" rel="noopener">Open</a></td></tr>
</tbody></table></div>
</details>

<div class="shots">
{% include shot.html file="slide-travel.jpg" class="slide" caption="How I got around" %}
{% include shot.html file="slide-stay.jpg" class="slide" caption="Zostel Gokarna" %}
</div>

### Day 1: the beach trek

Start in the morning, after breakfast, from Belekan Beach. The walk to Paradise Beach is short, and Paradise has plenty of shops, so stock up on water and snacks there. After Paradise the trek gets tough, through hills and small patches of jungle. You walk through Half Moon Beach and Om Beach and finish at Kudle Beach by evening, then take an auto back to your stay.

- **Route:** Belekan, Paradise, Half Moon, Om, Kudle
- **Distance:** 8 to 11 km, about 6 hours

<div class="shots">
{% include shot.html file="slide-trek.jpg" class="slide" caption="Day 1: the beach trek" %}
{% include shot.html file="slide-places.jpg" class="slide" caption="Day 2: fort, falls and caves" %}
</div>

### Day 2: fort, waterfall and caves

This is where the scooty pays off. Go to Mirjan Fort, then Vibhuti Falls, then Yana Caves, and take the Harlur Road route to reach Yana. Parking at Yana was ₹20 and the cave ticket ₹20.

### Day 3: Murudeshwar

I took a local bus from Gokarna to Honnavar (₹74) and another to Murudeshwar (₹30). You can keep your luggage in the temple clock room or the baggage counter (₹40), which is very handy if you are heading back the same day. Murudeshwar is a temple town, famous for the giant Shiva statue, the gopuram and the beach. A lift takes you up the gopuram for ₹20, and there is a cave (₹20) and a shoe-keeping counter at the temple. I took an auto to the railway station (₹25) for the night train.

<div class="shots">
{% include shot.html file="slide-murudeshwar.jpg" class="slide" caption="Day 3 at Murudeshwar" %}
{% include shot.html file="gopuram-night.jpg" class="slide" caption="The Murudeshwar gopuram at night" %}
</div>

### The beaches in a line each

- **Om Beach:** two crescents joined in the shape of an Om, great at sunset.
- **Kudle Beach:** the popular one, with greenery, volleyball and backpackers.
- **Half Moon Beach:** reached by the coastal hike or a boat from Om Beach, with a small patch of clean sand.
- **Paradise Beach:** also called Full Moon Beach, with no road. Walk 20 minutes from Half Moon or take a boat, and about 70% of it is rocks.

### Food

For breakfast I mostly ate at random local South Indian shops. Cheap, tasty and fun to explore. For the cafés worth trying, see the list on the right. Dolphin Bay is a good cheap breakfast, Shankar Cafe is cheap on the beach, and Mantra is the one for ambience, at a price.

<div class="shots">
{% include shot.html file="slide-cafes.jpg" class="slide" caption="Cafés to try" %}
</div>

### What I'd add to this plan

<div class="callout"><strong>A few things worth adding</strong>, from reading around rather than from my own trip, so check them locally:
<ul>
<li><strong>Avoid the trek in the monsoon.</strong> The trail gets slippery and the sea is rough, and many beach shacks close for the season.</li>
<li><strong>Wear proper shoes and start early.</strong> The stretch after Paradise is rocky, and flip-flops are a bad idea. Carry at least 1.5 litres of water.</li>
<li><strong>There is a boat option.</strong> Boats run from Om Beach to Half Moon and Paradise, which helps if your legs give up.</li>
<li><strong>Be careful in the water.</strong> Currents on these beaches can be strong, so swim only where others are swimming.</li>
<li><strong>See the main temple.</strong> The Mahabaleshwar Temple in Gokarna town is the reason for the pilgrim crowds. Temples often have a dress code, so check at the gate.</li>
<li><strong>Netrani Island.</strong> Boat and diving trips run from Murudeshwar in the dry season, if you can add a day.</li>
<li><strong>RAC train tickets</strong> mean you share a berth until someone cancels, so check the chart before you travel.</li>
<li><strong>Carry cash.</strong> The internet is poor in both Murudeshwar and Gokarna.</li>
</ul></div>
