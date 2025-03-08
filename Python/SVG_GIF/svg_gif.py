#!/usr/bin/env python3
import os
import time
import argparse
import io

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

def convert_svg_to_gif(
    svg_path,
    output_gif,
    duration=2.0,
    fps=10,
    width=400,
    height=400,
):
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    
    html_template = f"""
    <html>
    <head>
      <meta charset="UTF-8">
      <title>SVG Animation</title>
      <style>
        body, html {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            width: {width}px;
            height: {height}px;
        }}
      </style>
    </head>
    <body>
    {svg_content}
    </body>
    </html>
    """
    
    temp_html_path = "temp_svg_animation.html"
    with open(temp_html_path, "w", encoding="utf-8") as temp_html:
        temp_html.write(html_template)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"--window-size={width}x{height}")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("file://" + os.path.abspath(temp_html_path))
    
    time.sleep(1.0)
    
    num_frames = int(duration * fps)
    frame_interval = duration / num_frames
    
    frames = []
    
    for i in range(num_frames):
        png_data = driver.get_screenshot_as_png()
        
        # Use io.BytesIO to wrap the PNG data correctly
        screenshot_img = Image.open(io.BytesIO(png_data))
        
        # Crop if needed
        # screenshot_img = screenshot_img.crop((0, 0, width, height))
        
        frames.append(screenshot_img.convert("RGB"))
        
        time.sleep(frame_interval)
    
    driver.quit()
    
    frame_duration_ms = int(1000 / fps)
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration_ms,
        loop=0
    )
    
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    
    print(f"Created animated GIF: {output_gif}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert an animated SVG file to an animated GIF using headless Chrome."
    )
    parser.add_argument("input_svg", help="Path to the input SVG file.")
    parser.add_argument("output_gif", help="Path to the output GIF file.")
    parser.add_argument("--duration", type=float, default=2.0,
                        help="Total duration of the animation capture in seconds (default: 2.0).")
    parser.add_argument("--fps", type=int, default=10,
                        help="Frames per second for the output GIF (default: 10).")
    parser.add_argument("--width", type=int, default=400,
                        help="Viewport width in pixels (default: 400).")
    parser.add_argument("--height", type=int, default=400,
                        help="Viewport height in pixels (default: 400).")
    
    args = parser.parse_args()
    
    convert_svg_to_gif(
        svg_path=args.input_svg,
        output_gif=args.output_gif,
        duration=args.duration,
        fps=args.fps,
        width=args.width,
        height=args.height
    )

if __name__ == "__main__":
    main()

