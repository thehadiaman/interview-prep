from database.execute import execute_query

# Factory function to generate the function for booking appointment
def book_appointment_db_factory():
    def book_appointment_db(name, phone, date, slot):
        query = '''
            INSERT INTO appointments (name, phone, date, slot)
            VALUES (?, ?, ?, ?)
        '''
        params = [
            name, phone, date, slot
        ]
        execute_query(query, params)

        return {}

    return book_appointment_db