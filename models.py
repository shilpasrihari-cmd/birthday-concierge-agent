from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class EventSpec:
    age: int
    gender: str
    interests: List[str]
    budget: float
    date_range: List[str]
    location: str
    guests: List[str]


@dataclass
class BookingInfo:
    venue: Dict[str, Any]
    date: str
    status: str


@dataclass
class RSVPData:
    attending: List[str]
    not_attending: List[str]


@dataclass
class DietarySummary:
    vegan: int
    vegetarian: int
    halal: int
    allergies: List[str]


@dataclass
class FoodOrder:
    menu: str
    servings: int
    status: str

