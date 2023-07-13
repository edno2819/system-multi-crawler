from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

class SQLAlchemyManager:

    def __init__(self, app, uri):
        self.engine = create_engine(uri, echo=False)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
        self.Base = declarative_base()
        self.app = app
        self.init_db(app)

    def init_db(self):
        self.Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        return self.Session()

    def close_session(self):
        self.Session.remove()

    def commit(self):
        self.Session.commit()

    def rollback(self):
        self.Session.rollback()



# # criar uma nova instância de User
# new_user = User(name='John Doe', email='john.doe@example.com')
# # obter uma sessão do banco de dados
# session = db_manager.get_session()
# # adicionar o novo usuário à sessão
# session.add(new_user)
# # commitar a sessão para salvar as alterações no banco de dados
# session.commit()
# # consultar todos os usuários no banco de dados
# all_users = session.query(User).all()
# # imprimir todos os usuários
# for user in all_users:
#     print(f'{user.name} ({user.email})')

# # fechar a sessão quando terminar
# session.close()
