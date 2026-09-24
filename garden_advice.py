"""Provide gardening advice based on a season and plant type."""


SEASON_ADVICE = {
    "spring": (
        "Prepare the soil and start planting suitable seeds "
        "and seedlings."
    ),
    "summer": (
        "Water your plants regularly and provide some shade."
    ),
    "autumn": (
        "Remove fallen leaves and prepare plants for cooler weather."
    ),
    "winter": (
        "Protect your plants from frost with covers."
    ),
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest herbs regularly to encourage new growth.",
    "tree": "Check the soil moisture before watering deeply.",
}


def get_season_advice(season):
    """Return gardening advice for a season.

    Args:
        season (str): The season entered by the user.

    Returns:
        str: Advice for the season or a fallback message.
    """
    return SEASON_ADVICE.get(
        season,
        "No advice for this season.",
    )


def get_plant_advice(plant_type):
    """Return gardening advice for a plant type.

    Args:
        plant_type (str): The plant type entered by the user.

    Returns:
        str: Advice for the plant type or a fallback message.
    """
    return PLANT_ADVICE.get(
        plant_type,
        "No advice for this type of plant.",
    )


def main():
    """Collect user input and display relevant gardening advice."""
    season = input("Enter the season: ").strip().lower()
    plant_type = input("Enter the plant type: ").strip().lower()

    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)

    print("\nGardening advice:")
    print(season_advice)
    print(plant_advice)


if __name__ == "__main__":
    main()
