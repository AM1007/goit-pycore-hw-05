from functools import wraps
import re

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            # get error message
            msg: str = ve.args[0]
            # if we have 'got', pattern of error will be like (expected 2, got N)
            pattern = r"got (\d)"
            got = re.search(pattern, msg)
            if got:
                count = got.group(1)
                # depending on N return corresponding message
                if count == '0':
                    return "Give me name and phone please."
                elif count == '1':
                    return "Give me phone please."
            # if we have only expected, too many entered args
            elif msg.find("expected"):
                return "Too many arguments"
            # any other unexpected ValueError
            return f"{func.__name__} error, {type(ve)}, {ve}"
        except KeyError:
            return "Contact does not exist"
        except IndexError:
            return "Enter user name"
        except Exception as error:
            return f"{func.__name__} error, {type(error)}, {error}"
    return inner
