from utils import create_keyboard
from types import SimpleNamespace

KEYS = SimpleNamespace(**dict(
    random_connect = ':satellite: Connect',
    settings = ':gear: Settings',
    back = ':cross_mark: Back',
    disconnect = ':cross_mark: Disconnect'
))

keyboards = SimpleNamespace(**dict(
    main = create_keyboard([KEYS.random_connect, KEYS.settings]),
    back=create_keyboard([KEYS.back]),
    talking=create_keyboard([KEYS.disconnect])
)
)

predefined_texts = SimpleNamespace(**dict(
    welcome = 'To connect to an stranger click on the <b>Connect</b> button.',
    init = "Please choose an option.",
    disconnect = "you are disconnnected"
)
)

states = SimpleNamespace(**dict(
    init = "initializing",
    random_connect = "waiting",
    settings = "settings",
    talking = 'talking'
)
)