import uuid, os, importlib
from config import blueprints_dir

def unique_id():
    return uuid.uuid4().hex

def filter_bp(bp):
    return "__" not in bp

def import_module(bp_name):
    mod_str = 'blueprints.%s' % bp_name
    the_mod = importlib.import_module(mod_str)
    return getattr(the_mod, bp_name)

def load_blueprints():
    blueprint_files = os.listdir(blueprints_dir)
    blueprints_wanted = list(filter(filter_bp, blueprint_files))
    blueprint_module_names = list(map(lambda x: x.split(".")[0], blueprints_wanted))
    modules = list(map(import_module, blueprint_module_names))
    return modules 

    



    




