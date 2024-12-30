from common.core.error_handler import error_handler
from common.util.generate_time_slots import get_time_slots


def get_available_slots_usecase_factory(get_all_booked_slots_db):

    def get_available_slots_usecase(body):
        try:
            date = body.get('date', None)
            if date is None:
                raise error_handler('DATE_IS_REQUIRED')

            booked_slots = get_all_booked_slots_db(date=date)

            all_slots = get_time_slots()

            # Filter out all booked slots
            booked_slots = [item['slot'] for item in booked_slots]
            available_slots = [slot for slot in all_slots if slot not in booked_slots]

            return {
                "slots": available_slots
            }

        except Exception as e:
            raise e

    return get_available_slots_usecase
