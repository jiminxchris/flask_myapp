from config.default import *
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv(os.path.join(BASE_DIR, '.env'))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'myapp.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=quote(os.getenv('DB_PASSWORD')),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'Zb3\x81\xdb\xf1\xd9\xd7-Knb\x8eB\xa5\x18'
