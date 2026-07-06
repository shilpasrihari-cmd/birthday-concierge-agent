from models import EventSpec


def search_venues(event_spec: EventSpec):
    # Mock: return venues tailored to age/interests/budget
    return [
        {
            "name": "FunZone Arcade",
            "price": 500,
            "capacity": 20,
            "distance": "5km",
            "type": "games",
        },
        {
            "name": "Sports Arena Kids",
            "price": 650,
            "capacity": 25,
            "distance": "8km",
            "type": "sports",
        },
        {
            "name": "Family Restaurant Party Room",
            "price": 400,
            "capacity": 15,
            "distance": "3km",
            "type": "dining",
        },
    ]

