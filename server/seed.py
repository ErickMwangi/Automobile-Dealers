# seed.py
# ff

from app import app
from models import db, Car
from dotenv import dotenv_values

# db.init_app(app)

with app.app_context():

    print('Deleting existing cars...')
    Car.query.delete()

    print('Creating car objects...')
    Mercedes = Car(
        name='Mercedies Benz',
        model='S550 LWB',
        image='https://aristocars.co.ke/wp-content/uploads/2021/12/WhatsApp-Image-2021-10-28-at-7.41.51-PM.jpeg' 
    )
    Toyota = Car(
        name='Toyota Corolla',
        model='Altis [2008-2011]',
        image='https://media.licdn.com/dms/image/C5112AQEwRVOi1XsHHQ/article-cover_image-shrink_600_2000/0/1553781947495?e=2147483647&v=beta&t=8pK5eApqxV89aslCAGHziD1DTJNj2MljHk83ubjkDyw'
    )
    Subaru = Car(
        name='Subaru',
        model='Impreza 22B',
        image='https://hips.hearstapps.com/hmg-prod/images/subaru-22-b-front-6419cd0ac4059.png?crop=1.00xw:0.851xh;0,0.108xh&resize=980:*'
    )
    Nissan = Car(
        name='Nissan',
        model='240SX',
        image='https://www.carscoops.com/wp-content/uploads/2022/01/Nissan-Silvia-240-SX-r1-1024x555.jpg'
    )
    Audi = Car(
        name='Audi',
        model='A4',
        image='https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cdni.autocarindia.com/ExtraImages/20220922115517_Audi_A4_Tango_Red.jpg&w=700&q=90&c=1'
    )
    Honda = Car(
        name='Honda',
        model='Civic Type R',
        image='https://www.honda.ca/-/media/Brands/Honda/Models/TYPE-R/2023/Overview/03_Key-Features/Honda_Civic_TypeR_key-features_desktop_1036x520.png?h=520&iar=0&w=1036&rev=86a8e32265ac446dadf66e704156f39f&hash=F79E92877AED80EC7864F74CC77B2267'
    )
    volkswagen = Car(
        name='volkswagen',
        model='golf mk7',
        image='https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1562255566/autoexpress/vw-golf-mk7-uk-1.jpg'
    )
    Nissan2 = Car(
        name='Nissan',
        model='Altima 2020',
        image='https://hips.hearstapps.com/hmg-prod/images/2023-nissan-altima-113-1654783718.jpg?crop=0.712xw:0.535xh;0.132xw,0.347xh&resize=1200:*'
    )

    Hyundai = Car(
        name='Hyundai',
        model='Sonata 2023',
        image='https://s7d1.scene7.com/is/image/hyundai/2022-sonata-1?wid=1200&hei=630&qlt=85,0&fmt=webp'
    )

    Jeep = Car(
        name='Jeep',
        model='Wrangler 2023',
        image='https://media.ed.edmunds-media.com/jeep/wrangler/2023/oem/2023_jeep_wrangler_convertible-suv_high-tide_fq_oem_1_1600.jpg'
    )

    print('Adding Car objects to transaction...')
    db.session.add_all([Mercedes, Toyota, Subaru, Nissan, Audi, Honda, volkswagen, Nissan2, Hyundai, Jeep])
    print('Committing transaction...')
    db.session.commit()
    print('Complete.')
















# #!/usr/bin/env python3
# from random import randint, choice as rc
# from faker import Faker
# from app import app
# from models import db, Car, car_features, Feature
# fake = Faker()
# with app.app_context():
#     Car.query.delete()
#     Feature.query.delete()
#     cars = []
#     for i in range(25):
#         c = Car(
#             name=fake.name(),
#             model=fake.name(),
#             image = fake.text(),
#             )
#         cars.append(c)
#     db.session.add_all(cars)
#     features = []
#     for i in range(25):
#         f = Feature(
#             name= fake.name(),
#             description=fake.text(),
#         )
#         features.append(f)
#     db.session.add_all(features)
#     combinations=set()
#     transmission = ["Automatic", "Manual"]
#     for _ in range (25):
#         car_id= randint(1,25)
#         feature_id= randint(1,25)
#         transmission = rc(transmission)
#         if (car_id, feature_id, transmission ) in combinations:
#             continue
#         combinations.add((car_id, feature_id, transmission))
#         car_feature_data={"car_id":car_id, "feature_id":feature_id, "transmission":transmission}
#         statement=db.insert(car_features).values(car_feature_data)
#         db.session.execute(statement)
#         db.session.commit()