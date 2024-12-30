from database.execute import execute_query

# Factory function to generate the function for getting availabel slots
def get_all_booked_slots_db_factory():
    def get_all_booked_slots_db(date=None, slot=None):

        selector = ''
        params = []

        # Build where condition as per the payload given
        if date is not None:
            selector = 'date = ?'
            params.append(date)

        if slot is not None:
            if selector is not None:
                selector += ' AND '
            selector += 'slot = ?'

            params.append(slot)

        if selector is not None:
            selector = 'WHERE ' + selector

        query = f'''
            SELECT id, slot FROM appointments {selector}
        '''

        all_slots = execute_query(query, params)

        return all_slots

    return get_all_booked_slots_db