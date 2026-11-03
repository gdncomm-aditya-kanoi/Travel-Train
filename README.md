# Travel Train — by Aditya Kanoi

A travel journal for trips across India: expenses, things to do and skip,
day planners with maps, and Instagram posts. Hosted free on GitHub Pages.

## 1. Put it online (one time, ~5 minutes)

1. Create a GitHub account if you don't have one.
2. Create a new **public** repository.
   - Name it `<your-username>.github.io` for the address `https://<your-username>.github.io`
   - Or any name, e.g. `travel-train` → then open `_config.yml` and set `baseurl: "/travel-train"`
3. On the repo page click **Add file → Upload files**, drag in everything from this
   folder (including the hidden `.pages.yml`), and click **Commit changes**.
4. Go to **Settings → Pages**. Under *Build and deployment* choose
   **Deploy from a branch**, branch **main**, folder **/ (root)**, then **Save**.
5. Wait 1–2 minutes. Your site link appears at the top of the Pages settings.

Every time you change a file on GitHub, the site rebuilds by itself in about a minute.

## 2. Set your Instagram

Open `_data/instagram.yml` and edit it on GitHub (pencil icon):

```yaml
handle: your_real_handle
posts:
  - https://www.instagram.com/p/XXXXXXXXXXX/
  - https://www.instagram.com/reel/XXXXXXXXXXX/
```

Get a link in Instagram with **••• → Copy link**. Posts must be public.
They show as embedded posts; tapping one opens Instagram.

## 3. Add a journey

### Option A — on GitHub directly
1. **Photos:** open `assets/images/`, click **Add file → Create new file**, type
   `goa/.gitkeep` to make a folder, commit. Then open that folder and
   **Add file → Upload files** to drop in your photos (e.g. `cover.jpg`, `01.jpg`).
   Keep each photo under ~1 MB (resize on your phone or with squoosh.app).
2. **The post:** open `_trips/`, copy everything in `thanjavur.md`, then
   **Add file → Create new file**, name it `goa.md` (the name becomes the link:
   `/trips/goa/`), paste, and change the details.
3. Commit. Done.

### Option B — with a simple editor (recommended)
Go to **https://pagescms.org**, sign in with GitHub and open this repository.
You'll get forms for journeys (photo upload, expenses, day planner, Instagram links)
and everything saves into the repo for you. The forms come from `.pages.yml`.

## 4. The day planner and maps

Each day in a trip file looks like this:

```yaml
days:
  - title: The Chola temple loop from Thanjavur
    route: https://maps.app.goo.gl/T41wqWPxEcTfPfqJ9   # your Google Maps link
    stops:
      - name: Thanjavur
        note: Start
        lat: 10.787719
        lng: 79.1384288
      - name: New Bus Stand, Thanjavur
        lat: 10.7571929
        lng: 79.1125674
        return: true    # draws this last leg as a dotted "way back" line
```

- The site draws the little engraved map from the `lat`/`lng` of each stop.
- To get them: in Google Maps, **right-click** (or long-press on phone) a place —
  the first line is `lat, lng`; tap it to copy.
- Days with no stops show "Stops for this day are coming soon".
- **Map PDF:** every trip page has *Print or save as PDF*, which prints just the
  planner with all days. To offer your own PDF too, upload it to `assets/maps/`
  and set `map_pdf: /assets/maps/your-file.pdf` in the trip.

## 5. Money

Write amounts as plain numbers (`amount: 1850`). The site adds the total and
shows it the Indian way (₹1,25,000). Leave `0` to show a dash.

## Folder map

```
_config.yml            site settings (title, baseurl)
_data/instagram.yml    your handle + home-page posts
_trips/*.md            one file per journey
assets/images/<trip>/  photos
assets/maps/           optional map PDFs
_layouts/, _includes/  page templates (no need to touch)
assets/css/style.css   colours and fonts — change --ink to re-colour the site
assets/js/main.js      maps, tabs, state filter, Instagram loader
```

## Preview on your computer (optional)

Install Ruby, then: `gem install bundler jekyll` and run `jekyll serve` in this
folder. Open http://localhost:4000.
