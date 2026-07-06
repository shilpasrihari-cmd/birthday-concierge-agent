from models import BookingInfo


class BookingAgent:
    def book_venue(self, venue: dict, date: str, confirm: bool) -> BookingInfo:
        """
        Skill: book_venue
        SECURITY: requires explicit confirmation.
        """
        if not confirm:
            return BookingInfo(venue=venue, date=date, status="not_confirmed")

        # Mock booking
        print(f"[BOOKING] Booking {venue['name']} on {date}.")
        return BookingInfo(venue=venue, date=date, status="confirmed")

