DB_URL = 'asyncpg://danil@localhost:5432/fastapi'
DB_MODELS = [
    'src.models',
    'aerich.models',
]
TORTOISE_ORM = {
    'connections': {'default': DB_URL},
    'apps': {
        'models': {
            'models': DB_MODELS,
            'default_connection': 'default',
        },
    },
}

API_TOKEN = 'test'
