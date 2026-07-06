from tools.email_tool import send_email
from models import EventSpec, BookingInfo
from agents.llm_client import get_model


class InvitationAgent:
    def compose_invitation_email(self, event_spec: EventSpec, booking: BookingInfo):
        """
        Skill: compose_invitation_email
        Uses Gemini to generate a fun, personalized subject and email body.
        """
        try:
            model = get_model()
            prompt = (
                f"Write a fun, personalized birthday party invitation email.\n"
                f"The birthday child is {event_spec.age} years old and is a {event_spec.gender}.\n"
                f"Their interests are: {', '.join(event_spec.interests)}.\n"
                f"The venue is: {booking.venue['name']}.\n"
                f"The date is: {booking.date}.\n"
                f"Ask guests to RSVP and let us know if they have any dietary restrictions.\n"
                f"Output format MUST be exactly:\n"
                f"Subject: <Subject Line>\n"
                f"Body:\n"
                f"<Email Body>"
            )
            response = model.generate_content(prompt)
            text = response.text.strip()

            lines = text.split("\n")
            subject = f"Birthday Party at {booking.venue['name']} on {booking.date}"
            body_lines = []
            capture_body = False
            for line in lines:
                if line.startswith("Subject:"):
                    subject = line.replace("Subject:", "").strip()
                elif line.startswith("Body:"):
                    capture_body = True
                elif capture_body:
                    body_lines.append(line)

            if body_lines:
                body = "\n".join(body_lines).strip()
            else:
                body = text
        except Exception as e:
            print(f"[INVITATION] Error generating email via LLM: {e}. Falling back to default.")
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


