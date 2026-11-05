---
title: Mysore
state: Karnataka
date: 2026-11-05            # placeholder, used to sort trips (newest first). Replace with the real trip date
summary: "The palace, the zoo, a church and the night show in one day by train from Bengaluru, plus a 3-day plan with Chamundi Hills, Tipu Sultan's palace and the museums, staying at Zostel."
month: "2026"
days_count: 3
best_season: "Oct – Mar"
cost_note: "per person, for the 1 day I did"
stay_short: "Zostel Mysore"

cover: /assets/images/mysore/cover.jpg
cover_alt: "A collage of Mysore: the Mysuru Junction sign, the zoo letters, a tiger, a vintage truck and the two of us, next to the palace lit up at night"
cover_portrait: true          # show the cover and the card whole, not cropped
card: /assets/images/mysore/card.jpg
banner: ""
gallery: []

instagram: []

expenses:                   # rupees per person, for the one day I did (the sheet's shared items split in half; the souvenir magnet is left out)
  - category: Getting there
    note: "Train Bengaluru to Mysore and back, the bus, a Majestic auto and the KR Puram to Majestic cab"
    amount: 642
  - category: Local autos and parking
    note: "Autos to the zoo, from the palace to the church and to the station, plus bike parking"
    amount: 116
  - category: Entry and small fees
    note: "Zoo, palace, night show, bag and shoe keeping, washroom"
    amount: 391
  - category: Food
    note: "Dosa and coffee, lunch, ice cream, Limca, masala puri, coffee, tea and dinner at the station"
    amount: 430

things_to_do:
  - "Day 1: zoo, Mysore Palace, St. Philomena's Church, then the palace night show"
  - "Day 2: Chamundi Hills (temple and Nandi), then the Sand Museum"
  - "Day 3: Tipu Sultan's Summer Palace, Payana Vintage Museum and the Rail Museum"
  - "Buy the palace ticket before you queue for the night show"
  - "Stay at Zostel Mysore if you want a hostel base for 3 days"
things_to_skip:
  - "Trying to see everything in one day: the palace night show forces a late finish"
  - "Reaching the palace after 5:30 PM: day entry closes then"
  - "Buying a magnet at the first stall: compare shops (I paid ₹100)"

eat:
  - name: Dosa and coffee
    note: "Our breakfast on the way in, ₹180 for two"
  - name: Masala puri
    note: "A snack near the church, ₹70 for two"
  - name: Railway station dinner
    note: "₹190 for two before the night train"
  - name: Street food outside the palace
    note: "Cut fruit and snacks, cheap and quick"

details:
  - label: Getting there
    value: "Train from Bengaluru to Mysore, ₹302 each way"
  - label: Where to stay
    value: "Zostel Mysore (I did not stay on my one-day trip, so no price here)"
  - label: Palace
    value: "10 AM to 5:30 PM, ₹120 per person"
  - label: Night show
    value: "7 to 8 PM, ₹120 on the ticket"
  - label: Zoo
    value: "8:30 AM to 5:30 PM, ₹100 per person"
  - label: Budget level
    value: "Backpacker"

# Coordinates are approximate, picked by eye from the map. Check them in Google Maps before you rely on them.
# "route" opens in Google Maps with every stop in order.
days:
  - title: "Zoo, palace, church and the night show"
    route: "https://www.google.com/maps/dir/?api=1&origin=12.3150,76.6420&destination=12.3150,76.6420&waypoints=12.3010,76.6520%7C12.3052,76.6552%7C12.3144,76.6517&travelmode=driving"
    stops:
      - name: Mysuru railway station
        type: train
        note: "Arrive from Bengaluru, then the bus and an auto to the zoo (₹50)"
        lat: 12.3150
        lng: 76.6420
      - name: Mysore Zoo
        type: town
        note: "8:30 AM to 5:30 PM, ₹100 per person"
        lat: 12.3010
        lng: 76.6520
      - name: Mysore Palace
        type: palace
        note: "10 AM to 5:30 PM, ₹120 per person. Lunch first, then the palace"
        lat: 12.3052
        lng: 76.6552
      - name: St. Philomena's Church
        type: temple
        note: "6 AM to 8 PM, free. Auto from the palace (₹70)"
        lat: 12.3144
        lng: 76.6517
      - name: Palace night show
        type: palace
        note: "7 to 8 PM. We went back for the Light and Sound show"
        lat: 12.3052
        lng: 76.6552
  - title: "Chamundi Hills and the Sand Museum (plan)"
    route: "https://www.google.com/maps/dir/?api=1&origin=12.3100,76.6500&destination=12.3100,76.6500&waypoints=12.2724,76.6700%7C12.2740,76.6740%7C12.2860,76.6770&travelmode=driving"
    stops:
      - name: Zostel Mysore
        type: home
        note: "Base for the stay. Check the exact location in Google Maps"
        lat: 12.3100
        lng: 76.6500
      - name: Chamundi Hills
        type: hill
        note: "The hill above the city, with a view over Mysore"
        lat: 12.2724
        lng: 76.6700
      - name: Chamundeshwari Temple
        type: temple
        note: "The temple at the top"
        lat: 12.2725
        lng: 76.6700
      - name: Nandi statue
        type: temple
        note: "The huge Nandi bull on the way down the hill"
        lat: 12.2740
        lng: 76.6740
      - name: Mysore Sand Sculpture Museum
        type: town
        note: "Sculptures made of sand. Check the timings and entry fee"
        lat: 12.2860
        lng: 76.6770
  - title: "Tipu Sultan's palace, vintage cars and the Rail Museum (plan)"
    route: "https://www.google.com/maps/dir/?api=1&origin=12.3100,76.6500&destination=12.3150,76.6420&waypoints=12.4150,76.6970%7C12.4390,76.6770%7C12.3090,76.6440&travelmode=driving"
    stops:
      - name: Tipu Sultan's Summer Palace
        type: palace
        note: "At Srirangapatna, about 15 km from Mysore. Check the timings"
        lat: 12.4150
        lng: 76.6970
      - name: Payana Vintage Museum
        type: town
        note: "A vintage car museum near Srirangapatna, on the Bengaluru–Mysore expressway"
        lat: 12.4390
        lng: 76.6770
      - name: Rail Museum, Mysuru
        type: train
        note: "Old locomotives and coaches. Check the timings"
        lat: 12.3090
        lng: 76.6440
      - name: Mysuru railway station
        type: train
        note: "Train back to Bengaluru"
        lat: 12.3150
        lng: 76.6420
credits:
  - title: "Chamundi From Karanji"
    author: "Timothy A. Go"
    license: "CC BY-SA 4.0"
    license_url: https://creativecommons.org/licenses/by-sa/4.0
    source: https://commons.wikimedia.org/wiki/File:Chamundi_From_Karanji_Mysore_Nov23_A7C_08173.jpg
  - title: "Colossal Bull at the Chamundeswari Temple"
    author: "RaghavendraDorai"
    license: "CC BY-SA 4.0"
    license_url: https://creativecommons.org/licenses/by-sa/4.0
    source: https://commons.wikimedia.org/wiki/File:Colossal_Bull_at_the_Chamundeswari_Temple,_Mysuru,_Karnataka,_India_(2018).jpg
  - title: "Tipu Sultan’s Summer Palace, Srirangapatna"
    author: "Ananthmohanram18"
    license: "CC BY-SA 4.0"
    license_url: https://creativecommons.org/licenses/by-sa/4.0
    source: https://commons.wikimedia.org/wiki/File:Tipu_Sultan%E2%80%99s_Summer_Palace,_Srirangapatna,_Karnataka.jpg
  - title: "Payana Museum, Karnataka (2025) 187"
    author: "Gpkp"
    license: "CC BY-SA 4.0"
    license_url: https://creativecommons.org/licenses/by-sa/4.0
    source: https://commons.wikimedia.org/wiki/File:Payana_Museum,_Karnataka_(2025)_187.jpg
---

Mysore is Karnataka's palace city, and it is close enough to Bengaluru to do in a day. I did exactly that: train in, zoo, palace, a church, and the palace night show before the train home. This page has what I spent on that day, plus a 3-day plan for doing it properly with Chamundi Hills, Tipu Sultan's palace and the museums, staying at Zostel Mysore.

<div class="callout"><strong>The short version.</strong> Take the train from Bengaluru, start at the zoo, give the palace the afternoon and stay for the night show. If you have 3 days, add Chamundi Hills, Tipu Sultan's Summer Palace and the museums, and stay at Zostel Mysore.</div>

### Getting there

I took the train from Bengaluru to Mysore (₹302 each) and the same back. Between the station and the city we used the bus (₹380 for two), plus autos. On the way home, the KR Puram to Majestic cab cost ₹280, so it is worth planning the last stretch before you leave.

### Getting around

Autos did most of the work: ₹50 from the bus stop to the zoo, ₹70 from the palace to the church and ₹52 to the station. Everything on Day 1 is inside the city, so you do not need your own vehicle.

### Where to stay

For the 3-day version, stay at **Zostel Mysore**. I did not stay there on my one-day trip, so I have no price or photos of my own and nothing here is first-hand. Check the current rate and the location in the Zostel app, and book ahead if you are going on a weekend or in the Dasara season.

### The days

**Day 1: zoo, palace, church and the night show.** This is the day I actually did. Breakfast was dosa and coffee (₹180 for two), then an auto from the bus stop to the zoo (₹50). The zoo is open 8:30 AM to 5:30 PM and costs ₹100 per person, plus ₹30 for a bag ticket. After an ice cream and lunch (₹260 for two) we went to the palace (10 AM to 5:30 PM, ₹120 per person, ₹10 for shoe keeping). An auto took us to St. Philomena's Church (free, ₹30 to keep bags and shoes), where we had coffee and masala puri. Then back to the palace for the Light and Sound show, 7 to 8 PM.

<div class="shots">
{% include shot.html file="palace.jpg" class="tall" caption="Mysore Palace, from the garden" %}
{% include shot.html file="palace-hall.jpg" class="tall" caption="The palace durbar hall" %}
{% include shot.html file="church.jpg" class="tall" caption="St. Philomena's Church" %}
{% include shot.html file="palace-lights.jpg" class="tall" caption="The palace lit up for the night show" %}
</div>

**Day 2: Chamundi Hills and the Sand Museum (plan).** Go up Chamundi Hills in the morning for the Chamundeshwari Temple and the view over the city, and stop at the huge Nandi bull on the way down. Then see the Mysore Sand Sculpture Museum. I have not done this day, so check the timings and fees before you go.

<div class="shots">
{% include shot.html file="chamundi.jpg" caption="Chamundi Hills, seen from Karanji Lake" %}
{% include shot.html file="nandi.jpg" caption="The Nandi statue" %}
</div>

**Day 3: Tipu Sultan's palace, vintage cars and the Rail Museum (plan).** Tipu Sultan's Summer Palace is at Srirangapatna, a short way out of Mysore. The Payana Vintage Museum, a car museum, is also near Srirangapatna on the Bengaluru–Mysore expressway, so the two fit one trip. Come back for the Rail Museum before the train to Bengaluru. This day is a plan too, so check the timings and fees.

<div class="shots">
{% include shot.html file="tipu.jpg" caption="Tipu Sultan's Summer Palace" %}
{% include shot.html file="car-museum.jpg" caption="A vintage car at the Payana Museum" %}
</div>

### Food

Dosa and coffee for breakfast, a simple lunch near the palace, masala puri at the church and dinner at the railway station: nothing fancy, and about ₹430 a head for the whole day. Street stalls outside the palace sell cut fruit and snacks, and the souvenir stalls are where I bought the ₹100 magnet.

<div class="shots">
{% include shot.html file="street-food.jpg" class="tall" caption="Street food outside the palace" %}
{% include shot.html file="market.jpg" class="tall" caption="Souvenir stalls near the palace" %}
</div>

### Prices and timings

<div class="table-scroll"><table class="timetable"><thead><tr><th>Time</th><th>Place</th><th>Price</th></tr></thead><tbody>
<tr><td>8:30 AM to 5:30 PM</td><td>Mysore Zoo</td><td>₹100 per person</td></tr>
<tr><td>10:00 AM to 5:30 PM</td><td>Mysore Palace</td><td>₹120 per person</td></tr>
<tr><td>7:00 to 8:00 PM</td><td>Light and Sound show, Mysore Palace</td><td>₹120 night show</td></tr>
<tr><td>6:00 AM to 8:00 PM</td><td>Church</td><td>Free</td></tr>
</tbody></table></div>

### What I'd add to this plan

<div class="callout"><strong>A few things worth adding</strong>, from reading around rather than from my own trip, so check them locally:
<ul>
<li><strong>Do the zoo first.</strong> It opens at 8:30 AM and the afternoon is hot, so the palace is better after lunch.</li>
<li><strong>Check which evenings the palace is lit up.</strong> The lights are not on every night, so confirm before you plan your evening around them.</li>
<li><strong>Chamundi Hills</strong> can be reached by road or on foot up the steps. Go early, before the temple queues build up.</li>
<li><strong>Tipu Sultan's Summer Palace</strong> is in Srirangapatna, so group it with the other Srirangapatna sights instead of making a separate trip.</li>
<li><strong>Buy tickets yourself.</strong> Entry prices are fixed, so do not pay anyone extra to get you in.</li>
<li><strong>Carry cash.</strong> Autos and small stalls may not take UPI.</li>
</ul></div>
