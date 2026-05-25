# Simple Robot Simulator

import random
import time

battery = 100
tasks = ["Welding", "Pick and Place", "Painting", "Inspection"]

print("=== INDUSTRIAL ROBOT SYSTEM ===")

while battery > 0:

    print("\nBattery Level:", battery, "%")

    task = random.choice(tasks)
    print("Robot is performing:", task)

    work = random.randint(10, 25)
    battery -= work

    temperature = random.randint(30, 80)
    print("Motor Temperature:", temperature, "°C")

    if temperature > 70:
        print("WARNING: High Temperature!")

    if battery <= 20:
        print("LOW BATTERY - Charging Required")
        break

    time.sleep(2)

print("\nRobot Shutdown")