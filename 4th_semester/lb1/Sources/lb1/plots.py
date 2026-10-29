import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "/Users/alexander/Library/Developer/Xcode/DerivedData/lb1-gnmlepoenlklobbwwgfxaicarfts/Build/Products/Debug/experiment_results.csv"

print(f"Загружаем файл: {file_path}")

# Загружаем данные
df = pd.read_csv(file_path)
print(f"Загружено {len(df)} записей")
print(f"Колонки: {list(df.columns)}")

# Разделяем по типу
df_dup = df[df['allowDuplicates'] == 1]
df_nodup = df[df['allowDuplicates'] == 0]

# Создание графиков
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle(f'Анализ времени выполнения (N = {df["N"].unique()[0]})', fontsize=16)

# 1. Время (с дубликатами)
ax = axes[0, 0]
time_dup = df_dup[df_dup['success'] == 1].groupby('length')['timeMs'].mean()
ax.plot(time_dup.index, time_dup.values, 'o-', color='blue', linewidth=2, markersize=8)
ax.set_title('С дубликатами (время)')
ax.set_xlabel('Длина списка')
ax.set_ylabel('Время (мс)')
ax.grid(True)
ax.set_xticks([2, 4, 6, 8, 10, 12])

# 2. Время (без дубликатов)
ax = axes[0, 1]
time_nodup = df_nodup[df_nodup['success'] == 1].groupby('length')['timeMs'].mean()
ax.plot(time_nodup.index, time_nodup.values, 's-', color='green', linewidth=2, markersize=8)
ax.set_title('Без дубликатов (время)')
ax.set_xlabel('Длина списка')
ax.set_ylabel('Время (мс)')
ax.grid(True)
ax.set_xticks([2, 4, 6, 8, 10, 12])

# 3. Процент неудач (с дубликатами)
ax = axes[1, 0]
fail_dup = 100 - df_dup.groupby('length')['success'].mean() * 100
ax.bar(fail_dup.index, fail_dup.values, color='red', alpha=0.7)
ax.set_title('Процент неудач (с дубликатами)')
ax.set_xlabel('Длина списка')
ax.set_ylabel('Процент неудач (%)')
ax.grid(True, axis='y')
ax.set_xticks([2, 4, 6, 8, 10, 12])

# 4. Процент неудач (без дубликатов)
ax = axes[1, 1]
fail_nodup = 100 - df_nodup.groupby('length')['success'].mean() * 100
ax.bar(fail_nodup.index, fail_nodup.values, color='orange', alpha=0.7)
ax.set_title('Процент неудач (без дубликатов)')
ax.set_xlabel('Длина списка')
ax.set_ylabel('Процент неудач (%)')
ax.grid(True, axis='y')
ax.set_xticks([2, 4, 6, 8, 10, 12])

plt.tight_layout()
plt.savefig('graph.png')
plt.show()
