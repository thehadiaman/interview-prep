from libs.appointment.database.index import get_all_booked_slots_db, book_appointment_db
from libs.appointment.usecase.book_appointment_usecase import book_slot_usecase_factory
from libs.appointment.usecase.get_available_slots_usecase import get_available_slots_usecase_factory

get_available_slots_usecase = get_available_slots_usecase_factory(get_all_booked_slots_db)
book_slot_usecase = book_slot_usecase_factory(get_all_booked_slots_db, book_appointment_db)