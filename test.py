from config_simple.config import CONFIG as SIMPLE
from config_dynamic.config import CONFIG as DYNAMIC

print("===SIMPLE====")
print(SIMPLE.get('BASE_URL'))
print(SIMPLE.get('GRID_HUB_URL'))
print(SIMPLE.get('SOME_VAR_YOU_DO_NOT_NEED'))

print("===DYNAMIC====")
print(DYNAMIC.get('BASE_URL'))
print(DYNAMIC.get('GRID_HUB_URL'))
print(DYNAMIC.get('SOME_VAR_YOU_DO_NOT_NEED'))
