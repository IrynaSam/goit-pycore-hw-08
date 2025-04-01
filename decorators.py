
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Missing argument(s)!"
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    return inner