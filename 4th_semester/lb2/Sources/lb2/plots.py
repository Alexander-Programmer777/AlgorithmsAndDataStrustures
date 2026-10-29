import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/alexander/Library/Developer/Xcode/DerivedData/lb2-cfxwlfijkbamtcfjqsumsybfekpg/Build/Products/Debug/tsp_experiment_results.csv"

print(f"Загружаем файл: {file_path}")
df = pd.read_csv(file_path)
print(f"Загружено {len(df)} записей")
print(f"Колонки: {list(df.columns)}")

# Группировка по N
grouped = df.groupby('N')

avg_time = grouped['timeMs'].mean()
avg_steps = grouped['steps'].mean()

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Зависимость времени и числа шагов от размера N', fontsize=16)

# 1. Время от N
ax = axes[0]
ax.plot(avg_time.index, avg_time.values, 'o-', color='blue', linewidth=2, markersize=6)
ax.set_title('Среднее время решения')
ax.set_xlabel('N')
ax.set_ylabel('Время (мс)')
ax.grid(True)

# 2. Шаги от N
ax = axes[1]
ax.plot(avg_steps.index, avg_steps.values, 's-', color='green', linewidth=2, markersize=6)
ax.set_title('Среднее количество шагов')
ax.set_xlabel('N')
ax.set_ylabel('Шаги')
ax.grid(True)

plt.tight_layout()
plt.savefig('tsp_graphs.png')
plt.show()
