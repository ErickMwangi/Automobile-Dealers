#!/usr/bin/env python3
from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Car, car_features, Feature
fake = Faker()
with app.app_context():
    Car.query.delete()
    Feature.query.delete()

    cars = []
    for i in range(25):
        c = Car(
            name=fake.name(),
            model=fake.name(),
            image = fake.text(),
            )
        cars.append(c)
    db.session.add_all(cars)

    features = []
    for i in range(25):
        f = Feature(
            name= fake.name(),
            description=fake.text(),
        )
        features.append(f)
    db.session.add_all(features)
    combinations=set()
    transmission = ["Automatic", "Manual"]

    for _ in range (25):
        car_id= randint(1,25)
        feature_id= randint(1,25)
        transmission = rc(transmission)
        if (car_id, feature_id, transmission ) in combinations:
            continue
        combinations.add((car_id, feature_id, transmission))
        car_feature_data={"car_id":car_id, "feature_id":feature_id, "transmission":transmission}
        statement=db.insert(car_features).values(car_feature_data)
        db.session.execute(statement)
        db.session.commit()