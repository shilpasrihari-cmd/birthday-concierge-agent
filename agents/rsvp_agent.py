from models import RSVPData, EventSpec


class RSVPAgent:
    def collect_rsvps(self, event_spec: EventSpec) -> RSVPData:
        """
        Skill: collect_rsvps
        Mock: assume half attend.
        """
        attending = event_spec.guests[: len(event_spec.guests) // 2]
        not_attending = event_spec.guests[len(attending):]
        print(f"[RSVP] Attending: {len(attending)}, Not attending: {len(not_attending)}")
        return RSVPData(attending=attending, not_attending=not_attending)

