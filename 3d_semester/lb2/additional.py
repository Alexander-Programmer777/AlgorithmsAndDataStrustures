
import matplotlib.pyplot as plt
import numpy as np


def generate_clouds(clouds_number=3, N=300):
    clouds = np.zeros((clouds_number * N, 2))

    cloud_params = [[2.5, 2.5, 1.8],
                    [-5.5, -7.5, 2.0],
                    [5.5, -7.5, 1.7]]

    for i in range(clouds_number):
        center_x, center_y, spread = cloud_params[i]
        clouds[i * N: (i + 1) * N, 0] = center_x + spread * np.random.randn(N)
        clouds[i * N: (i + 1) * N, 1] = center_y + spread * np.random.randn(N)

    return clouds


def expand_to_5d(clouds):
    expanded_clouds = np.zeros((len(clouds), 5))

    for i in range(len(clouds)):
        x1, x2 = clouds[i]

        expanded_clouds[i, 0] = x1
        expanded_clouds[i, 1] = x2
        expanded_clouds[i, 2] = x1 + x2
        expanded_clouds[i, 3] = np.log(abs(x1)) + x2
        expanded_clouds[i, 4] = np.sin(x1 * x2)

    return expanded_clouds



def my_PCA(clouds_data):

    mean_values = np.mean(clouds_data, axis=0)
    std_values = np.std(clouds_data, axis=0)
    Z = (clouds_data - mean_values) / std_values   # standardized data => mean = 0, std = 1

    C = 1/(len(Z) - 1) * Z.T @ Z       # Z.T @ Z = matrix 5x5 of dot products between all X_i X_j pairs; n - 1 - несмещенная оценка ковариации

    eigen_values, eigen_vectors = np.linalg.eig(C)
    sorted_indexes = np.argsort(eigen_values)[::-1]
    eigen_vectors = eigen_vectors[:, sorted_indexes]

    res = Z @ eigen_vectors[:, :2]
    return res


def my_KMeans(data, k=3, max_iterations=100, epsilon=1e-6):
    centroid_indexes = np.random.choice(len(data), k, replace=False)
    centroids = data[centroid_indexes].copy()
    clusters = {i: [] for i in range(k)}
    labels = np.zeros(len(data), dtype=int)

    for i in range(max_iterations):
        clusters = {i: [] for i in range(k)}

        for index, x in enumerate(data):
            distances = np.linalg.norm(centroids - x, axis=1)
            nearest_cluster_ind = distances.argmin()
            clusters[nearest_cluster_ind].append(x)
            labels[index] = nearest_cluster_ind

        new_centroids = []
        for cluster_index in range(k):
            points_in_cluster = clusters[cluster_index]
            new_center = np.mean(points_in_cluster, axis=0)
            new_centroids.append(new_center)
        new_centroids = np.array(new_centroids)

        if np.allclose(centroids, new_centroids, atol=epsilon):
            break

        centroids = new_centroids.copy()

    # WCSS finding
    WCSS = 0
    for cluster_index, points in clusters.items():
        centroid = centroids[cluster_index]
        for point in points:
            squared_distance = np.sum((point - centroid) ** 2)
            WCSS += squared_distance

    return clusters, WCSS, labels


def elbow_method(data, max_k=10):
    WCSS_list = []     # Weighted Sum of Squared Centroid Deviations
    for k in range(1, max_k + 1):
        clusters, WCSS, labels = my_KMeans(data, k)
        WCSS_list.append(WCSS)

    return WCSS_list


def draw_plots(original_data, pca_data, clusters, inertias):
    plt.figure(figsize=(15, 8))

    # plot 1
    plt.subplot(2, 2, 1)
    plt.scatter(original_data[:, 0], original_data[:, 1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Исходные данные (2D)')
    plt.grid(True, alpha=0.3)

    # plot 2
    plt.subplot(2, 2, 2)
    plt.scatter(pca_data[:, 0], pca_data[:, 1])
    plt.xlabel('Главная компонента 1')
    plt.ylabel('Главная компонента 2')
    plt.title('Данные после PCA от 5d к 2d')
    plt.grid(True, alpha=0.3)

    # plot 3
    plt.subplot(2, 2, 3)
    plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('K-means кластеризация')
    plt.grid(True, alpha=0.3)

    # plot 4
    plt.subplot(2, 2, 4)
    k_range = range(1, len(inertias) + 1)
    plt.plot(k_range, inertias, 'bo-')
    plt.xlabel('Количество кластеров')
    plt.ylabel('WCSS')
    plt.title('Метод локтя')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    for i in range(10):
        clouds_2d = generate_clouds()
        clouds_5d = expand_to_5d(clouds_2d)
        clouds_PCA = my_PCA(clouds_5d)
        clusters, WCSS, labels = my_KMeans(clouds_PCA)
        WCSS_list = elbow_method(clouds_PCA)

        draw_plots(clouds_2d, clouds_PCA, labels, WCSS_list)