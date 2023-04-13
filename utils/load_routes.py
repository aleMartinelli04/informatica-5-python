from glob import glob
from importlib import import_module


def load_routes(routes_dir: str = 'routes', emoji: str = '🦦'):
    registered = 0

    for file in glob(f'{routes_dir}/**/*.py', recursive=True):
        file_name = file.replace('/', '.')[:-3]
        import_module(file_name)
        registered += 1

    print(f'{emoji} Registered {registered} routes')
