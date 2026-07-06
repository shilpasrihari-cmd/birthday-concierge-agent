from tools.email_tool import send_email
from models import EventSpec, BookingInfo


class InvitationAgent:
    def compose_invitation_email(self, event_spec: EventSpec, booking: BookingInfo):
        """
        Skill: compose_invitation_email
        """
        subject = f"Birthday Party at {booking.venue['name']} on {booking.date}"
        body = (
            f"You're invited to a birthday party!\n\n"
            f"Location: {booking.venue['name']} ({booking.venue['distance']})\n"
            f"Date: {booking.date}\n"
            f"Please RSVP and share any dietary restrictions."
        )
        return subject, body

    def send_invitations(self, event_spec: EventSpec, booking: BookingInfo):
        """
        Skill: send_invitations
        """
        subject, body = self.compose_invitation_email(event_spec, booking)
        for guest in event_spec.guests:
            # SECURITY: do not log full body
            send_email(guest, subject, body)

