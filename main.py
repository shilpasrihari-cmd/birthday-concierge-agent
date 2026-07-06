from agents.orchestrator import ConciergeOrchestrator


def get_sample_user_input():
    return {
        "age": 10,
        "gender": "male",
        "interests": ["sports", "games"],
        "budget": 700.0,
        "date_range": ["2026-08-01", "2026-08-31"],
        "location": "Mississauga, ON",
        "guests": [
            "guest1@example.com",
            "guest2@example.com",
            "guest3@example.com",
            "guest4@example.com",
        ],
    }


def main():
    print("=== Birthday Party Concierge Agent ===")
    user_input = get_sample_user_input()

    # SECURITY: explicit confirmations
    confirm_booking = True  # set False to demonstrate guardrail
    confirm_food = True     # set False to demonstrate guardrail

    orchestrator = ConciergeOrchestrator()
    state = orchestrator.plan_party(user_input, confirm_booking, confirm_food)

    print("\n=== Final Summary ===")
    booking = state.get("booking")
    if booking:
        print(f"Booking: {booking.venue['name']} on {booking.date} ({booking.status})")

    rsvp_data = state.get("rsvp_data")
    if rsvp_data:
        print(f"Attending: {len(rsvp_data.attending)}, Not attending: {len(rsvp_data.not_attending)}")

    food_order = state.get("food_order")
    if food_order:
        import sys
        msg = f"Food: {food_order.menu}, Servings: {food_order.servings}, Status: {food_order.status}"
        try:
            print(msg)
        except UnicodeEncodeError:
            print(msg.encode(sys.stdout.encoding or 'ascii', errors='replace').decode(sys.stdout.encoding or 'ascii'))



if __name__ == "__main__":
    main()

