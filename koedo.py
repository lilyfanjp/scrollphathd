#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import scrollphathd as scrhd
import misaki_gothic
## from scrollphathd.fonts import misaki_gothic # if installed at dist-packages/scrollphathd/fonts

print("""

Scrolls japanese texts across the screen in a 7x7 pixel large font.
Press Ctrl+C to exit!

""")

scrhd.rotate(180)
scrhd.write_string(u"　小江戸らぐ", x=0, y=0, font=misaki_gothic, brightness=0.5)

while True:
    scrhd.show()
    scrhd.scroll(1)
    time.sleep(0.05)

