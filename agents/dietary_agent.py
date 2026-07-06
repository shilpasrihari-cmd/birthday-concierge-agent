from models import RSVPData, DietarySummary


class DietaryAgent:
    def summarize_dietary(self, rsvp_data: RSVPData) -> DietarySummary:
        """
        Skill: summarize_dietary
        Mock: no restrictions.
        """
        print("[DIETARY] No dietary restrictions collected (mock).")
        return DietarySummary(vegan=0, vegetarian=0, halal=0, allergies=[])

