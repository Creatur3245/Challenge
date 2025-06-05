import matplotlib.pyplot as plt

# Coordinates (longitude, latitude)
coordinates = {
    "Anomalies": [(-54.3484, -4.4429), (-54.3137, -4.2840)],
    "Kuhikugu Site": [(-53.5, -10.2)],
    "Wind Patterns": [(-53.21, -10.45), (-54.10, -4.05)],
    "Weather Stations": [(-53.18, -10.42), (-54.05, -4.01)],
    "Jaguar Sightings": [(-53.19, -10.44), (-54.08, -4.03)]
}

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
for label, coords in coordinates.items():
    lons, lats = zip(*coords)
    ax.scatter(lons, lats, label=label, s=100)

ax.set_title("Coordinate Verification Map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.show()
