import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the MycoDB data
MycoDB = pd.read_csv('MycoDB.csv')

# Calculate some basic statistics
num_studies = len(MycoDB)
print(f'Number of studies: {num_studies}')

# Calculate the mean and standard deviation of the effect size
effect_size = MycoDB['EFFECTSIZE1']
mean_effect_size = np.mean(effect_size)
std_effect_size = np.std(effect_size)
print(f'Mean effect size: {mean_effect_size:.2f}')
print(f'Standard deviation of effect size: {std_effect_size:.2f}')

# Visualize the distribution of the effect size
sns.histplot(effect_size, kde=True)
plt.xlabel('Effect size')
plt.ylabel('Density')
plt.title('Distribution of effect sizes')
plt.show()

# Visualize the effect size by plant species
sns.boxplot(x='PlantSpecies', y='EFFECTSIZE1', data=MycoDB)
plt.xlabel('Plant species')
plt.ylabel('Effect size')
plt.title('Effect size by plant species')
plt.xticks(rotation=90)
plt.show()