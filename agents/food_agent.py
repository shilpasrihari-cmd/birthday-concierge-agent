from models import EventSpec, RSVPData, DietarySummary, FoodOrder
from tools.food_tool import order_food
from agents.llm_client import get_model


class FoodAgent:
    def propose_menu(self, event_spec: EventSpec, rsvp_data: RSVPData, dietary: DietarySummary):
        """
        Skill: propose_menu
        Uses Gemini to suggest a customized menu based on age, interests, dietary needs, and attendee count.
        """
        try:
            model = get_model()
            prompt = (
                f"Propose a birthday party menu and number of servings.\n"
                f"Age of birthday child: {event_spec.age}\n"
                f"Interests: {', '.join(event_spec.interests)}\n"
                f"Number of attending guests: {len(rsvp_data.attending)}\n"
                f"Dietary Restrictions:\n"
                f"- Vegan count: {dietary.vegan}\n"
                f"- Vegetarian count: {dietary.vegetarian}\n"
                f"- Halal count: {dietary.halal}\n"
                f"- Allergies: {', '.join(dietary.allergies) if dietary.allergies else 'None'}\n\n"
                f"Output format MUST be exactly:\n"
                f"Menu: <Menu items list>\n"
                f"Servings: <Integer number of servings>"
            )
            response = model.generate_content(prompt)
            text = response.text.strip()

            lines = text.split("\n")
            menu = ""
            servings = len(rsvp_data.attending) + 5  # default fallback
            for line in lines:
                if line.startswith("Menu:"):
                    menu = line.replace("Menu:", "").strip()
                elif line.startswith("Servings:"):
                    try:
                        servings = int(line.replace("Servings:", "").strip())
                    except ValueError:
                        pass
            if not menu:
                menu = text
        except Exception as e:
            print(f"[FOOD] Error generating menu via LLM: {e}. Falling back to default.")
            if event_spec.age <= 12:
                menu = "Pizza, juice, cake"
            else:
                menu = "Mixed platters, soft drinks, cake"
            servings = len(rsvp_data.attending) + 5

        return menu, servings

    def propose_and_order_food(
        self,
        event_spec: EventSpec,
        rsvp_data: RSVPData,
        dietary: DietarySummary,
        confirm: bool,
    ) -> FoodOrder:
        """
        Skill: propose_and_order_food
        SECURITY: requires explicit confirmation.
        """
        menu, servings = self.propose_menu(event_spec, rsvp_data, dietary)
        if not confirm:
            print("[FOOD] Food order not confirmed.")
            return FoodOrder(menu=menu, servings=servings, status="not_confirmed")

        return order_food(menu, servings)


