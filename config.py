class Config:
    """Flask Configurations"""
    ENV = 'development'
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/flask"