
rooms = {"A": "Dirty", "B": "Dirty"}
position = "A"

while "Dirty" in rooms.values():
    if rooms[position] == "Dirty":
        print("Cleaning room", position)
        rooms[position] = "Clean"
    elif position == "A":
        position = "B"
        print("Moving to room B")
    else:
        position = "A"
        print("Moving to room A")

print("All rooms are clean")
