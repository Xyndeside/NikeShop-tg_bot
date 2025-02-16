from aiogram.filters.state import State, StatesGroup

class CartState(StatesGroup):
    item_selected = State()