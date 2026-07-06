from concurrent.futures import ThreadPoolExecutor
from tools.venue_tool import search_venues
from models import EventSpec


def score_venue(venue, event_spec: EventSpec):
    # Simple scoring: lower price + closer distance + matching interests
    score = 0
    score -= venue["price"] / 100
    if venue["distance"].endswith("km"):
        score -= float(venue["distance"].replace("km", "")) / 2
    if "sports" in event_spec.interests and venue["type"] == "sports":
        score += 5
    if "games" in event_spec.interests and venue["type"] == "games":
        score += 5
    return score


class VenueAgent:
    def recommend_venues(self, event_spec: EventSpec, candidate_dates):
        """
        Skill: recommend_venues
        Uses Antigravity-style parallel scoring of venues.
        """
        venues = search_venues(event_spec)

        # Antigravity: evaluate venues in parallel
        with ThreadPoolExecutor(max_workers=len(venues)) as executor:
            scores = list(executor.map(lambda v: score_venue(v, event_spec), venues))

        ranked = sorted(
            zip(venues, scores),
            key=lambda vs: vs[1],
            reverse=True,
        )
        return [v for v, s in ranked]

