from models import EventSpec
from agents.intake_agent import IntakeAgent
from agents.date_agent import DateAgent
from agents.venue_agent import VenueAgent
from agents.booking_agent import BookingAgent
from agents.invitation_agent import InvitationAgent
from agents.rsvp_agent import RSVPAgent
from agents.dietary_agent import DietaryAgent
from agents.food_agent import FoodAgent


class ConciergeOrchestrator:
    def __init__(self):
        self.intake = IntakeAgent()
        self.date_agent = DateAgent()
        self.venue_agent = VenueAgent()
        self.booking_agent = BookingAgent()
        self.invitation_agent = InvitationAgent()
        self.rsvp_agent = RSVPAgent()
        self.dietary_agent = DietaryAgent()
        self.food_agent = FoodAgent()
        self.state = {}

    def plan_party(self, user_input: dict, confirm_booking: bool, confirm_food: bool):
        # Intake
        event_spec: EventSpec = self.intake.create_event_spec(user_input)
        self.state["event_spec"] = event_spec

        # Dates
        candidate_dates = self.date_agent.suggest_dates(event_spec)
        self.state["candidate_dates"] = candidate_dates

        # Venues (with Antigravity-style parallel scoring)
        venues = self.venue_agent.recommend_venues(event_spec, candidate_dates)
        self.state["venues"] = venues

        # SECURITY: human-in-the-loop selection
        selected_date = candidate_dates[0]
        selected_venue = venues[0]
        self.state["selected_date"] = selected_date
        self.state["selected_venue"] = selected_venue

        # Booking
        booking = self.booking_agent.book_venue(selected_venue, selected_date, confirm_booking)
        self.state["booking"] = booking

        if booking.status != "confirmed":
            print("[ORCHESTRATOR] Booking not confirmed. Stopping workflow.")
            return self.state

        # Invitations
        self.invitation_agent.send_invitations(event_spec, booking)

        # RSVPs
        rsvp_data = self.rsvp_agent.collect_rsvps(event_spec)
        self.state["rsvp_data"] = rsvp_data

        # Dietary
        dietary_summary = self.dietary_agent.summarize_dietary(rsvp_data)
        self.state["dietary_summary"] = dietary_summary

        # Food
        food_order = self.food_agent.propose_and_order_food(
            event_spec, rsvp_data, dietary_summary, confirm_food
        )
        self.state["food_order"] = food_order

        return self.state

