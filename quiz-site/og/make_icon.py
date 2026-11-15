#!/usr/bin/env python3
"""Generate the Pixelbolt recipes for the CCAR app icon.

Writes icon.pixel.json (32x32, rounded tile: favicon / 192 / 512 icons) and
icon-maskable.pixel.json (64x64 full-bleed, same drawing offset by 16px so it
stays inside the maskable safe zone). Render with Pixelbolt:

  node bin/pixelbolt.js render quiz-site/og/icon.pixel.json --out <dir> --scale <1|6|16>
  node bin/pixelbolt.js render quiz-site/og/icon-maskable.pixel.json --out <dir> --scale <3|8>   (192 / 512)
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE = {
    "b": "#2F5BB7",  # blueprint blue (tile)
    "h": "#3E6CCB",  # top highlight
    "d": "#244A99",  # bottom shade
    "g": "#6F93DD",  # blueprint grid dots
    "n": "#102A43",  # navy outlines
    "w": "#FFFFFF",  # connectors, component boxes
    "e": "#C9D6EE",  # placeholder "text" lines
    "a": "#FFB81C",  # orchestrator box
    "o": "#E09A00",  # orchestrator shade
}


def diagram(ox=0, oy=0):
    """The architecture diagram: an orchestrator box wired to two components."""
    def r(x, y, w, h, c):
        return {"op": "rect", "x": x + ox, "y": y + oy, "w": w, "h": h, "color": c, "filled": True}
    return [
        # connectors (white "ink" on the blueprint)
        r(15, 13, 2, 4, "w"), r(7, 16, 18, 2, "w"), r(7, 18, 2, 2, "w"), r(23, 18, 2, 2, "w"),
        # orchestrator (amber, navy outline)
        r(10, 5, 12, 8, "n"), r(11, 6, 10, 6, "a"), r(11, 11, 10, 1, "o"), r(13, 8, 6, 1, "n"),
        # components (white, navy outline) with two "text" lines each
        r(3, 20, 11, 8, "n"), r(4, 21, 9, 6, "w"), r(5, 23, 6, 1, "e"), r(5, 25, 4, 1, "e"),
        r(18, 20, 11, 8, "n"), r(19, 21, 9, 6, "w"), r(20, 23, 6, 1, "e"), r(20, 25, 4, 1, "e"),
    ]


def grid_dots(size, step=4, start=2):
    return [{"op": "pixel", "x": x, "y": y, "color": "g"}
            for y in range(start, size, step) for x in range(start, size, step)]


def rounded_tile():
    ops = [{"op": "rect", "x": 0, "y": 0, "w": 32, "h": 32, "color": "b", "filled": True}]
    ops += grid_dots(32)
    ops += [{"op": "rect", "x": 0, "y": 0, "w": 32, "h": 2, "color": "h", "filled": True},
            {"op": "rect", "x": 0, "y": 29, "w": 32, "h": 3, "color": "d", "filled": True}]
    for (x, y, w) in [(0, 0, 3), (0, 1, 2), (0, 2, 1), (29, 0, 3), (30, 1, 2), (31, 2, 1),
                      (0, 31, 3), (0, 30, 2), (0, 29, 1), (29, 31, 3), (30, 30, 2), (31, 29, 1)]:
        ops.append({"op": "clear", "x": x, "y": y, "w": w, "h": 1})
    return ops


def recipe(name, size, ops):
    return {"version": 1, "name": name, "width": size, "height": size, "palette": PALETTE,
            "frames": [{"name": "icon", "ops": ops}]}


def main():
    icon = recipe("ccar-icon", 32, rounded_tile() + diagram())
    mask_ops = [{"op": "rect", "x": 0, "y": 0, "w": 64, "h": 64, "color": "b", "filled": True}] + grid_dots(64) + diagram(16, 16)
    maskable = recipe("ccar-icon-maskable", 64, mask_ops)
    for fname, data in [("icon.pixel.json", icon), ("icon-maskable.pixel.json", maskable)]:
        with open(os.path.join(HERE, fname), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
            f.write("\n")
    print("wrote icon.pixel.json, icon-maskable.pixel.json")


if __name__ == "__main__":
    main()
