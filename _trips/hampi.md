---
title: Hampi
state: Karnataka
date: 2025-07-15            # used to sort trips, newest first (approximate, please confirm)
summary: "Boulders, ruined temples and cycle rides in Hampi, then on to Badami and Pattadakal."
month: "Monsoon"
days_count: 3
best_season: "Oct – Feb"
cost_note: "per person"

# Photos: drop files into assets/images/hampi/ and list them under gallery.
cover: /assets/images/hampi/cover.svg       # city banner; swap for cover.jpg when you have a photo
gallery: []
#  - /assets/images/hampi/01.jpg
#  - /assets/images/hampi/02.jpg

# Cheat-sheet PDF (made by tools/build_assets.py)
map_pdf: /assets/maps/hampi-guide.pdf

instagram:
  - https://www.instagram.com/p/DIISz40zrSf/

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
        note: Start. Hire the cycle here
        lat: 15.3325
        lng: 76.4520
      - name: Virupaksha Temple
        note: Dosa breakfast in the bazaar
        lat: 15.3352
        lng: 76.4587
      - name: Krishna Temple
        lat: 15.3302
        lng: 76.4604
      - name: Vittala Temple
        note: The stone chariot
        lat: 15.3423
        lng: 76.4755
      - name: Kadirampura
        note: Back for the night
        lat: 15.3325
        lng: 76.4520
        return: true
  - title: Royal enclosure and Matanga Hill
    route: "https://www.google.com/maps/dir/?api=1&origin=15.3325,76.4520&destination=15.3325,76.4520&waypoints=15.3178,76.4689%7C15.3203,76.4714%7C15.3211,76.4728%7C15.3134,76.4728%7C15.3316,76.4684&travelmode=bicycling"
    stops:
      - name: Kadirampura
        note: Start
        lat: 15.3325
        lng: 76.4520
      - name: Hazara Rama Temple
        lat: 15.3178
        lng: 76.4689
      - name: Lotus Mahal
        lat: 15.3203
        lng: 76.4714
      - name: Elephant Stable
        lat: 15.3211
        lng: 76.4728
      - name: Queen's Bath
        lat: 15.3134
        lng: 76.4728
      - name: Matanga Hill
        note: Sunset climb
        lat: 15.3316
        lng: 76.4684
      - name: Kadirampura
        note: Back for the night
        lat: 15.3325
        lng: 76.4520
        return: true
  - title: Bus to Badami and Pattadakal
    route: "https://www.google.com/maps/dir/?api=1&origin=15.3325,76.4520&destination=15.9484,75.8160&waypoints=15.2752,76.3893%7C15.9598,76.1156%7C15.9184,75.6844&travelmode=driving"
    stops:
      - name: Kadirampura
        note: "Bus to Hospet, ₹15"
        lat: 15.3325
        lng: 76.4520
      - name: Hospet bus stand
        note: "Bus to Ilkal, ₹140, about 2.5 hours"
        lat: 15.2752
        lng: 76.3893
      - name: Ilkal
        note: "Change to a Superfast bus, ₹81"
        lat: 15.9598
        lng: 76.1156
      - name: Badami
        note: "Caves, fort, Bhutanatha Temple and falls"
        lat: 15.9184
        lng: 75.6844
      - name: Pattadakal
        note: Group of monuments
        lat: 15.9484
        lng: 75.8160
---

Hampi is the ruined Vijayanagara capital in North Karnataka. I went for 3 days with a friend: two days of cycling around the ruins, then one long bus day to Badami and Pattadakal.

- **Stay in Kadirampura**, 2 km from the ruins. Homestays there are clean and cheap.
- **Hire a cycle** for ₹100 a day. There are no bike rentals, and autos cost about ₹1,500 a day.
- **Skip the autos at Hospet station.** Walk 600 m to JSW bus stop; the bus to Hampi is ₹15.
- **Hampi to Badami is the hard part.** Take Superfast buses only (Hospet, Ilkal, Badami), or the 5:45 AM train from Hospet.
- **Food is mostly veg or egg**, and priced for tourists.
