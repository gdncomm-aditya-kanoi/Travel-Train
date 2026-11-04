---
title: Hampi
state: Karnataka
date: 2025-07-15            # used to sort trips, newest first (approximate, please confirm)
summary: "Boulders, ruined temples and cycle rides in Hampi, then on to Badami and Pattadakal."
month: "Monsoon"
days_count: 3
best_season: "Oct – Feb"
cost_note: "per person"

# Photos live in assets/images/hampi/. Swap any file for your own and keep the name, or add paths under gallery.
cover: /assets/images/hampi/collage.jpg
cover_alt: "A collage of my Hampi trip"
card: /assets/images/hampi/u-vittala-sunset.jpg
banner: /assets/images/hampi/banner.svg
gallery: []

# Cheat-sheet PDF and line-art banner are made by tools/build_assets.py
map_pdf: /assets/maps/hampi-guide.pdf

instagram:
  - https://www.instagram.com/p/DIISz40zrSf/
  - https://www.instagram.com/p/C9obSeVSdJW/

expenses:                   # rupees per person (the trip was for 2, split in half)
  - category: Getting there
    note: "Train both ways: Bengaluru to Hospet, Badami to Bengaluru"
    amount: 308
  - category: Stay
    note: "Viru Homestay, Kadirampura, 2 nights"
    amount: 439
  - category: Food
    note: "Chai, dosa, rooftop lunch, café dinner"
    amount: 462
  - category: Local transport
    note: "Cycles, local buses, a few autos"
    amount: 338
  - category: Entry
    note: "Vittala Temple chariot ticket"
    amount: 18

things_to_do:
  - "Rent a plain ₹100 cycle in the morning and return it at night"
  - "Day 1: Virupaksha, Krishna Temple, Vittala Temple and its stone chariot"
  - "Day 2: Hazara Rama, Lotus Mahal, Elephant Stable, Queen's Bath, then Matanga Hill at sunset"
  - "Day 3: Badami Caves, fort and falls, then Pattadakal"
  - "Use a map: Hampi is spread out and signs are few"
things_to_skip:
  - "Autos outside Hospet station (₹600–1,000): take the ₹15 bus from JSW bus stop"
  - "Zostel Hampi without your own vehicle: 30 km out, uphill, rough road"
  - "Staying in Hampi or Hospet: Kadirampura is cheaper and closer"
  - "Slow local buses from Ilkal to Badami: take only Superfast"
  - "Looking for a bike rental: there is none"

eat:
  - name: Happy Hampi Cafe
    note: "Breakfast · Kadirampura"
  - name: Gopi Roof Restaurant
    note: "Lunch · Hampi"
  - name: Chillout Bamboo
    note: "Lunch · Hampi · a bit pricey, lovely setting"
  - name: Old Chill Out Ganesh
    note: "Indian food · Hampi"
  - name: Shanti Cafe
    note: "Cheap, all meals · Kadirampura"
  - name: Hotel Paradise
    note: "Cheap, all meals · Badami"

details:
  - label: Nearest station
    value: "Hospet Junction, 13 km"
  - label: Nearest airport
    value: "Hubballi or Toranagallu (JSW)"
  - label: Where I stayed
    value: "Viru Homestay, Kadirampura (₹400 a night)"
  - label: Cycle hire
    value: "₹100 plain · ₹200 basket · ₹300 geared"
  - label: Budget level
    value: "Backpacker"

# Coordinates are from OpenStreetMap. Kadirampura is approximate.
# "route" opens in Google Maps with every stop in order.
days:
  - title: Temples and the stone chariot
    route: "https://www.google.com/maps/dir/?api=1&origin=15.3325,76.4520&destination=15.3325,76.4520&waypoints=15.3352,76.4587%7C15.3302,76.4604%7C15.3423,76.4755&travelmode=bicycling"
    stops:
      - name: Kadirampura
        type: home
        note: Start. Hire the cycle here
        lat: 15.3325
        lng: 76.4520
      - name: Virupaksha Temple
        type: temple
        note: Dosa breakfast in the bazaar
        lat: 15.3352
        lng: 76.4587
      - name: Krishna Temple
        type: temple
        lat: 15.3302
        lng: 76.4604
      - name: Vittala Temple
        type: chariot
        note: The stone chariot
        lat: 15.3423
        lng: 76.4755
      - name: Kadirampura
        type: home
        note: Back for the night
        lat: 15.3325
        lng: 76.4520
        return: true
  - title: Royal enclosure and Matanga Hill
    route: "https://www.google.com/maps/dir/?api=1&origin=15.3325,76.4520&destination=15.3325,76.4520&waypoints=15.3178,76.4689%7C15.3203,76.4714%7C15.3211,76.4728%7C15.3134,76.4728%7C15.3316,76.4684&travelmode=bicycling"
    stops:
      - name: Kadirampura
        type: home
        note: Start
        lat: 15.3325
        lng: 76.4520
      - name: Hazara Rama Temple
        type: temple
        lat: 15.3178
        lng: 76.4689
      - name: Lotus Mahal
        type: palace
        lat: 15.3203
        lng: 76.4714
      - name: Elephant Stable
        type: stable
        lat: 15.3211
        lng: 76.4728
      - name: Queen's Bath
        type: bath
        lat: 15.3134
        lng: 76.4728
      - name: Matanga Hill
        type: hill
        note: Sunset climb
        lat: 15.3316
        lng: 76.4684
      - name: Kadirampura
        type: home
        note: Back for the night
        lat: 15.3325
        lng: 76.4520
        return: true
  - title: Bus to Badami and Pattadakal
    route: "https://www.google.com/maps/dir/?api=1&origin=15.3325,76.4520&destination=15.9484,75.8160&waypoints=15.2752,76.3893%7C15.9598,76.1156%7C15.9184,75.6844&travelmode=driving"
    stops:
      - name: Kadirampura
        type: home
        note: "Bus to Hospet, ₹15"
        lat: 15.3325
        lng: 76.4520
      - name: Hospet bus stand
        type: bus
        note: "Bus to Ilkal, ₹140, about 2.5 hours"
        lat: 15.2752
        lng: 76.3893
      - name: Ilkal
        type: town
        note: "Change to a Superfast bus, ₹81"
        lat: 15.9598
        lng: 76.1156
      - name: Badami
        type: cave
        note: "Caves, fort, Bhutanatha Temple and falls"
        lat: 15.9184
        lng: 75.6844
      - name: Pattadakal
        type: temple
        note: Group of monuments
        lat: 15.9484
        lng: 75.8160

credits:
  - title: "Lotus Mahal"
    author: "Vyacheslav Argenberg"
    license: "CC BY 4.0"
    license_url: https://creativecommons.org/licenses/by/4.0
    source: https://commons.wikimedia.org/wiki/File:Hampi,_India,_Lotus_Mahal.jpg
  - title: "Elephant Stables"
    author: "Ingo Mehling"
    license: "CC BY-SA 4.0"
    license_url: https://creativecommons.org/licenses/by-sa/4.0
    source: https://commons.wikimedia.org/wiki/File:Hampi_-_Elephant_Stables.jpg
  - title: "Coracles on the Tungabhadra"
    author: "Dey.sandip"
    license: "CC BY-SA 3.0"
    license_url: https://creativecommons.org/licenses/by-sa/3.0
    source: https://commons.wikimedia.org/wiki/File:Two_Coracles_and_Tungabhadra_River.jpg
---
Hampi doesn't feel like a town. It feels like a giant open-air museum dropped between boulders, banana fields and a river. I went for 3 days with one friend: two days cycling around the ruins, then one long, chaotic day to Badami and Pattadakal. This is everything that worked, everything that didn't, and the money side, so you can skip my mistakes.

<div class="callout"><strong>The short version.</strong> Stay in Kadirampura, hire a ₹100 cycle, never take the autos outside Hospet station, and give Badami its own day. The rest of this page is why.</div>

### Getting there

I took the overnight Hampi Express (Golgumbaz Express) from Bengaluru. It leaves around 10 PM and drops you at Hospet Junction by about 7 AM, which is the nearest station. Sleeper was ₹260, and the big city around it has everything you need.

<div class="callout warn"><strong>The auto trap.</strong> Right outside the station, autos quote ₹600–1,000 for Hampi. Ignore them. Walk 600 m to JSW bus stop, the biggest in the district, and take a bus to Hampi or Kadirampura for ₹15.</div>

### Getting around


There are no scooter or bike rentals in Hampi, Hospet or Kadirampura (the auto owners have that locked up), so your choices are an auto (about ₹1,500 for a day), a bus that only drops you in Hampi, or a cycle. Take the cycle.

- ₹100 a day for a plain cycle, ₹200 with a basket, ₹300 geared. I took the ₹100 one.
- Rent in the morning, return at night.
- Ask the shop to explain the map. Ours did, and it saved us hours.

<div class="shots">
{% include shot.html file="u-cycle.jpg" caption="My ₹100 cycle, heading for Vittala Bazaar" %}
{% include shot.html file="06-coracles.jpg" caption="Coracles on the Tungabhadra" %}
</div>

### Where to stay

I stayed in **Kadirampura**, a small village 2–2.5 km from the monuments. Stays are cheap, and cafés and breakfast places are 300 m away. Viru Homestay cost ₹1,750 for two people for two nights (about ₹400 per person per night, booked on Goibibo, which gave extra discounts). The rooms and bathrooms were spotless, with a balcony and a terrace with night lights, and the host was lovely. Hotels in Hospet mean a commute every evening, and homestays inside Hampi are overpriced.

**Why not Zostel?** I usually stay in Zostels, so I booked Zostel Hampi, then cancelled and lost about ₹800.

- Good: the views of Kishkindha, the Tungabhadra nearby, a campfire, games and a workspace with wifi.
- Not good: it is in Gangavati, 30 km from Hospet and 15 km from Hampi, uphill on a road that is broken in places and risky after dark or in rain. It is the only place to eat nearby, and beds run about ₹1,000 (4-bed dorm) or ₹750 (6–8 beds), which is dear for Hampi.

Unless you have your own vehicle, skip it.

### The days

**Day 1: temples and the chariot.** Start with a dosa breakfast at Virupaksha, then do the Krishna Temple, the Ganesha statues, Ugra Narasimha and the Shivling. Finish at Vittala Temple for the stone chariot (₹35 ticket), the one on the ₹50 note.




<div class="shots">
{% include shot.html file="u-ganesha-shrine.jpg" caption="Sasivekalu Ganesha shrine" %}
{% include shot.html file="u-kadalekalu.jpg" caption="Inside the giant Ganesha shrine" %}
{% include shot.html file="u-virupaksha-tank.jpg" caption="Virupaksha Temple tower over the tank" %}
{% include shot.html file="u-vittala-sunset.jpg" caption="Vittala Temple complex at golden hour" %}
</div>

**Day 2: the royal enclosure.** Lotus Mahal, Elephant Stable, Queen's Bathhouse, the Victory Palace and Hazara Rama Temple, then Matanga Hill for the view.


<div class="shots">
{% include shot.html file="04-lotus-mahal.jpg" caption="Lotus Mahal" %}
{% include shot.html file="05-elephant-stables.jpg" caption="Elephant Stables, eleven domed halls" %}
</div>

**Day 3: Badami and Pattadakal.** Badami Caves, Bhoothnath Temple, the fort and falls, the lakeside, then the Group of Monuments at Pattadakal.



<div class="shots">
{% include shot.html file="u-badami-vishnu.jpg" caption="Vishnu seated on the serpent Sesha, Badami caves" %}
{% include shot.html file="u-badami-lake.jpg" caption="Agastya Lake, Badami, with the Bhoothnath temples" %}
</div>

### Food

Options are limited, and non-veg is rare, so expect veg or egg. Many cafés are aimed at foreign tourists, so as an Indian you will find prices a little high. Six places I would go back to are listed on the right; Gopi Roof for lunch and Happy Hampi Cafe for breakfast are the easy ones.

### Hampi to Badami: the hard part

This is the real *maut ka khel*. There is no direct bus, and cabs ask over ₹3,000. Your options:

1. **Train:** Hospet to Badami at 5:45 AM or at midnight. The MEMU and DEMU timetable is worth checking, because it is hard to find online or on Google Maps.
2. **Bus:** Kadirampura to Hospet (₹15), Hospet to Ilkal (₹140, about 2.5 hours), Ilkal to Badami (₹81, about 2 hours).

What I learned doing it by bus:

- Eat before you leave. There is almost nothing to eat in Ilkal or Badami's main town.
- Ilkal has many beggars who will crowd you. Keep your things close while you change buses.
- Take only **Superfast** buses. The ordinary bus from Ilkal went into every village and took 2 hours for a 30-minute ride.
- ₹140 and ₹81 for about 230 km is steep compared to Kerala.


### What I'd add to this plan

<div class="callout"><strong>A few things worth adding</strong>, from reading around rather than from my own trip, so check them locally:
<ul>
<li><strong>Start early.</strong> Do the big sites before 9 AM. Midday is hot, the rock and stone floors burn, and the tour groups arrive. Carry water and a hat.</li>
<li><strong>Sunrise or sunset on Matanga Hill.</strong> It is the best free view of the whole site. Take a torch for the climb down.</li>
<li><strong>Try a coracle ride</strong> on the Tungabhadra, and ask the price before you sit in. In the monsoon they are sometimes stopped when the river is high.</li>
<li><strong>Anegundi and Anjanadri Hill</strong> (the Hanuman birthplace), across the river, make a good half-day if you have a spare day.</li>
<li><strong>Don't squeeze Badami into one day.</strong> It is about 4.5 hours of bus riding, plus waiting. If you can, sleep one night in Badami and do the caves and Pattadakal properly.</li>
<li><strong>Why no non-veg?</strong> The area around Hampi Bazaar is a protected heritage zone, so non-veg and alcohol are largely off the menu there.</li>
<li><strong>Carry cash.</strong> ATMs are few, and small cafés and cycle shops may not take UPI.</li>
<li><strong>Check ticket rules.</strong> Only some monuments are ticketed. Ask at the first counter whether the ticket is valid at the other sites the same day.</li>
</ul></div>
