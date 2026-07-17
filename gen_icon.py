"""Generate app icons for YearBlocks PWA."""
from PIL import Image, ImageDraw

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    # Draw a mini year-grid: 5 columns x 7 rows
    cols = 5
    rows = 7
    margin = size * 0.18
    gap = size * 0.025
    avail = size - margin * 2
    cell = (avail - gap * (cols - 1)) / cols
    # Recalculate to fit rows too
    cell_h = (avail - gap * (rows - 1)) / rows
    cell = min(cell, cell_h)

    total_w = cell * cols + gap * (cols - 1)
    total_h = cell * rows + gap * (rows - 1)
    start_x = (size - total_w) / 2
    start_y = (size - total_h) / 2

    # Simulate: past days green, today orange, future dark gray
    # Like we're ~60% through the year
    total_cells = cols * rows  # 35
    today_idx = 21  # ~60%

    for i in range(total_cells):
        r = i // cols
        c = i % cols
        x = start_x + c * (cell + gap)
        y = start_y + r * (cell + gap)

        if i < today_idx:
            color = (48, 209, 88, 255)    # green #30D158
        elif i == today_idx:
            color = (255, 159, 10, 255)   # orange #FF9F0A
        else:
            color = (44, 44, 46, 255)     # dark gray #2C2C2E

        radius = cell * 0.2
        draw.rounded_rectangle([x, y, x + cell, y + cell], radius=radius, fill=color)

    return img

sizes = [192, 512, 1024]
for s in sizes:
    icon = make_icon(s)
    icon.save(f"icon-{s}.png")
    print(f"Generated icon-{s}.png")

# Apple touch icon (180x180)
apple_icon = make_icon(180)
apple_icon.save("apple-touch-icon.png")
print("Generated apple-touch-icon.png")
