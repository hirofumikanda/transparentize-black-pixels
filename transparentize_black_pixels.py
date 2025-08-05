import os
from PIL import Image

def process_tile(tile_path):
    try:
        with Image.open(tile_path).convert("RGBA") as img:
            pixels = img.load()
            width, height = img.size

            for y in range(height):
                for x in range(width):
                    r, g, b, a = pixels[x, y]
                    if r == 0 and g == 0 and b == 0:
                        pixels[x, y] = (0, 0, 0, 0)

            img.save(tile_path)
            print(f"✅ 処理完了: {tile_path}")
    except Exception as e:
        print(f"⚠️ エラー: {tile_path} -> {e}")

def walk_tiles(root_dir):
    for z in os.listdir(root_dir):
        z_path = os.path.join(root_dir, z)
        if not os.path.isdir(z_path):
            continue
        for x in os.listdir(z_path):
            x_path = os.path.join(z_path, x)
            if not os.path.isdir(x_path):
                continue
            for y_file in os.listdir(x_path):
                if not y_file.endswith(".png"):
                    continue
                tile_path = os.path.join(x_path, y_file)
                process_tile(tile_path)

if __name__ == "__main__":
    walk_tiles("tiles")
