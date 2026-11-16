---
title: Ooty and Coonoor
state: Tamil Nadu
date: 2026-09-04            # used to sort trips, newest first (the trip ran 2 to 5 September 2026)
summary: "Three days in the Nilgiris: a Zostel above the tea hills, Ooty Lake, Pykara Waterfall, a campfire at 12 degrees and the Nilgiri toy train from Ooty down to Coonoor."
month: "September 2026"
days_count: 3
best_season: "Oct – Jun (I went in September: cloudy, with some rain)"
cost_note: "per person, 3 of us splitting evenly (without the Zostel bed and the Bengaluru to Coimbatore train)"
stay_short: "Zostel Ooty (dorm)"

cover: /assets/images/ooty/cover.jpg
cover_alt: "Evening light over the green hills and cottages of Ooty"
cover_strip: true             # show the cover whole at full width
card: /assets/images/ooty/card.jpg
banner: /assets/images/ooty/banner.svg
gallery: []

instagram:
  - https://www.instagram.com/p/DdnY9T5iUbs/?img_index=1
  - https://www.instagram.com/p/DeD5UqSCcBH/?img_index=1
  - https://www.instagram.com/p/Dd-k-I0iNae/?img_index=1
  - https://www.instagram.com/p/Ddsj81miDX0/?img_index=1
  - https://www.instagram.com/p/Dd1PxCKCc2o/?img_index=1
  - https://www.instagram.com/p/DdkzRnipczL/
  - https://www.instagram.com/p/DdZE2DTCdCd/?img_index=1

expenses:                   # rupees per person, from our shared sheet (3 of us, split evenly; the group total was ₹13,028)
  - category: Getting to Ooty
    note: "Cab from HSR to KSR Majestic, auto from Coimbatore station to the bus stop, bus from Coimbatore to Ooty"
    amount: 229
  - category: Autos and the day cab
    note: "Ooty bus stand to the Zostel, town, tea factory and gardens, back to the hostel, the 6th Mile and Pykara day cab (₹2,000 for the car), Zostel to the station, Coonoor autos"
    amount: 1586
  - category: Food, tea and cafés
    note: "Zostel breakfast, De Jones Tea Bar, Moody's, Pykara lunch, La Bella Vie, chai stops and the Coimbatore dinner"
    amount: 1606
  - category: Entry fees and boating
    note: "Ooty Lake boating, tea factory and tea garden, Botanical Garden, two pine forests, 6th Mile shooting point, Pykara falls and lake, Dolphin's Nose"
    amount: 522
  - category: Nilgiri toy train, Ooty to Coonoor
    note: "Second sitting, ₹499.05 for the three of us (fare, IRCTC fee and insurance)"
    amount: 166
  - category: Coonoor back to Bengaluru
    note: "Coonoor to Coimbatore bus, a Coimbatore station AC waiting hall, the Bengaluru station to HSR bus"
    amount: 171
  - category: Zostel Ooty bed, 2 nights
    note: "Not in my sheet. Check the price on the Zostel app for your dates"
    amount: 0
  - category: Bengaluru to Coimbatore train
    note: "Not in my sheet"
    amount: 0

things_to_do:
  - "Book the Ooty to Coonoor toy train on IRCTC as soon as the dates are fixed"
  - "Stay in a Zostel in Ooty for the views and the common room, and have the campfire"
  - "Take a cab for a day to Pykara Waterfall, the pine forests and the 6th Mile shooting point"
  - "Sit by the window on the toy train, the tea estates and tunnels are the point"
  - "Come back from Coonoor by road so the day is not all train"
  - "Carry a jacket: it was 12 degrees and windy at night"
things_to_skip:
  - "Packing the day too full: the toy train is slow and that is the whole point"
  - "Going without a printout or the original ID for the train: the ERS says it is needed"
  - "Booking the cab without agreeing the full-day price first"
  - "Relying on a clear sky in the monsoon: some of my days were rainy"

eat:
  - name: Zostel Ooty
    note: "Breakfast with paratha, omelette and corn flakes, and dinner, ₹683 for the three of us"
  - name: De Jones Tea Bar
    note: "A tea stop in Ooty"
  - name: Moody's
    note: "Strawberry chocolate, a croissant and puffs"
  - name: La Bella Vie, Coonoor
    note: "The house of the Kapoor and Sons film, now a café and restaurant"
  - name: Valarmathi Mess, Coimbatore
    note: "Dinner near the railway station before the night train"

details:
  - label: Getting there
    value: "Train to Coimbatore, then a bus up to Ooty"
  - label: Stay
    value: "Zostel Ooty, dorm bed"
  - label: Toy train
    value: "56139 UAM ONR Pass, Ooty to Coonoor, 9:15 to 10:20, second sitting"
  - label: Getting around
    value: "Autos in town, a cab for Pykara, the toy train to Coonoor"
  - label: Budget level
    value: "Backpacker"

# Coordinates are approximate, picked by eye from the map. Check them in Google Maps before you rely on them.
# "route" opens in Google Maps with every stop in order.
days:
  - title: Coimbatore to Ooty (2 September)
    route: "https://www.google.com/maps/dir/?api=1&origin=11.0005,76.9667&destination=11.4020,76.6880&waypoints=11.4102,76.6950%7C11.4188,76.7116&travelmode=driving"
    stops:
      - name: Coimbatore Railway Station
        type: train
        note: "Overnight train from Bengaluru, then an auto to the bus stop"
        lat: 11.0005
        lng: 76.9667
      - name: Coimbatore to Ooty bus
        type: bus
        note: "Bus up the ghat road to Ooty"
      - name: Zostel Ooty
        type: home
        note: "Auto from the bus stand, breakfast and a rest"
      - name: Ooty Lake
        type: town
        note: "Pedal boating and samosas"
        lat: 11.4020
        lng: 76.6880
      - name: Tea factory and Botanical Garden
        type: hill
        note: "By auto: tea factory, tea estate, garden and groundnuts"
        lat: 11.4188
        lng: 76.7116
      - name: De Jones Tea Bar and Moody's
        type: food
        note: "Tea, then pastries before the auto back to the hostel"
  - title: Pykara and the pine forests (3 September)
    route: "https://www.google.com/maps/dir/?api=1&origin=11.4102,76.6950&destination=11.4729,76.6041&travelmode=driving"
    stops:
      - name: Pine Forest
        type: hill
        note: "First of two pine forests, entry fee"
      - name: 6th Mile Shooting Point
        type: hill
        note: "A viewpoint and film spot, entry fee"
      - name: Pykara Waterfall and Lake
        type: waterfall
        note: "Lunch by the falls, falls entry, a car entry for the lake"
        lat: 11.4729
        lng: 76.6041
      - name: Cosmic Cups
        type: food
        note: "Chai on the way back"
      - name: Zostel Ooty, evening
        type: home
        note: "Dinner and the campfire at 12 degrees"
  - title: Toy train to Coonoor and home (4 September)
    route: "https://www.google.com/maps/dir/?api=1&origin=11.4088,76.6990&destination=11.3533,76.7957&travelmode=driving"
    stops:
      - name: Ooty Railway Station (UAM)
        type: train
        note: "The 9:15 toy train, second sitting"
        lat: 11.4088
        lng: 76.6990
      - name: Coonoor Railway Station (ONR)
        type: train
        note: "Arrives 10:20, about 19 km"
        lat: 11.3533
        lng: 76.7957
      - name: Dolphin's Nose
        type: hill
        note: "By auto, entry fee"
      - name: La Bella Vie
        type: food
        note: "Lunch and chai in the house from the film, then a short bus to the Coonoor bus stand"
      - name: Coimbatore
        type: bus
        note: "Bus to Coimbatore, the AC waiting hall and dinner at Valarmathi Mess"
        lat: 11.0005
        lng: 76.9667
      - name: Bengaluru
        type: train
        note: "Night train, arriving on 5 September, then a bus to HSR"
        return: true
---

Ooty sits at about 2,240 m in the Nilgiris, and this was a short trip with two friends: a hostel with a view, a lake, a waterfall, tea country and a ride on the Nilgiri Mountain Railway. We split every cost three ways in a shared sheet, and the numbers below are per person.

<div class="callout"><strong>The short version.</strong> Overnight train to Coimbatore, bus up to Ooty, two nights at Zostel with a day cab to Pykara, then the 9:15 toy train down to Coonoor and the bus and night train home. Book the toy train first.</div>

### Postcards from Ooty

{% include postcards.html label="Postcards from Ooty" items="ow-14.jpg|My hostel in Ooty;;ow-29.jpg|The toy train over the terraces;;ow-40.jpg|Ooty Lake;;ow-30.jpg|A day at Pykara Waterfall;;ow-20.jpg|Let the good things grow;;ow-38.jpg|A station on the line;;ow-35.jpg|Out of the window's wallpaper;;ow-25.jpg|Campfire nights;;ow-42.jpg|A 10 out of 10 bench;;ow-17.jpg|Oxygen, part one;;ow-27.jpg|Udhagamandalam to Coonoor;;ow-10.jpg|Kapoor and Sons, in real life" %}

### The plan

<div class="table-scroll"><table class="timetable"><thead><tr><th>Day</th><th>Where</th><th>What we did</th></tr></thead><tbody>
<tr><td>Wed 2 Sep</td><td>Coimbatore to Ooty</td><td>Auto to the bus stop, bus up to Ooty, Zostel, breakfast, Ooty Lake boating, tea factory, tea estate, Botanical Garden, De Jones Tea Bar and Moody's</td></tr>
<tr><td>Thu 3 Sep</td><td>Pykara and the pine forests</td><td>A day cab: pine forest, 6th Mile shooting point, lunch at Pykara, the falls and the lake, a second pine forest, chai, then dinner and a campfire at the Zostel</td></tr>
<tr><td>Fri 4 Sep</td><td>Coonoor and home</td><td>9:15 toy train from Ooty to Coonoor, Dolphin's Nose, La Bella Vie, bus to Coimbatore, the night train to Bengaluru (home on the morning of 5 Sep)</td></tr>
</tbody></table></div>

### Getting to Ooty

From HSR I took a cab to KSR Majestic for the overnight train to Coimbatore. At Coimbatore we took an auto from the station to the bus stop and a bus up to Ooty. The bus is the cheap way up, and the road is a slow climb.

### Where I stayed: Zostel Ooty

We stayed two nights at Zostel Ooty in a dorm. The common room has an arched window, books, board games and a balcony over the hills, and in the evening there is a campfire. The window next to my bed looked at the tea hills. The stay itself is not in my sheet, so I do not have the price, and it changes with the date and the bed. Check the Zostel app.

<div class="shots stories">
{% include shot.html file="ow-14.jpg" class="full" caption="My hostel in Ooty" %}
{% include shot.html file="ow-16.jpg" class="full" caption="Views from my window, the snooze station" %}
{% include shot.html file="ow-17.jpg" class="full" caption="The couch by the arched window" %}
{% include shot.html file="ow-20.jpg" class="full" caption="They have a little Santorini too" %}
{% include shot.html file="ow-22.jpg" class="full" caption="Cool corners, and a friendly cat" %}
{% include shot.html file="ow-21.jpg" class="full" caption="Books and games in the common room" %}
{% include shot.html file="ow-13.jpg" class="full" caption="Ferns on the terrace" %}
{% include shot.html file="ow-23.jpg" class="full" caption="The night sky from the hostel" %}
{% include shot.html file="ow-25.jpg" class="full" caption="Campfire at 12 degrees" %}
</div>

**Where it is.** The pin below searches Google Maps for the hostel, so open it for the exact address, photos and directions from the bus stand.

<iframe class="live-map no-print" title="Google map of Zostel Ooty" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Zostel+Ooty&output=embed"></iframe>

[Open Zostel Ooty in Google Maps](https://www.google.com/maps/search/?api=1&query=Zostel+Ooty){:target="_blank" rel="noopener"}

#### What the Zostel cost us, from my sheet

<div class="table-scroll"><table class="timetable"><thead><tr><th>Item</th><th>Amount</th><th>Split</th></tr></thead><tbody>
<tr><td>Bed in the dorm, 2 nights</td><td>Not in my sheet</td><td>Check the Zostel app for your dates</td></tr>
<tr><td>Auto, Ooty bus stand to the Zostel</td><td>₹250</td><td>₹83 each</td></tr>
<tr><td>Breakfast at the Zostel (day 1)</td><td>₹683</td><td>₹227 each</td></tr>
<tr><td>Dinner at the Zostel (day 2)</td><td>₹486</td><td>Two of us shared it, ₹243 each</td></tr>
<tr><td>Auto, Zostel to the Ooty railway station</td><td>₹250</td><td>₹83 each</td></tr>
</tbody></table></div>

### Day 1: lake, tea and gardens

We went by auto from the Ooty bus stand to the Zostel for breakfast and a rest. Then an auto into town for the lake: a pedal boat at Ooty Lake was ₹550 for the three of us, and a samosa at the lake. We then took an auto (₹500) for the tea factory (₹60 entry), a tea garden (₹60 entry) and the Botanical Garden (₹200 for three), with groundnuts at the garden. The day ended with tea at De Jones Tea Bar and pastries at Moody's, then an auto back to the hostel.

<div class="shots stories">
{% include shot.html file="ow-40.jpg" class="full" caption="Ooty Lake and its pedal boats" %}
{% include shot.html file="ow-46.jpg" class="full" caption="By the water" %}
{% include shot.html file="ow-47.jpg" class="full" caption="A fruit stall: carrots first" %}
{% include shot.html file="ow-48.jpg" class="full" caption="Evening light over the hills" %}
{% include shot.html file="ow-37.jpg" class="full" caption="On the grass hills" %}
{% include shot.html file="ow-35.jpg" class="full" caption="And these are views" %}
</div>

### Day 2: Pykara and the pine forests

We hired a cab for the whole day (₹2,000 for the car, about ₹667 each). It took us to a pine forest, the 6th Mile shooting point, lunch near Pykara Waterfall, the falls, the lake, a second pine forest and a chai at Cosmic Cups. The entries were small (₹100 to ₹120 each place, for the three of us), and add up, so carry change.

<div class="shots stories">
{% include shot.html file="ow-30.jpg" class="full" caption="A day at Pykara Waterfall" %}
{% include shot.html file="ow-33.jpg" class="full" caption="The falls, and sometimes we just pause" %}
{% include shot.html file="ow-39.jpg" class="full" caption="Fit check at Pykara" %}
{% include shot.html file="ow-42.jpg" class="full" caption="A 10 out of 10 bench" %}
{% include shot.html file="ow-31.jpg" class="full" caption="Looking up in the pine forest, and the window back at the Zostel" %}
{% include shot.html file="ow-49.jpg" class="full" caption="A boat on the water" %}
</div>

### Food

Breakfast at the Zostel was the best of it: parathas, an omelette, fries and corn flakes with tea, and a book on the table. The rest was cafés in town, a thali near the waterfall and chai wherever we stopped.

<div class="shots stories">
{% include shot.html file="ow-19.jpg" class="full" caption="A hotel could never: breakfast with a view and tea" %}
{% include shot.html file="ow-34.jpg" class="full" caption="Parathas, omelette and corn flakes" %}
{% include shot.html file="ow-36.jpg" class="full" caption="Good food: a south Indian thali" %}
</div>

<div class="table-scroll"><table class="timetable"><thead><tr><th>Place</th><th>Where</th><th>What we had</th><th>Map</th></tr></thead><tbody>
<tr><td>Zostel Ooty</td><td>Ooty</td><td>Breakfast and dinner</td><td><a href="https://www.google.com/maps/search/?api=1&query=Zostel+Ooty" target="_blank" rel="noopener">Maps</a></td></tr>
<tr><td>De Jones Tea Bar</td><td>Ooty</td><td>Tea</td><td><a href="https://www.google.com/maps/search/?api=1&query=De+Jones+Tea+Bar+Ooty" target="_blank" rel="noopener">Maps</a></td></tr>
<tr><td>Moody's</td><td>Ooty</td><td>Strawberry chocolate, a croissant and puffs</td><td><a href="https://www.google.com/maps/search/?api=1&query=Moody%27s+Ooty" target="_blank" rel="noopener">Maps</a></td></tr>
<tr><td>Cosmic Cups</td><td>On the Pykara day</td><td>Chai</td><td><a href="https://www.google.com/maps/search/?api=1&query=Cosmic+Cups+Ooty" target="_blank" rel="noopener">Maps</a></td></tr>
<tr><td>La Bella Vie</td><td>Coonoor</td><td>Lunch and chai, about ₹1,840 for the three of us</td><td><a href="https://www.google.com/maps/search/?api=1&query=La+Bella+Vie+Coonoor" target="_blank" rel="noopener">Maps</a></td></tr>
<tr><td>Valarmathi Mess</td><td>Coimbatore railway station</td><td>Dinner before the night train</td><td><a href="https://www.google.com/maps/search/?api=1&query=Valarmathi+Mess+Coimbatore" target="_blank" rel="noopener">Maps</a></td></tr>
</tbody></table></div>

### The Nilgiri Mountain Railway: Ooty to Coonoor

The Nilgiri Mountain Railway is the toy train that climbs between Mettupalayam, Coonoor and Ooty. You do not have to ride the whole line. The easy way is the Ooty (UAM) to Coonoor (ONR) stretch, which is about 19 km and takes a bit over an hour. We took the 9:15 morning train, and it reached Coonoor at 10:20 on our ticket. Timings change, so check IRCTC before you go.

<div class="callout"><strong>What the ticket says.</strong> Train 56139, UAM ONR Pass, from Udagamandalam (Ooty) to Coonoor on 4 September 2026. Departs 9:15, arrives 10:20. Second sitting (2S), General quota, 19 km. The total was ₹499.05 for the three of us: ₹480 fare, ₹17.70 IRCTC convenience fee and ₹1.35 insurance.</div>

<div class="shots one">
{% include shot.html file="ers-ticket.jpg" class="full" caption="My IRCTC e-ticket (PNR, names, transaction ID and QR code hidden)" %}
</div>

I booked on 29 July for 4 September, so about five weeks ahead, and all three of us got confirmed seats in the same coach, one of them by the window. The IRCTC fee is charged once per e-ticket, not per passenger, so one person booking for the group saves a little.

### How to book it on IRCTC

1. **Log in.** Open the IRCTC Rail Connect app or irctc.co.in and sign in. Make an account first if you do not have one, and finish the verification it asks for.
2. **Search.** Put "UDAGAMANDALAM (UAM)" in From and "COONOOR (ONR)" in To. Pick the date, the class and the General quota, and search.
3. **Pick the train.** Look for the services between UAM and ONR (mine was 56139, "UAM ONR PASS"). Check that second sitting (2S) shows seats, and tap Book Now.
4. **Add the passengers.** Enter each name, age and gender, and choose a seat preference such as window side. Add a mobile number you can reach.
5. **Review and pay.** Check the fare and the optional insurance, then pay by UPI, card or net banking. The ticket says payment gateway charges are extra.
6. **Keep the ticket.** The ERS and the confirmation SMS come in at once, and the ticket stays in your account under booked tickets. Save the ERS as a PDF and carry the original ID of the person who booked.

If the train is full or you cannot plan ahead, ask at the Ooty railway station. Some services have unreserved tickets sold at the counter. Book early for weekends and holidays.

### The ride

It is slow, and that is the point. The train rolls through eucalyptus woods and tea estates and past small stations, with the coaches rocking a little, so grab a window seat. The fare on my ticket was far less than a taxi, and the ride is the sight, not the way to get anywhere fast.

<div class="shots stories">
{% include shot.html file="ow-27.jpg" class="full" caption="Udhagamandalam to Coonoor, in the window" %}
{% include shot.html file="ow-38.jpg" class="full" caption="A little station on the line" %}
{% include shot.html file="ow-43.jpg" class="full" caption="The platform and the train" %}
{% include shot.html file="ow-32.jpg" class="full" caption="Out of the window, trees and track" %}
{% include shot.html file="ow-44.jpg" class="full" caption="See you again" %}
{% include shot.html file="ow-41.jpg" class="full" caption="The old engine, and a tin cup of tea" %}
</div>

### Coonoor and back

From Coonoor we took an auto for the rest of the day (₹1,200 for the three of us). It went to Dolphin's Nose for the view (₹120 entry), then La Bella Vie for lunch and chai. We took a short bus (₹14 in all) to the Coonoor bus stand, and a bus to Coimbatore (₹183 for three). If you do not want to ride back by train, the bus between Ooty and Coonoor is far cheaper and takes about 45 to 60 minutes. My suggestion is the same: take the toy train one way and come back by road.

La Bella Vie is the colonial house that stood in for the Kapoor and Sons family home in the film. We took photos of the film frames next to the real house.

<div class="shots stories">
{% include shot.html file="ow-2.jpg" class="full" caption="The Kapoor and Sons home, since 1921" %}
{% include shot.html file="ow-4.jpg" class="full" caption="The house: in real life, and in the film" %}
{% include shot.html file="ow-5.jpg" class="full" caption="The tea-garden view" %}
{% include shot.html file="ow-7.jpg" class="full" caption="Rains kept us in, as in the film" %}
{% include shot.html file="ow-8.jpg" class="full" caption="There were much prettier flowers in real life" %}
{% include shot.html file="ow-11.jpg" class="full" caption="The veranda, and the pasta" %}
</div>

From Coimbatore we waited in the AC waiting hall (₹150 for three), had dinner at Valarmathi Mess and took the night train home. On the morning of 5 September a bus took us from the Bengaluru railway station to HSR.

<div class="shots stories">
{% include shot.html file="ow-45.jpg" class="full" caption="Adrak khayega?" %}
{% include shot.html file="ow-26.jpg" class="full" caption="See you again" %}
{% include shot.html file="ow-28.jpg" class="full" caption="Somedays I miss Ooty like it was a person" %}
</div>

### What I'd add to this plan

<div class="callout"><strong>A few things worth adding</strong>, from reading around rather than from my own trip, so check them locally:
<ul>
<li><strong>Sim's Park and Lamb's Rock</strong> in Coonoor, if you have spare time between the train and the bus.</li>
<li><strong>Doddabetta Peak</strong>, the highest point in the Nilgiris, is an easy half-day from Ooty.</li>
<li><strong>Pack warm.</strong> Nights are cold in the hills (12 degrees with wind for us), so take a proper jacket.</li>
<li><strong>Book the toy train and the Zostel early</strong> for weekends and school holidays.</li>
<li><strong>Prices drift.</strong> Treat my costs as a ballpark for September 2026.</li>
</ul></div>
