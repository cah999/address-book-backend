from models.phones import Phones
from utils.repository import SQLAlchemyRepository


class PhonesRepository(SQLAlchemyRepository):
    model = Phones
