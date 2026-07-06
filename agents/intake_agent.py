from models import EventSpec


class IntakeAgent:
    def create_event_spec(self, user_input: dict) -> EventSpec:
        """
        Skill: create_event_spec
        Parses user input into a structured EventSpec.
        """
        return EventSpec(
            age=user_input["age"],
            gender=user_input["gender"],
            interests=user_input["interests"],
            budget=user_input["budget"],
            date_range=user_input["date_range"],
            location=user_input["location"],
            guests=user_input["guests"],
        )

