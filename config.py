import os.path

SQLALCHEMY_DATABASE = os.path.join(os.getcwd(), 'test.db')
FIXTURE_BASE_DIR = 'fixtures'


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLALCHEMY_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USER_ROLES_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'user_roles.json')
    USER_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'users.json')
    ORDERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'orders.json')
    OFFERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'offers.json')
