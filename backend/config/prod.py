DATABASE = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'database': 'test',
                'user': 'test',
                'password': 'test123!',
            },
        },
        'reader': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'database': 'test',
                'user': 'test',
                'password': 'test123!',
            },
        }
    },
    'apps': {
        'models': {
            'models': ['app.models'],
            'default_connection': 'default',
        }
    },
}
