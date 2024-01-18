import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)

# Subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.jointplot(x=x, y=y, kind="hex", color="#4CB391", ax=axes[0])

# verde invertidos
sns.jointplot(x=x, y=y, kind="hex", cmap="Greens_r", ax=axes[1])

plt.tight_layout()
plt.show()
