---
title: Kudremukh
state: Karnataka
date: 2026-08-31            # used to sort trips, newest first (the trip ran 30 to 31 August 2026)
summary: "A guided-permit trek to Kudremukh Peak in the Western Ghats: rolling grassland ridges, cloud over the peak and a 20 km round trip, with Belur on the way in."
month: "August 2026"
days_count: 2
best_season: "Monsoon and just after (Jun – Oct)"
cost_note: "per person, whole trip including Belur"
stay_short: "Homestay in Samse"

cover: /assets/images/kudremukh/cover.jpg
cover_alt: "Green grassland ridges of Kudremukh under heavy cloud"
cover_strip: true             # show the cover whole at full width
card: /assets/images/kudremukh/card.jpg
banner: ""
gallery: []

series: kudremukh-trip
series_order: 1
series_title: "The Kudremukh trip"
series_label: "Overview and trek"

instagram:
  - https://www.instagram.com/p/DdHAH-oifVP/?img_index=1
  - https://www.instagram.com/p/DdOskKGicri/?img_index=1
  - https://www.instagram.com/p/DdMJ7XjiViA/?img_index=1
  - https://www.instagram.com/p/DdJpRbSiUZU/?img_index=1

expenses:                   # rupees per person (2 of us, split evenly, from my sheet; the Belur part is on the Belur page)
  - category: Trek pass
    note: "Aranya Vihaara booking, ₹1,160 for two"
    amount: 580
  - category: Homestay
    note: "River Edge homestay in Samse, ₹2,400 for two"
    amount: 1200
  - category: Coffee and masala puri
    note: "In Kalasa, on arrival"
    amount: 52
  - category: Auto to the homestay
    note: "Kalasa to the homestay, ₹300 for two"
    amount: 150
  - category: Jeep and guide
    note: "Homestay to the base camp, ₹828 for two"
    amount: 414
  - category: Auto back to Kalasa
    note: "Homestay to Kalasa bus stop (a bus is cheaper)"
    amount: 150
  - category: Bike parking
    note: "₹200 for two"
    amount: 100
  - category: Bus home
    note: "Kalasa to Bengaluru, non-AC sleeper, ₹1,670 for two. A non-AC seater was ₹435 each"
    amount: 835
  - category: Belur on the way in
    note: "Bus from Bengaluru, lunch and the Belur to Kalasa bus: see the Belur page"
    amount: 938

things_to_do:
  - "Book the pass on Aranya Vihaara as soon as the slots open: they sell out"
  - "Stay the night before in Samse so you start fresh at the base"
  - "Have a heavy breakfast and carry a tiffin, such as puliyogare rice"
  - "Start before the morning cut-off and be down before dark"
  - "Soak your socks in Dettol and salt for the leeches"
  - "Carry your trash back with you"
things_to_skip:
  - "Racing to the top: it is not a race, so spend time on the trail"
  - "Regular sneakers: the trail is slippery and I saw one sole come off"
  - "Booking before your dates are locked: the pass is non-refundable"
  - "Plastic bottles and wafer packets: no single-use plastic is allowed"

eat:
  - name: Homestay in Samse
    note: "Dinner and breakfast; they can pack a lunch if you ask"
  - name: Coffee and masala puri, Kalasa
    note: "First stop after the bus"
  - name: Masala dosa, Kalasa
    note: "Post-trek snack before the night bus"

details:
  - label: Peak height
    value: "About 6,214 ft (from my route sheet)"
  - label: Distance
    value: "About 20 km round trip"
  - label: Time
    value: "6 to 8 hours including breaks"
  - label: Pass
    value: "Aranya Vihaara (aranyavihaara.karnataka.gov.in), for me 6 AM to 11 AM slot"
  - label: Getting there
    value: "Bus Bengaluru to Belur, then Belur to Kalasa, then an auto to Samse"
  - label: Budget level
    value: "Backpacker"

# Coordinates are approximate, picked by eye from the map. Check them in Google Maps before you rely on them.
# "route" opens in Google Maps with every stop in order.
days:
  - title: Bengaluru to Belur to Samse
    route: "https://www.google.com/maps/dir/?api=1&origin=12.9767,77.5713&destination=13.2330,75.2850&waypoints=13.1650,75.8650%7C13.2380,75.3590&travelmode=driving"
    stops:
      - name: Majestic bus stand, Bengaluru
        type: bus
        note: "Bus to Belur"
        lat: 12.9767
        lng: 77.5713
      - name: Belur
        type: temple
        note: "Chennakeshava temple and lunch. See the Belur page"
        lat: 13.1650
        lng: 75.8650
      - name: Kalasa
        type: bus
        note: "Belur to Kalasa bus at 3:15 PM, then coffee and masala puri"
        lat: 13.2380
        lng: 75.3590
      - name: Samse homestay
        type: home
        note: "Auto from Kalasa, about 15 minutes"
        lat: 13.2330
        lng: 75.2850
  - title: The Kudremukh trek
    route: "https://www.google.com/maps/dir/?api=1&origin=13.2330,75.2850&destination=13.1250,75.2480&waypoints=13.2200,75.2600&travelmode=walking"
    stops:
      - name: Samse homestay
        type: home
        note: "Jeep to the base camp early in the morning"
        lat: 13.2330
        lng: 75.2850
      - name: Base camp and checkpost
        type: town
        note: "Permit and ID check, guide, plastic check"
        lat: 13.2200
        lng: 75.2600
      - name: Kudremukh Peak
        type: peak
        note: "About 4 hours up, lunch at the top"
        lat: 13.1250
        lng: 75.2480
      - name: Kalasa
        type: bus
        note: "About 4 hours down, auto to Kalasa, night bus to Bengaluru"
        lat: 13.2380
        lng: 75.3590
        return: true
---

Kudremukh is a peak in the Western Ghats, in Kudremukh National Park, Chikkamagaluru district. This page is the parent of a 2-day trip: a day on the road through [Belur]({{ '/trips/belur/' | relative_url }}) to a homestay in Samse, then the trek the next morning and the night bus home. I went with a friend, and all the costs below are per person.

<div class="callout"><strong>The whole trip in one line.</strong> Bus to Belur and its Hoysala temples, bus on to Kalasa, a night in Samse, the trek from about 6 AM, then the night bus back to Bengaluru. Book the pass first, because everything else depends on the date.</div>

### How the two pages fit together

- **Kudremukh (this page):** the permit, the stay, the trek, the money and what to carry.
- **[Belur]({{ '/trips/belur/' | relative_url }}) (Day 1):** the stop on the bus route from Bengaluru. There is no direct bus to Kalasa, so Belur is where you change, and the temple is worth the break.

### The permit, first

The trek only runs through the Aranya Vihaara portal (aranyavihaara.karnataka.gov.in). Daily numbers are capped, weekend slots go fast, every trekker needs a government ID on the booking, and it is non-refundable. My slot was 6 AM to 11 AM on 31 August, so I had to be at the checkpost early. Do not rely on any blog for the exact fee, because it changes every year. Check the portal.

<div class="shots stories">
{% include shot.html file="itinerary.jpg" class="full" caption="The route: Samse, base camp, stream, peak" %}
{% include shot.html file="permit.jpg" class="full" caption="Permit and guide" %}
{% include shot.html file="travel-plan.jpg" class="full" caption="Bengaluru, Kalasa, Samse" %}
</div>

### Getting there

From HSR Layout I went to Majestic and took a bus to [Belur]({{ '/trips/belur/' | relative_url }}). At Belur I took one of the Belur to Horanadu express buses that stop at Kalasa on the way (via Mudigere and Kottigehara). The 3:15 PM one worked for me, and the others leave at 1:15, 2:15, 4:00, 5:00 and 5:45 PM. At Kalasa I had coffee and masala puri, then an auto to the homestay in Samse.

### Where to stay

Samse is the village where most homestays are, about 15 minutes from Kalasa, so you can sleep near the base and start fresh. Mine was the River Edge homestay: ₹1,200 each for the night, with a view of a stream from the stay. Book ahead, and ask them to pack breakfast and a lunch.

### The trek

In the morning we took a shared jeep from the homestay to the base camp, where the guide, the permit and the ID check happen, with a plastic check too. From there it is about 9 km to the peak. A guide is compulsory to start. In my case you walk at your own pace and the guide does not stay with you, but some reports say they stay with the group, so do not plan around either.

The path starts in dense forest with streams, muddy roots and leeches, then opens onto huge grassland ridges, with a lone tree as a rest point. The last stretch is a long, steady climb in changing weather: one minute you can see for miles, the next you are in cloud. It took me about 4 hours up, a hot lunch at the top, and about 4 hours back down.

<div class="shots stories">
{% include shot.html file="base-camp.jpg" class="full" caption="Base camp to the hike" %}
{% include shot.html file="hike-minutes.jpg" class="full" caption="Hike minutes" %}
{% include shot.html file="worth-it.jpg" class="full" caption="Was it worth it? Hell yes" %}
</div>

### What to carry

- 1 L of water, and refill at the streams along the trail
- Trekking shoes with good grip, extra socks and a rain jacket or poncho
- Snacks with the outer plastic removed, a tiffin lunch, power bank, cap and sunscreen
- Salt and Dettol for the leeches, a small first-aid kit and a bag for your trash
- The printed permit and the original ID, since they check them
- Trekking poles help on the muddy descent

<div class="shots stories">
{% include shot.html file="essentials.jpg" class="full" caption="Essentials to carry" %}
</div>

### Going back

We came down, took an auto from the homestay to the Kalasa bus stop, had a masala dosa and took the night bus to Bengaluru. I took a non-AC sleeper because I was exhausted, and a seater is cheaper.

### Questions I got asked

- **How hard is it?** Moderate. It is long, with several climbs and flat stretches between them, but not technical. Do some walking or cardio first.
- **Is it for beginners?** Yes, with reasonable fitness.
- **Leeches?** Yes, especially in the rains. Wear proper socks and use salt and Dettol.
- **Can you camp at the peak?** No, it is banned. You come down the same day.
- **Best time?** During and just after the monsoon it is extremely green, but expect mud, mist and poor views at the top.
- **The one thing to know?** Do not underestimate the distance. Start early, keep a buffer for the return and take your trash back.

### What I'd add to this plan

<div class="callout"><strong>A few things worth adding</strong>, from reading around rather than from my own trip, so check them locally:
<ul>
<li><strong>Be at the checkpost early.</strong> There is a morning entry cut-off, and you cannot get in after it.</li>
<li><strong>Phone signal drops</strong> past the checkpost, so download offline maps and tell someone your plan.</li>
<li><strong>Weather flips fast.</strong> Leave a buffer so you are not coming down in the dark.</li>
<li><strong>Prices drift.</strong> Treat my costs as a ballpark for the year I went.</li>
</ul></div>

**Next:** Day 1, the stopover in [Belur]({{ '/trips/belur/' | relative_url }}).
