from models import EventSpec, RSVPData, DietarySummary, FoodOrder
from tools.food_tool import order_food


class FoodAgent:
    def propose_menu(self, event_spec: EventSpec, rsvp_data: RSVPData, dietary: DietarySummary):
        """
        Skill: propose_menu
        Simple menu based on age and count.
        """
        count = len(rsvp_data.attending)
        if event_spec.age <= 12:
            menu = "Pizza, juice, cake"
        else:
            menu = "Mixed platters, soft drinks, cake"
        servings = count + 5
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

