# Þurfum þennan
import json

# Tengjumst við skránna bekkur.json (verður að vera til)
with open("bekkur.json","r") as skra:
    gogn = json.load(skra)

# with sér um að loka skránni, skra.close()

# Kíkjum i breytuna gogn
print(gogn)

# Þinn kóði hér til að sækja gögn úr dict (json)
