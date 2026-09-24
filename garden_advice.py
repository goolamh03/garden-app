"""Provide basic gardening advice based on user selections."""


# Get user selections instead of using hardcoded values.
season = input("Enter the season: ").strip().lower()
plant_type = input("Enter the plant type: ").strip().lower()

# Variable to hold the generated gardening advice.
advice = ""

# Determine advice based on the selected season.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the selected plant type.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice.
print(advice)

# TODO:
# - Refactor the code into functions for readability and modularity.
# - Store gardening advice in dictionaries.
# - Add function documentation.
