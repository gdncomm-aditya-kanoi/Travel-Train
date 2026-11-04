/* Travel Train — small helpers, no libraries */
(function () {
  "use strict";

  /* ₹ amounts in Indian grouping: 125000 → ₹1,25,000 */
  document.querySelectorAll("[data-inr]").forEach(function (el) {
    var n = Number(el.getAttribute("data-inr"));
    if (!isNaN(n)) el.textContent = "₹" + n.toLocaleString("en-IN");
  });

  /* State filter on the home page */
  var chips = document.querySelectorAll(".chip[data-filter]");
  var cards = document.querySelectorAll("#trip-grid .trip-card");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var f = chip.getAttribute("data-filter");
      chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
      cards.forEach(function (card) {
        card.hidden = f !== "all" && card.getAttribute("data-state") !== f;
      });
      var grid = document.getElementById("journeys");
      if (grid) grid.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  /* Day planner tabs (arrow keys move between days) */
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".day-tabs [role=tab]"));
  function selectTab(tab) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { selectTab(tab); });
    tab.addEventListener("keydown", function (e) {
      var next = null;
      if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
      if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (next) { e.preventDefault(); selectTab(next); next.focus(); }
    });
  });

  /* Print / save the planner as a PDF */
  var printBtn = document.querySelector("[data-print-map]");
  if (printBtn) {
    printBtn.addEventListener("click", function () {
      document.body.classList.add("print-map");
      window.print();
    });
    window.addEventListener("afterprint", function () {
      document.body.classList.remove("print-map");
    });
  }

  /* Day maps, drawn in the engraved style from each stop's lat/lng */
  var dataEl = document.getElementById("trip-days");
  if (dataEl) {
    var days = [];
    try { days = JSON.parse(dataEl.textContent) || []; } catch (e) { days = []; }
    document.querySelectorAll(".day-map").forEach(function (box) {
      var day = days[Number(box.getAttribute("data-day"))] || {};
      box.innerHTML = drawMap(day, box.getAttribute("data-title"), Number(box.getAttribute("data-day"))) + liveMap(day);
    });
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  /* A real, zoomable Google map of the same stops (no key needed) */
  function liveMap(day) {
    var st = (day.stops || []).filter(function (s) { return isFinite(Number(s.lat)) && isFinite(Number(s.lng)) && s.lat !== null; });
    if (st.length < 2) return "";
    var pt = function (s) { return Number(s.lat) + "," + Number(s.lng); };
    var src = "https://maps.google.com/maps?output=embed&saddr=" + encodeURIComponent(pt(st[0])) +
      "&daddr=" + st.slice(1).map(function (s) { return encodeURIComponent(pt(s)); }).join("+to:");
    return '<iframe class="live-map no-print" title="Google map of this day" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="' + src + '"></iframe>';
  }

  function drawMap(day, title, idx) {
    var W = 600, H = 480, PAD_X = 90, PAD_Y = 70;
    var id = "dm" + idx;
    var stops = (day.stops || []).filter(function (s) {
      return isFinite(Number(s.lat)) && isFinite(Number(s.lng)) && s.lat !== null && s.lng !== null;
    });

    var out = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' +
      esc(title + (stops.length ? ": " + stops.map(function (s) { return s.name; }).join(" to ") : ", stops not added yet")) + '">' +
      "<defs>" +
      '<pattern id="' + id + '-dots" width="12" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="0.9" fill="currentColor"/><circle cx="8" cy="6.5" r="0.7" fill="currentColor"/></pattern>' +
      "</defs>" +
      '<rect width="' + W + '" height="' + H + '" fill="url(#' + id + '-dots)" opacity="0.35"/>' +
      '<path d="M552 26 L560 54 L552 48 L544 54 Z" fill="currentColor"/>' +
      '<text x="552" y="72" text-anchor="middle" class="m-small">N</text>';

    if (!stops.length) {
      out += '<rect x="150" y="212" width="300" height="56" rx="28" fill="#F7F1E4" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 5"/>' +
        '<text x="300" y="246" text-anchor="middle" class="m-note">Stops for this day are coming soon</text>';
      return out + "</svg>";
    }

    /* Equal-scale projection in kilometres, fitted to the frame */
    var lat0 = stops.reduce(function (a, s) { return a + Number(s.lat); }, 0) / stops.length;
    var kx = Math.cos(lat0 * Math.PI / 180) * 111.32, ky = 110.57;
    var lngs = stops.map(function (s) { return Number(s.lng); });
    var lats = stops.map(function (s) { return Number(s.lat); });
    var minLng = Math.min.apply(null, lngs), maxLat = Math.max.apply(null, lats);
    var spanX = Math.max((Math.max.apply(null, lngs) - minLng) * kx, 4);
    var spanY = Math.max((maxLat - Math.min.apply(null, lats)) * ky, 4);
    var scale = Math.min((W - 2 * PAD_X) / spanX, (H - 2 * PAD_Y) / spanY);
    var offX = (W - spanX * scale) / 2, offY = (H - spanY * scale) / 2;
    var pts = stops.map(function (s) {
      return {
        x: offX + (Number(s.lng) - minLng) * kx * scale,
        y: offY + (maxLat - Number(s.lat)) * ky * scale,
        s: s
      };
    });

    /* Stops that are too close to tell apart get pushed apart (exact repeats are left alone) */
    pts.forEach(function (p, n) {
      for (var pass = 0; pass < 6; pass++) {
        var moved = false;
        for (var j = 0; j < n; j++) {
          var dx = p.x - pts[j].x, dy = p.y - pts[j].y, d = Math.hypot(dx, dy);
          if (d >= 6 && d < 28) { p.x = pts[j].x + dx / d * 28; p.y = pts[j].y + dy / d * 28; moved = true; }
        }
        if (!moved) break;
      }
    });

    /* Route: dashed, dotted for a leg marked "return" */
    for (var i = 1; i < pts.length; i++) {
      var a = pts[i - 1], b = pts[i];
      var back = !!b.s.return;
      out += '<path d="M' + a.x.toFixed(1) + " " + a.y.toFixed(1) + " L" + b.x.toFixed(1) + " " + b.y.toFixed(1) + '" fill="none" stroke="currentColor" ' +
        (back ? 'stroke-width="2" stroke-dasharray="1 6" stroke-linecap="round"' : 'stroke-width="2.5" stroke-dasharray="9 6"') + "/>";
    }

    /* Markers and labels. A return stop on top of an earlier stop becomes a ring round it. */
    var placed = [];
    pts.forEach(function (p, n) {
      var twin = null;
      for (var j = 0; j < n; j++) {
        if (Math.hypot(pts[j].x - p.x, pts[j].y - p.y) < 6) { twin = pts[j]; break; }
      }
      if (twin) {
        out += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="18" fill="none" stroke="currentColor" stroke-width="2"/>';
        return;
      }
      var hollow = !!p.s.return;
      out += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="12" ' +
        (hollow ? 'fill="#F7F1E4" stroke="currentColor" stroke-width="2.5"' : 'fill="currentColor" stroke="#F7F1E4" stroke-width="3"') + "/>" +
        '<text x="' + p.x.toFixed(1) + '" y="' + (p.y + 4.5).toFixed(1) + '" text-anchor="middle" class="m-num' + (hollow ? " m-num-hollow" : "") + '">' + (n + 1) + "</text>";

      /* Label goes on whichever side has room, then moves down until it is clear of other labels */
      var right = p.x < W / 2 + 40;
      var lx = right ? p.x + 20 : p.x - 20;
      var ly = p.y + 6;
      var w = String(p.s.name).length * 8.5;
      var tries = 0;
      var clash = function () {
        return placed.some(function (q) {
          var overlapX = right === q.right ? Math.abs(q.x - lx) < Math.max(w, q.w) : Math.abs((right ? lx + w / 2 : lx - w / 2) - (q.right ? q.x + q.w / 2 : q.x - q.w / 2)) < (w + q.w) / 2;
          return overlapX && Math.abs(q.y - ly) < 20;
        });
      };
      while (clash() && tries++ < 8) ly += 22;
      ly = Math.min(ly, H - 40);
      placed.push({ x: lx, y: ly, w: w, right: right });
      out += '<text x="' + lx.toFixed(1) + '" y="' + ly.toFixed(1) + '" text-anchor="' + (right ? "start" : "end") + '" class="m-label">' + esc(p.s.name) + "</text>";
    });

    /* Scale bar with a round number of km */
    var nice = [1, 2, 5, 10, 20, 50, 100, 200];
    var km = nice[0];
    for (var k = 0; k < nice.length; k++) { if (nice[k] * scale <= 120) km = nice[k]; }
    var len = km * scale, x2 = W - 30, x1 = x2 - len;
    out += '<line x1="' + x1.toFixed(1) + '" y1="452" x2="' + x2 + '" y2="452" stroke="currentColor" stroke-width="2"/>' +
      '<line x1="' + x1.toFixed(1) + '" y1="446" x2="' + x1.toFixed(1) + '" y2="458" stroke="currentColor" stroke-width="2"/>' +
      '<line x1="' + x2 + '" y1="446" x2="' + x2 + '" y2="458" stroke="currentColor" stroke-width="2"/>' +
      '<text x="' + ((x1 + x2) / 2).toFixed(1) + '" y="440" text-anchor="middle" class="m-small">' + km + " km</text>";

    return out + "</svg>";
  }

  /* Instagram embeds: load Instagram's script only when a page has posts */
  if (document.querySelector(".instagram-media")) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.instagram.com/embed.js";
    document.body.appendChild(s);
  }
})();
