import re

    # Teksts, kuru analizēsim
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

    # Regulārās izteiksmes personvārdiem un organizācijām
person_name_pattern = r'\b[A-Z][a-zāčēģīļņšž]+ [A-Z][a-zāčēģīļņšž]+\b'
organization_pattern = r'\b[A-Z][a-zāčēģīļņšž]+(?: [A-Z][a-zāčēģīļņšž]+)+\b'

    # Atrodam visus iespējamos personvārdus un organizācijas
person_names = re.findall(person_name_pattern, text)
organizations = re.findall(organization_pattern, text)

    # Filtrējam organizācijas, pamatojoties uz specifiskām pazīmēm
organization_filter = [org for org in organizations if "Universitāte" in org or "Akadēmija" in org or "Sabiedrība" in org]
organization_names = [org for org in organizations if org not in organization_filter]

    # Filtrējam personvārdus, lai izslēgtu nepareizas vienības
person_names = [name for name in person_names if name != "Latvijas Universitāte"]

    # Izvadām rezultātus
print("Personvārdi:")
for name in person_names:
  print(f'Frāze: "{name}", Tips: Personvārds')

print("\nOrganizācijas:")
for org in organization_filter:
  print(f'Frāze: "{org}", Tips: Organizācija')
