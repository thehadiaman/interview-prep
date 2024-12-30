# Error handler
def error_handler(error_message: str):
    return Exception({
        "message": error_message
    })