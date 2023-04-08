from src.data import NewUser, University
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
        address_line_2=faker_en.building_number(),
        state=faker_en.current_country(),
        postal_code=faker_en.postcode(),
        date_of_birth=faker_en.date(),
    )


def generated_university():
    yield University(
        uni_name=['University of Aberdeen', 'University of Wales, Aberystwyth', 'University of Abertay Dundee',
                  'American InterContinental University - London', 'Aga Khan University', 'Anglia Ruskin University',
                  'Aston University', 'The American University in London', 'Heythrop College, University of London',
                  'University of Manchester', 'Middlesex University', 'Imperial College School of Medicine'
                  'The Manchester Metropolitan University' 'Napier University', 'University of Newcastle-upon-Tyne',
                  'University of Wales, Newport', 'Newport International University', 'University of Northampton',
                  'University of Nottingham', 'Nottingham Trent University', 'Open University', 'University of Oxford',
                  'University of Paisley', 'University of Plymouth', 'University of Portsmouth', 'Queen Mary, '
                                                                                                 'University of '
                                                                                                 'London',
                  "The Queen's University Belfast", 'Royal Academy of Music, University of London', 'Royal College of '
                                                                                                    'Art',
                  'Royal College of Music, University of London', 'University of Reading', 'Royal Free Hospital '
                                                                                           'School of Medicine, '
                                                                                           'University of London',
                  'The Robert Gordon University', 'Royal Holloway and Bedford New College', 'Richmond University - '
                                                                                            'The American '
                                                                                            'International University '
                                                                                            'in London',
                  'Roehampton University of Surrey', 'University of Salford', 'Institute of Advanced Legal Studies, '
                                                                              'University of London',
                  'Institute of Classical Studies, University of London', 'Institute of Germanic Studies, University '
                                                                          'of London',
                  'Institute of Latin American Studies, University of London', 'Warburg Institute, '
                  'University of London', 'South Bank University', 'Schiller International University, London',
                  'Stratford College London', "Saint George's Hospital Medical School, University of London",
                  'University of Sheffield']
    )
