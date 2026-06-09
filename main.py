import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

data = {

    'Country': ['Bangladesh', 'China', 'India', 'Philippines', 'Pakistan', 'Indonesia'],

    'Population_Affected_Pct': [55, 28.2, 27.8, 25.0, 20.0, 18.0],

    'Primary_Cause': [

        'Cyclones & Ganges Delta Overflows',

        'Heavy Rainfall & Major River Basins',

        'Intense Monsoons & River Overflows',

        'Typhoons & Coastal Storm Surges',

        'Catastrophic Monsoons & Glacier Melt',

        'Extreme Rains & Rapid Land Subsidence'

    ]

}

df = pd.DataFrame(data)

df = df.sort_values('Population_Affected_Pct', ascending=False).reset_index(drop=True)


plt.figure(figsize=(10, 6))

sns.barplot(x='Population_Affected_Pct', y='Country', data=df, palette='Blues_r', hue='Country')

plt.title('Estimated Percentage of Population Exposed to Severe Flood Risk', fontsize=14, fontweight='bold', pad=15)

plt.xlabel('Percentage of Population (%)', fontsize=12)

plt.ylabel('Country', fontsize=12)

plt.xlim(0, 65)


for i, v in enumerate(df['Population_Affected_Pct']):
    plt.text(v + 1, i, f"{v}%", color='black', va='center', fontweight='bold')

plt.tight_layout()

plt.savefig('population_affected.png', dpi=300)

plt.close()

fig, ax = plt.subplots(figsize=(10, 6))

ax.axis('off')

plt.title('Primary Drivers of Flood Risk by Country', fontsize=16, fontweight='bold', pad=20)

for i, row in df.iterrows():
    ax.text(0.05, 0.9 - int(i) * 0.15, str(row['Country']), fontsize=13, fontweight='bold', va='center',bbox=dict(facecolor='#4a90e2', alpha=0.2, edgecolor='#4a90e2', boxstyle='round,pad=0.6'))

    ax.text(0.32, 0.9 - int(i) * 0.15, '➔', fontsize=18, va='center', color='gray')

    ax.text(0.40, 0.9 - int(i) * 0.15, str(row['Primary_Cause']), fontsize=12, va='center',bbox=dict(facecolor='#e74c3c', alpha=0.15, edgecolor='#e74c3c', boxstyle='round,pad=0.6'))

plt.tight_layout()

plt.savefig('flood_causes.png', dpi=300)

plt.close()

print("Images saved as population_affected.png and flood_causes.png")

