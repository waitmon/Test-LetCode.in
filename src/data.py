from dataclasses import dataclass


@dataclass
class NewUser:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    address_line_1: str = None
    address_line_2: str = None
    state: str = None
    postal_code: str = None
    date_of_birth: str = None
