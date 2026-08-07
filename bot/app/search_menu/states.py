from aiogram.fsm.state import StatesGroup, State


class SearchMenuState(StatesGroup):

    waiting_length_type = State()

    waiting_dictionary_word = State()

    waiting_trap_username = State()
