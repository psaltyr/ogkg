import matplotlib.pyplot as plt

# Зчитування даних із файлу
file_path = "DS5.txt"
points = []

with open(file_path, "r") as file:
    for line in file:
        x, y = map(int, line.split())
        points.append((x, y))

# Розділення координат на X та Y
x_coords, y_coords = zip(*points)

# Створення графіку
plt.figure(figsize=(20, 10))  # Розмір вікна в дюймах (960x540 пікселів при DPI = 100)
plt.scatter(x_coords, y_coords, s=1, color="pink")  # s - розмір точки
plt.title("Точки з датасету")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")  # Однаковий масштаб по осях

# Збереження результату
output_file = "output.png"
plt.savefig(output_file, dpi=100)  # DPI = 100 для відповідності розміру 960x540
plt.show()

print(f"Результат збережено у файл: {output_file}")
