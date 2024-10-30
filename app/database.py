import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql://postgres:password@db/clients"

MAX_RETRIES = 5
RETRY_DELAY = 10

def create_db_engine():
    engine = create_engine(DATABASE_URL)
    return engine

def connect_with_retry(max_retries=MAX_RETRIES, retry_delay=RETRY_DELAY):
    engine = create_db_engine()
    Session = sessionmaker(bind=engine)

    for attempt in range(max_retries):
        try:
            with engine.connect() as connection:
                print("Подключение успешно!")
                return Session, engine
        except SQLAlchemyError:
            print(f"Не удалось подключиться. Попытка {attempt + 1} из {max_retries}.")
            time.sleep(retry_delay)

    raise Exception("Не удалось подключиться к базе данных после нескольких попыток.")


SessionLocal, engine = connect_with_retry()

Base = declarative_base()
