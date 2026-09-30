
import importlib
import pkgutil
from pathlib import Path

def load_plugins(client):
    package = "plugins"
    plugin_dir = Path(__file__).resolve().parent.parent / package
    loaded = []
    for module in pkgutil.iter_modules([str(plugin_dir)]):
        if module.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{package}.{module.name}")
        if hasattr(mod, "setup"):
            mod.setup(client)
        loaded.append(module.name)
    return loaded
