from models import FoodOrder


def order_food(menu: str, servings: int) -> FoodOrder:
    # Mock food ordering
    print(f"[FOOD] Ordering {menu} for {servings} servings.")
    return FoodOrder(menu=menu, servings=servings, status="ordered")

