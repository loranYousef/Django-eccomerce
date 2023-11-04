import os

os.environ["DJANGO_SETTINGS_MODULE"] = "project.src.settings"
import django
django.setup()


from faker import Faker
import random
from product.models import Product, Brand


def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']

    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,9)]}"
        Brand.objects.create(name=name,image=image)
    print(f"Seed {n} Brands ...")


def seed_product(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg']
    flag_types =['Sale','Feature','New']

    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        image =f"products/{images[random.randint(0,13)]}"
        brand = Brand.objects.get(id=random.randint(3,20))
        price = round(random.uniform(20.99,99.99),2)
        flag= flag_types[random.randint(0,2)]
        subtitle = fake.text(max_nb_chars=500)
        description = fake.text(max_nb_chars=2000)
        quantity = random.randint(2,30)

        Product.objects.create(
            name=name,
            sku=sku,
            image=image,
            brand=brand,
            price=price,
            flag=flag,
            subtitle=subtitle,
            description=description,
            quantity=quantity
        )

    print(f"Seed {n} Products ...")



# seed_brand(20)
seed_product(3000)