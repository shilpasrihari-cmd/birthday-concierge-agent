from tools.calendar_tool import get_available_dates
from models import EventSpec


class DateAgent:
    def suggest_dates(self, event_spec: EventSpec):
        """
        Skill: suggest_dates
        Uses calendar tool to find candidate dates.
        """
        return get_available_dates(event_spec.date_range)

