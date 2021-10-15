from utils import create_keyboard
from types import SimpleNamespace
KEYS = SimpleNamespace(**dict(
    random_connect = 'Connect',
    settings = 'Settings'
))

keyboards = dict(
    main = create_keyboard([KEYS.random_connect, KEYS.settings])
)