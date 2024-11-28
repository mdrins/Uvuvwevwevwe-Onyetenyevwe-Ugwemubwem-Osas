import pandas as pd
from datetime import datetime

# Funkcija, lai aprēķinātu stundas starp diviem laikiem
def calculate_hours_with_validation(start, end):
    time_format = "%H:%M"
    try:
        start_time = datetime.strptime(start, time_format)
        end_time = datetime.strptime(end, time_format)
        hours_worked = (end_time - start_time).total_seconds() / 3600
        return max(0, hours_worked)  # Nodrošina, ka nav negatīvu vērtību
    except ValueError:
        return 0  # Ja laiks nav derīgs, atgriež 0

# Nolasīt CSV failu
input_file = 'darba_laiki.csv'
data = pd.read_csv(input_file)

# Pievieno nostrādāto stundu kolonnu
data['Nostrādātās_stundas'] = data.apply(
    lambda row: calculate_hours_with_validation(row['Sākums'], row['Beigas']), axis=1
)

# Aprēķina nedēļas kopsummu katram darbiniekam
weekly_hours = data.groupby('Darbinieks')['Nostrādātās_stundas'].sum().reset_index()
weekly_hours.rename(columns={'Nostrādātās_stundas': 'Kopā_stundas'}, inplace=True)

# Nosaka darbinieku ar visvairāk nostrādātajām stundām
most_hours_employee = weekly_hours.loc[weekly_hours['Kopā_stundas'].idxmax()]

# Saglabā rezultātus jaunā CSV failā
output_file = 'darbinieku_stundu_apkopojums.csv'
weekly_hours.to_csv(output_file, index=False)

# Rezultātu izdrukāšana
print("Nostrādāto stundu kopsavilkums:")
print(weekly_hours)
print("\nDarbinieks ar visvairāk nostrādātajām stundām:")
print(f"Darbinieks: {most_hours_employee['Darbinieks']}, Stundas: {most_hours_employee['Kopā_stundas']}")

print(f"\nRezultāti ir saglabāti failā: {output_file}")
