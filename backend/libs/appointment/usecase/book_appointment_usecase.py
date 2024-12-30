from common.core.error_handler import error_handler
from common.util.format_date import get_formatted_date
from common.util.generate_time_slots import get_time_slots

# Factory function to generate the function for
def book_slot_usecase_factory(get_all_booked_slots_db, book_appointment_db):

    def book_slot_usecase(body):
        try:
            name = body.get('name', None)
            phone = body.get('phone', None)
            date = body.get('date', None)
            slot = body.get('slot', None)

            if not (name and phone and date and slot):
                raise error_handler('REQUIRED_FIELD(S)_MISSING')

            date, is_valid = get_formatted_date(date)

            if is_valid is False:
                raise error_handler('DATE_IS_NOT_VALID')

            slots = get_time_slots()

            if slot not in slots:
                raise error_handler('INVALID_SLOT')

            preexisting_slot = get_all_booked_slots_db(date=date, slot=slot)

            if len(preexisting_slot) > 0:
                raise error_handler('SLOT_ALREADY_BOOKED')

            book_appointment_db(name, phone, date, slot)

            return {
                "message": "APPOINTMENT_BOOKED"
            }

        except Exception as e:
            raise e

    return book_slot_usecase
