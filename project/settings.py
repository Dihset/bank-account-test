import os

__all__ = ('DB_LOGIN', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_URI', 'TORTOISE_CONFIG')


DB_LOGIN = os.getenv('DB_LOGIN', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'bank-account-postgresql')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_NAME = os.getenv('DB_NAME', 'bank-account')

DB_URI = f'postgres://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

TORTOISE_CONFIG = {
    'connections': {
        'default': DB_URI
    },
    'apps': {
        'models': {
            'models': ['project.core.models'],
            'default_connection': 'default',
        }
    }
}
