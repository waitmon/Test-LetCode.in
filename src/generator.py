from src.data import NewUser
from faker import Faker

faker_en = Faker('En')
Faker.seed()


def generated_new_user():
    yield NewUser(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        phone_number=faker_en.msisdn(),
        address_line_1=faker_en.address(),
        address_line_2=faker_en.address(),
        state=faker_en.current_country(),
        postal_code=faker_en.postcode(),
        date_of_birth=faker_en.date(),
    )
