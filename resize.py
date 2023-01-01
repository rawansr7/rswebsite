from PIL import Image

size = (1056, 594)

for i in range(1, 13):
    for j in range(1, 5):
        print(i, j)
        image = Image.open(f"static/imgCars/c{i}.{j}.png")

        new_image = image.resize(size)
        new_image.save(f"static/imgCars/c{i}.{j}.png")
