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
    },
    'apps': {
        'models': {
            'models': ['aerich.models', 'app.models'],
        },
    },
    'routers': ['config.router.Router'],
}
