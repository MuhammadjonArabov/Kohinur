from aiogram.fsm.state import StatesGroup, State

class TeacherStates(StatesGroup):
    fullname = State()
    subject = State()
    phone = State()
    sending_datas_to_admin = State()
    waiting_admin = State()
    waiting_select = State()
    teacher_tests_selected = State()
    teacher_group_selected = State()
    teacher_test_subject_selecting = State()
    teacher_test_count_selecting = State()
    teacher_test_waiting_start = State()
    reason_non_acceptance = State()
    teacher_new_group_start = State()
    teacher_new_group_subject = State()
    teacher_new_group_days = State()
    teacher_new_group_times = State()