---
title: Thanjavur
state: Tamil Nadu
date: 2026-01-15            # used to sort trips, newest first
summary: "[One line on what this trip was about — the mood, the reason you went.]"
month: "[Month YYYY]"
days_count: 3
best_season: "[Months]"

# Photos: upload to assets/images/thanjavur/ then put the paths here.
# Leave cover as "" to show a placeholder.
cover: ""                   # e.g. /assets/images/thanjavur/cover.jpg
gallery: []
#  - /assets/images/thanjavur/01.jpg
#  - /assets/images/thanjavur/02.jpg

# Optional: a PDF map people can download (upload it to assets/maps/)
map_pdf: ""                 # e.g. /assets/maps/thanjavur-map.pdf

# Instagram posts or reels from this trip
instagram: []
#  - https://www.instagram.com/reel/XXXXXXXXXXX/

expenses:                   # amounts in rupees, numbers only
  - category: Getting there
    note: "[Train / bus / flight, class]"
    amount: 0
  - category: Stay
    note: "[Hostel / hotel, nights]"
    amount: 0
  - category: Food
    note: "[Per day roughly]"
    amount: 0
  - category: Local transport
    note: "[Auto, scooter rental, cabs]"
    amount: 0
  - category: Activities & entry
    note: "[Tickets, guides]"
    amount: 0

things_to_do:
  - "[Something worth doing]"
  - "[A place to eat]"
things_to_skip:
  - "[An overrated spot]"
  - "[A scam to watch for]"

details:
  - label: Nearest station
    value: "[Station name]"
  - label: Nearest airport
    value: "[Airport name]"
  - label: Where I stayed
    value: "[Stay name, area]"
  - label: Budget level
    value: "[Backpacker / mid / comfort]"

# Day planner. Each stop needs lat/lng to appear on the map.
# Get them in Google Maps: right-click a place → click the numbers to copy.
days:
  - title: "[Title of the day]"
    route: https://maps.app.goo.gl/we7XqRUqWUHiatXGA
    stops: []
#      - name: First stop
#        note: what you did
#        lat: 10.78
#        lng: 79.13
  - title: The Chola temple loop from Thanjavur
    route: https://maps.app.goo.gl/T41wqWPxEcTfPfqJ9
    stops:
      - name: Thanjavur
        note: Start
        lat: 10.787719
        lng: 79.1384288
      - name: Kumbakonam
        note: "[What you did here]"
        lat: 10.9601852
        lng: 79.3844976
      - name: Gangaikonda Cholapuram
        note: Brihadeeswarar (Shiva) Temple
        lat: 11.2063794
        lng: 79.4494846
      - name: New Bus Stand, Thanjavur
        note: Back to base
        lat: 10.7571929
        lng: 79.1125674
        return: true          # draws the way back as a dotted line
  - title: "[Title of the day]"
    route: ""
    stops: []
---

[Write the story of the trip here — how you got there, the first impression, the day that stood out.]

[A second paragraph, if you have more to say.]
