import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df[3:]
print(april_may_june)

orders = pd.read_csv('shoefly.csv')
orders['shoe_source'] = orders.apply(lambda row : "vegan" if row['shoe_material'] != "leather" else "animal", axis=1)

orders['salutation'] = orders.apply(lambda row : "Dear Mr.  " + row.last_name if row.gender=='male' else "Dear Ms. " + row.last_name)

print(orders.head())