from sqlalchemy import create_engine

class db():
    def __init__(self):
        pass

    def get_connect(self):
        return create_engine('sqlite:///chinook.db') #La ruta depende de donde tengas almacenada la base de datos
