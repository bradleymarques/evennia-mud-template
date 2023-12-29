# nopycln: file

r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

from dotenv import load_dotenv

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *  # noqa # nopycln: import

######################################################################
# Evennia base server config
######################################################################


load_dotenv()

SERVERNAME = "My Game"
GAME_SLOGAN = "My Game's cool slogan!"

# TODO: REMOVE THIS - FOR TESTING ONLY TO ALLOW FOR PASSWORDS LIKE "password":
AUTH_PASSWORD_VALIDATORS = []

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
