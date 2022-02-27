length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_liters = volume * 0.001
necessary_liters = volume_liters * (1 - percent / 100)
print(necessary_liters)