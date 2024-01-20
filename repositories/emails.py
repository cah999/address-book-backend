from models.emails import Emails
from utils.repository import SQLAlchemyRepository


class EmailsRepository(SQLAlchemyRepository):
    model = Emails
