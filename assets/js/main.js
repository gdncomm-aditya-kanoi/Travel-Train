/* Travel Train — small helpers, no libraries */
(function () {
  "use strict";

  /* Small engraved symbols (20 x 20 box) used on the maps and in the stop list */
  var ICONS = {
    home: '<path d="M3 10 L10 4 L17 10 M5 9 V16 H15 V9 M8.5 16 V12 H11.5 V16"/>',
    temple: '<path d="M4 16 H16 M6 16 V13 H14 V16 M7.5 13 V10 H12.5 V13 M8.7 10 V7 H11.3 V10 M9.6 7 V4 H10.4 V7"/>',
    chariot: '<path d="M4 12 H16 V14.5 H4 Z M6 12 V9 H14 V12 M8 9 V6.5 H12 V9 M10 6.5 V4"/><circle cx="6.5" cy="16.3" r="1.9"/><circle cx="13.5" cy="16.3" r="1.9"/>',
    palace: '<path d="M3 16 H17 M4 16 V9 M16 16 V9 M4 9 L10 4 L16 9 M8 16 V12.5 Q10 9.5 12 12.5 V16"/>',
    stable: '<path d="M3 16 H17 M4 16 V12 Q6 8 8 12 V16 M8 16 V12 Q10 8 12 12 V16 M12 16 V12 Q14 8 16 12 V16"/>',
    bath: '<path d="M3 5 H17 V16 H3 Z M5 9 q1.5 -1.5 3 0 t3 0 t3 0 M5 13 q1.5 -1.5 3 0 t3 0 t3 0"/>',
    hill: '<path d="M2 16 L8 6 L11.5 11 L13.5 8.5 L18 16 Z"/>',
    bus: '<rect x="3" y="4" width="14" height="10" rx="2"/><path d="M3 9 H17 M6 17 V14 M14 17 V14"/>',
    town: '<path d="M3 16 V8 H8 V16 M8 16 V5 H13 V16 M13 16 V10 H17 V16 M2 16 H18"/>',
    beach: '<path d="M2 16 H18 M3 13 q1.5 -1.5 3 0 t3 0 t3 0 t3 0 M10 11 V5 M10 5 q-4 0 -6 3 M10 5 q4 0 6 3"/>',
    waterfall: '<path d="M3 5 H17 M7 5 Q6 10 7 14 M10 5 Q9 11 10 15 M13 5 Q12 10 13 14 M3 17 q2.5 -2 5 0 t5 0 t4 0"/>',
    fort: '<path d="M3 16 H17 M4 16 V7 H7 V9 H9 V7 H11 V9 H13 V7 H16 V16 M9 16 V12 H11 V16"/>',
    train: '<rect x="4" y="3" width="12" height="11" rx="2"/><path d="M4 9 H16 M7 17 L9 14 M13 17 L11 14"/>',
    cave: '<path d="M2 16 L5 7 L10 4 L15 7 L18 16 Z M7.5 16 V12 Q10 8 12.5 12 V16"/>'
  };
  function icon(type, x, y, size) {
    if (!ICONS[type]) return "";
    return '<g transform="translate(' + x.toFixed(1) + " " + y.toFixed(1) + ") scale(" + (size / 20).toFixed(3) + ')" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">' + ICONS[type] + "</g>";
  }
  document.querySelectorAll(".stop-ico").forEach(function (el) {
    var t = el.getAttribute("data-ico");
    if (ICONS[t]) el.innerHTML = '<svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">' + ICONS[t] + "</svg>";
  });


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
    var W = 600, H = 480, PAD_X = 80, PAD_Y = 70;
    var id = "dm" + idx;
    var stops = (day.stops || []).filter(function (s) {
      return isFinite(Number(s.lat)) && isFinite(Number(s.lng)) && s.lat !== null && s.lng !== null;
    });

    var out = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' +
      esc(title + (stops.length ? ": " + stops.map(function (s) { return s.name; }).join(" to ") : ", stops not added yet")) + '">' +
      "<defs>" +
      '<pattern id="' + id + '-dots" width="12" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="0.9" fill="currentColor"/><circle cx="8" cy="6.5" r="0.7" fill="currentColor"/></pattern>' +
      "</defs>" +
      '<rect width="' + W + '" height="' + H + '" fill="url(#' + id + '-dots)" opacity="0.3"/>' +
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
      return { x: offX + (Number(s.lng) - minLng) * kx * scale, y: offY + (maxLat - Number(s.lat)) * ky * scale, s: s };
    });

    /* Stops too close to tell apart get pushed apart (exact repeats are left alone) */
    pts.forEach(function (p, n) {
      for (var pass = 0; pass < 6; pass++) {
        var moved = false;
        for (var j = 0; j < n; j++) {
          var dx = p.x - pts[j].x, dy = p.y - pts[j].y, d = Math.hypot(dx, dy);
          if (d >= 6 && d < 34) { p.x = pts[j].x + dx / d * 34; p.y = pts[j].y + dy / d * 34; moved = true; }
        }
        if (!moved) break;
      }
    });
    var twin = pts.map(function (p, n) {
      for (var j = 0; j < n; j++) if (Math.hypot(pts[j].x - p.x, pts[j].y - p.y) < 6) return j;
      return -1;
    });

    /* Legs. A way-back leg bows to whichever side keeps it furthest from the other stops, so it never runs over the outward route. */
    var legs = [], samples = [];
    for (var i = 1; i < pts.length; i++) {
      var a = pts[i - 1], b = pts[i], back = !!b.s.return;
      var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2, len = Math.hypot(b.x - a.x, b.y - a.y) || 1;
      var cx = mx, cy = my;
      /* Bow a leg (always the way-back ones, and any leg that would graze another stop) to the side that keeps it clear */
      var graze = false;
      pts.forEach(function (q, k) {
        if (k === i || k === i - 1) return;
        var t = Math.max(0, Math.min(1, ((q.x - a.x) * (b.x - a.x) + (q.y - a.y) * (b.y - a.y)) / (len * len)));
        if (Math.hypot(a.x + t * (b.x - a.x) - q.x, a.y + t * (b.y - a.y) - q.y) < 24) graze = true;
      });
      if (back || graze) {
        var nx = -(b.y - a.y) / len, ny = (b.x - a.x) / len, bow = Math.max(len * (back ? 0.42 : 0.3), 36), best = -1;
        [1, -1].forEach(function (sg) {
          var qx = mx + nx * bow * sg, qy = my + ny * bow * sg, m = 1e9;
          if (qx < 14 || qx > W - 14 || qy < 14 || qy > H - 60) return;
          pts.forEach(function (q, k) { if (k !== i && k !== i - 1) m = Math.min(m, Math.hypot(q.x - qx, q.y - qy)); });
          if (m > best) { best = m; cx = qx; cy = qy; }
        });
      }
      legs.push({ a: a, b: b, cx: cx, cy: cy, back: back, len: len });
      for (var t = 0.08; t < 0.95; t += 0.07) {
        samples.push({ x: (1 - t) * (1 - t) * a.x + 2 * (1 - t) * t * cx + t * t * b.x, y: (1 - t) * (1 - t) * a.y + 2 * (1 - t) * t * cy + t * t * b.y });
      }
    }

    /* Route lines: a pale halo underneath so the dashes stay readable over the dot texture, plus a direction arrow */
    legs.forEach(function (l) {
      var d = "M" + l.a.x.toFixed(1) + " " + l.a.y.toFixed(1) + " Q" + l.cx.toFixed(1) + " " + l.cy.toFixed(1) + " " + l.b.x.toFixed(1) + " " + l.b.y.toFixed(1);
      out += '<path d="' + d + '" fill="none" stroke="#F7F1E4" stroke-width="7" stroke-linecap="round"/>' +
        '<path d="' + d + '" fill="none" stroke="currentColor" ' +
        (l.back ? 'stroke-width="2.2" stroke-dasharray="1 6" stroke-linecap="round"' : 'stroke-width="2.6" stroke-dasharray="9 6"') + "/>";
      if (l.len > 46) {
        var t = 0.55, px = (1 - t) * (1 - t) * l.a.x + 2 * (1 - t) * t * l.cx + t * t * l.b.x, py = (1 - t) * (1 - t) * l.a.y + 2 * (1 - t) * t * l.cy + t * t * l.b.y;
        var tx = 2 * (1 - t) * (l.cx - l.a.x) + 2 * t * (l.b.x - l.cx), ty = 2 * (1 - t) * (l.cy - l.a.y) + 2 * t * (l.b.y - l.cy);
        out += '<path transform="translate(' + px.toFixed(1) + " " + py.toFixed(1) + ") rotate(" + (Math.atan2(ty, tx) * 180 / Math.PI).toFixed(1) + ')" d="M7 0 L-5 -5 L-5 5 Z" fill="currentColor" stroke="#F7F1E4" stroke-width="2" stroke-linejoin="round"/>';
      }
    });

    /* Markers. A return stop that sits on an earlier stop becomes a ring round it. */
    pts.forEach(function (p, n) {
      if (twin[n] >= 0) {
        out += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="19" fill="none" stroke="currentColor" stroke-width="2"/>';
        return;
      }
      var hollow = !!p.s.return;
      out += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="12" ' +
        (hollow ? 'fill="#F7F1E4" stroke="currentColor" stroke-width="2.5"' : 'fill="currentColor" stroke="#F7F1E4" stroke-width="3"') + "/>" +
        '<text x="' + p.x.toFixed(1) + '" y="' + (p.y + 4.5).toFixed(1) + '" text-anchor="middle" class="m-num' + (hollow ? " m-num-hollow" : "") + '">' + (n + 1) + "</text>";
    });

    /* Labels: try 8 positions round each marker and keep the one that touches the fewest lines, markers and other labels */
    var boxes = [{ x: 520, y: 12, w: 70, h: 66 }, { x: W - 170, y: 418, w: 160, h: 50 }];
    var hit = function (r, b, pad) { return r.x < b.x + b.w + pad && r.x + r.w + pad > b.x && r.y < b.y + b.h + pad && r.y + r.h + pad > b.y; };
    pts.forEach(function (p, n) {
      if (twin[n] >= 0) return;
      var ico = ICONS[p.s.type] ? 24 : 0, w = String(p.s.name).length * 9.2 + ico + 8, h = 22;
      var cands = [[18, -h / 2], [-18 - w, -h / 2], [-w / 2, -h - 16], [-w / 2, 16], [18, -h - 8], [-18 - w, -h - 8], [18, 8], [-18 - w, 8], [18, -h - 24], [-18 - w, -h - 24], [18, 24], [-18 - w, 24], [-w / 2, -h - 34], [-w / 2, 34]];
      var best = null;
      cands.forEach(function (c, ci) {
        var r = { x: p.x + c[0], y: p.y + c[1], w: w, h: h }, score = ci * 0.8 + (ci >= 8 ? 12 : 0);
        if (r.x < 6 || r.y < 6 || r.x + r.w > W - 6 || r.y + r.h > H - 6) score += 100;
        pts.forEach(function (q, k) { if (twin[k] < 0 && q.x > r.x - 15 && q.x < r.x + r.w + 15 && q.y > r.y - 15 && q.y < r.y + r.h + 15) score += 40; });
        boxes.forEach(function (bx) { if (hit(r, bx, 4)) score += 60; });
        samples.forEach(function (sp) { if (sp.x > r.x - 4 && sp.x < r.x + r.w + 4 && sp.y > r.y - 4 && sp.y < r.y + r.h + 4) score += 22; });
        if (!best || score < best.score) best = { r: r, score: score, far: ci >= 8 };
      });
      boxes.push(best.r);
      if (best.far) {
        var lx = Math.max(best.r.x, Math.min(p.x, best.r.x + best.r.w)), ly = Math.max(best.r.y, Math.min(p.y, best.r.y + best.r.h));
        var ld = Math.hypot(lx - p.x, ly - p.y) || 1;
        out += '<line x1="' + (p.x + (lx - p.x) / ld * 13).toFixed(1) + '" y1="' + (p.y + (ly - p.y) / ld * 13).toFixed(1) + '" x2="' + lx.toFixed(1) + '" y2="' + ly.toFixed(1) + '" stroke="currentColor" stroke-width="1"/>';
      }
      out += icon(p.s.type, best.r.x + 1, best.r.y + 1, 20) +
        '<text x="' + (best.r.x + ico + 2).toFixed(1) + '" y="' + (best.r.y + 16).toFixed(1) + '" class="m-label">' + esc(p.s.name) + "</text>";
    });

    /* Scale bar with a round number of km */
    var nice = [1, 2, 5, 10, 20, 50, 100, 200];
    var km = nice[0];
    for (var k = 0; k < nice.length; k++) { if (nice[k] * scale <= 120) km = nice[k]; }
    var len2 = km * scale, x2 = W - 30, x1 = x2 - len2;
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
