---
title: Wayanad
state: Kerala
date: 2024-06-10            # used to sort trips, newest first (month from the photo dates, June 2024)
summary: "A monsoon weekend in the Malabar hills: zip line, Banasura Dam, a glass bridge, Edakkal Caves and tea-estate rides on a rented bike."
month: "June 2024"
days_count: 3
best_season: "Oct – May"
cost_note: "per person"
stay_short: "Zostel Plus Wayanad"

cover: /assets/images/wayanad/cover.jpg
cover_alt: "A cold beer on a wooden rail above the misty Wayanad hills"
card: /assets/images/wayanad/card.jpg
banner: ""
gallery: []

map_pdf: /assets/maps/wayanad-tourist-map.pdf

instagram:
  - https://www.instagram.com/p/DR8usViCXVL/?img_index=1
  - https://www.instagram.com/p/DCqb46bJlWL/
  - https://www.instagram.com/p/C8LvnUSywYf/?img_index=1

expenses:                   # rupees per person (the trip was for 2; shared items split in half, personal buys left out)
  - category: Getting there
    note: "Sleeper bus Bengaluru to Wayanad, train Bengaluru to Calicut and back (the up ticket was refunded and rebooked), KSRTC bus Wayanad to Calicut, auto, metro and the bus home"
    amount: 1356
  - category: Stay
    note: "Zostel Plus Wayanad, 2 nights"
    amount: 1958
  - category: Bike and petrol
    note: "Royal Brothers rental and fuel for the loop"
    amount: 1093
  - category: Food
    note: "Breakfasts, three restaurant meals, a train-station dinner, and chai and coffee along the way"
    amount: 1091
  - category: Entry and activities
    note: "Zip line, Banasura Dam, En Ooru, 900 Kandi glass bridge and jeep, Edakkal Caves, parking"
    amount: 1025
  - category: Souvenirs and extras
    note: "Raincoat, fridge magnet and chocolates"
    amount: 280

things_to_do:
  - "Ride a bike through the tea estates: the roads between spots are half the trip"
  - "Book the zip line at Muddy Boots first thing on Day 1 (₹350)"
  - "Take the van up at Banasura Dam if the walk is wet (₹25 both ways)"
  - "Walk the glass bridge at 900 Kandi (₹250), and take the jeep up if you can (₹200)"
  - "Carry a raincoat: I needed one in June"
  - "Try the grape tea at Chembra"
things_to_skip:
  - "Chembra Peak trek: it was closed when I went"
  - "Riding after dark in the rain: the hill roads are slick and unlit"
  - "Trying to fit every spot in one day: they are far apart"

eat:
  - name: Chattiyum Chorum
    note: "Kalpetta, normal prices, best in the evening"
    map: https://maps.app.goo.gl/5jYTq8JoLPt9c9y67
  - name: Udupi
    note: "Kalpetta, normal prices, best in the evening"
    map: https://maps.app.goo.gl/6v2tv7vXJ75LSkMc8
  - name: Dosa Cafe
    note: "Kalpetta, normal prices, good for breakfast"
    map: https://maps.app.goo.gl/kNbnjbJpbLc4MvDW8
  - name: India Gate
    note: "Vythiri, normal prices, afternoon to evening. I had lunch here"
    map: https://maps.app.goo.gl/6v2tv7vXJ75LSkMc8
  - name: Mywo Restaurant
    note: "Vythiri, normal prices, afternoon"
    map: https://maps.app.goo.gl/66DPmJaymPCRDirX7
  - name: Lunch Box
    note: "Near Banasura, Kerala meals, afternoon"
    map: https://maps.app.goo.gl/TxiXPjVf7zH9J5wC6

details:
  - label: Getting there
    value: "Overnight sleeper bus from Bengaluru, or train to Calicut (Kozhikode) and a bus up"
  - label: Nearest station
    value: "Calicut, about 3 hours by KSRTC bus from Kalpetta (₹98 on the board, I paid ₹87)"
  - label: Where I stayed
    value: "Zostel Plus Wayanad"
  - label: Bike hire
    value: "Royal Brothers, about ₹650 a person for the trip"
  - label: Budget level
    value: "Backpacker"

# Coordinates are approximate, picked by eye from the map. Check them in Google Maps before you rely on them.
days:
  - title: Zip line, Banasura Dam and Meenmutty
    route: "https://maps.app.goo.gl/F2BWtLEJnRctoxuz5"
    stops:
      - name: Zostel Plus Wayanad
        type: home
        note: "Start"
        lat: 11.5790
        lng: 76.0990
      - name: Muddy Boots Zip Line
        type: hill
        note: "Priority 1. ₹350"
        lat: 11.5446
        lng: 76.0840
      - name: Banasura Sagar Dam
        type: hill
        note: "Priority 1. Parking ₹10, entry ₹40, van ₹25"
        lat: 11.6667
        lng: 75.9547
      - name: Meenmutty Waterfalls
        type: waterfall
        note: "Priority 1. If closed, go back to Pookode Lake"
        lat: 11.4780
        lng: 76.1380
      - name: Zostel Plus Wayanad
        type: home
        note: "Back for the night. With time left, go to En Ooru Village"
        lat: 11.5790
        lng: 76.0990
        return: true
  - title: Glass bridge, wildlife or falls, and Edakkal Caves
    route: "https://maps.app.goo.gl/89nyRUktwwwhUG588"
    stops:
      - name: Zostel Plus Wayanad
        type: home
        note: "Start"
        lat: 11.5790
        lng: 76.0990
      - name: 900 Kandi Glass Bridge
        type: hill
        note: "Priority 1. Entry ₹250, jeep ₹200"
        lat: 11.5235
        lng: 76.1330
      - name: Soochipara Waterfalls
        type: waterfall
        note: "Or the Wildlife Sanctuary. If both are closed, use Plan B below"
        lat: 11.5115
        lng: 76.1767
      - name: Edakkal Caves
        type: cave
        note: "Entry ₹50, parking ₹10"
        lat: 11.6256
        lng: 76.2345
      - name: Zostel Plus Wayanad
        type: home
        note: "Back for the night"
        lat: 11.5790
        lng: 76.0990
        return: true
  - title: Chembra, Kalpetta and the bus to Calicut
    route: "https://maps.app.goo.gl/YpUmskkn3C7Kqh53A"
    stops:
      - name: Chembra Peak
        type: hill
        note: "The trek was closed. Grape tea at the base instead"
        lat: 11.5167
        lng: 76.0833
      - name: En Ooru Village
        type: town
        note: "Plan B: Likkidi View Point, Pookode Lake and En Ooru if left from Day 1"
        lat: 11.5535
        lng: 76.0356
      - name: Kalpetta bus stand
        type: bus
        note: "KSRTC bus to Calicut"
        lat: 11.6085
        lng: 76.0830
      - name: Calicut railway station
        type: train
        note: "Night train to Bengaluru"
        lat: 11.2480
        lng: 75.7830
---

Wayanad is the green, misty corner of Kerala up in the Western Ghats, and in June the clouds sit right on the tea estates. I went for 3 days with a friend, took the overnight sleeper bus up, rented a bike for the rides between spots and came back by train from Calicut. I kept a plan, a price list and a packing list for it, so I put them here.

<div class="callout"><strong>The short version.</strong> Sleeper bus from Bengaluru, two nights at Zostel Plus Wayanad, zip line and Banasura Dam on Day 1, the glass bridge and Edakkal Caves on Day 2, and a bus to Calicut for the night train home on Day 3.</div>

<div class="shots">
{% include shot.html file="slide-1.jpg" class="slide" caption="Wayanad, Monsoon 2024" %}
{% include shot.html file="slide-2.jpg" class="slide" caption="Views from the hostel and the dam" %}
</div>

### Getting there

I took the overnight sleeper bus from Bengaluru, which cost ₹1,470 for the two of us. My first plan was the train to Calicut and a bus up, but the up ticket was cancelled and refunded, so I kept the train for the way back (₹708 for two). From Calicut it is about 3 hours to Kalpetta by KSRTC bus, which I took on the way back, and an auto from the bus stop to the station cost ₹50.

### Where to stay

Zostel Plus Wayanad. Two nights came to about ₹3,900 for both of us. It sits up in the hills with a long view, a pool and a bonfire at night.

<div class="shots">
{% include shot.html file="slide-3.jpg" class="slide" caption="A story, in a few frames" %}
{% include shot.html file="slide-4.jpg" class="slide" caption="Around the hostel" %}
</div>

### Getting around

Rent a bike. Royal Brothers charged about ₹1,300 for the trip, and petrol came to ₹880 between us. Distances in Wayanad look small on the map but take time on the hill roads, so a bike is far better than relying on buses.

### Day 1: zip line, Banasura Dam and Meenmutty

Start at the Muddy Boots zip line (₹350). Banasura Sagar Dam is next: parking ₹10, entry ₹40, and a van to the top for ₹25 if you want it. Meenmutty Waterfalls is the third stop. If it is closed, go back to Pookode Lake instead. With time to spare in the afternoon, go to En Ooru Village (₹50 entry plus ₹30 for the jeep, both ways) and then back to the hostel. If you are short on time, skip Meenmutty and go to Kurumbalakotta Mala and back.

### Day 2: glass bridge and Edakkal Caves

The glass bridge at 900 Kandi has a ₹250 entry, ₹10 parking and a ₹200 jeep ride up. After that go to the Wildlife Sanctuary or Soochipara Waterfalls, whichever is open, and finish with Edakkal Caves (₹50 entry, ₹10 parking). If the first two are closed, use Plan B: the glass bridge, Likkidi View Point, Pookode Lake and En Ooru Village.

<div class="shots">
{% include shot.html file="slide-5.jpg" class="slide" caption="900 Kandi" %}
{% include shot.html file="slide-6.jpg" class="slide" caption="On the road" %}
</div>

### Day 3: Chembra and the way back

The Chembra Peak trek (₹75) was closed when I went, so I had grape tea at the base and shopped for vegetables in Kalpetta. Then I took the KSRTC bus from Kalpetta to Calicut (₹87 each), an auto to the station, dinner and the night train home. Back in Bengaluru, the metro and a local bus got me home.

<div class="shots">
{% include shot.html file="slide-7.jpg" class="slide" caption="Around the campfire" %}
</div>

### Prices I saw

<details class="ref">
<summary>Entry charges and fares</summary>
<div class="table-scroll"><table class="timetable"><thead><tr><th>Place</th><th>Price</th><th>For</th></tr></thead><tbody>
<tr><td>En Ooru</td><td>₹50</td><td>Entry</td></tr>
<tr><td>En Ooru jeep</td><td>₹30</td><td>To and from</td></tr>
<tr><td>900 Kandi</td><td>₹250</td><td>Entry</td></tr>
<tr><td>900 Kandi jeep</td><td>₹200</td><td>To and from</td></tr>
<tr><td>Muddy Boots</td><td>₹350</td><td>Zip line</td></tr>
<tr><td>Banasura Sagar Dam</td><td>₹10 + ₹40</td><td>Parking and entry</td></tr>
<tr><td>Banasura Sagar Dam van</td><td>₹25</td><td>Optional, to and from</td></tr>
<tr><td>Meenmutty</td><td>₹50</td><td>Entry</td></tr>
<tr><td>Edakkal Caves</td><td>₹80</td><td>Entry on the board (I paid ₹50)</td></tr>
<tr><td>Chembra Peak</td><td>₹75</td><td>Trekking</td></tr>
<tr><td>Kalpetta to Kozhikode</td><td>₹98</td><td>Bus</td></tr>
</tbody></table></div>
</details>

### Packing list

- Two cargos, two sweatshirts, a cap, four hankies, a bathing towel and a hand towel
- Three pairs of socks, white shoes, sandals, a T-shirt and a raincoat
- A blanket and an inflatable pillow for the bus
- Dry, ready-to-eat snacks and some extra carrying bags
- A plastic protector for the phone (still unticked on my list)
