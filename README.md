# 🌌 The Cluster Colony: k-Means Star Mapper

An interactive, unsupervised Machine Learning simulation designed to teach **k-Means Clustering** and spatial distance geometry from scratch. You play as an Astrophysicist charting an uncharted sector of deep space, deploying coordinate tracking hubs (Centroids) to group unknown celestial anomalies based purely on their structural Euclidean similarities.

## 🎓 Learning Objectives

This project focuses on teaching:
* **Unsupervised Learning:** Finding underlying structural relationships and data patterns in raw datasets without historical target labels.
* **k-Means Clustering:** An iterative spatial partitioning algorithm that groups multi-dimensional data arrays into *k* distinct clusters.
* **Gravitational Centroids:** The geometric center point of an assigned cluster space that dictates the boundaries of nearby records.
* **Euclidean Metric Calculations:** Computing the direct, straight-line spatial distance between data vectors using foundational coordinate geometry.

---

## ✨ Features

* **Deep-Space Cartography Scenario:** Bridges the gap between abstract vector mathematics and an intuitive interstellar navigation game.
* **Dynamic Coordinate Proximity Tracking:** Details the exact step-by-step Euclidean distances computed from the testing node to each user hub.
* **Interactive Hub Placement:** Allows players to manually guess starting coordinate arrays to witness firsthand how initialization coordinates alter algorithmic success.
* **Zero Module Dependencies:** Written from scratch using standard Python math definitions, skipping heavy geospatial matrices or standard machine learning imports.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed.

### 2. Setup and Execution
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/cluster-colony-kmeans.git](https://github.com/YOUR_USERNAME/cluster-colony-kmeans.git)
    cd cluster-colony-kmeans
    ```
2.  **Save the Code:** Save the provided script as `star_mapper.py`.
3.  **Run the Script:**
    ```bash
    python star_mapper.py
    ```

### 3. Gameplay Instructions
1.  **Read Telescope Feed:** Examine the structural baseline coordinates (Brightness vs. Temperature) of known reference stars.
2.  **Deploy Cluster Centroids:** Choose coordinates for Centroid Hub 1 and Centroid Hub 2 to serve as your gravitational anchors.
3.  **Intercept Uncharted Matter:** Track the system as it reads a novel borderline star profile.
4.  **Analyze Spatial Distances:** Observe the Euclidean proximity scores to verify if your centroids assigned the anomaly to its proper solar system.

---

## 🧠 Code Structure Highlights

### Euclidean Distance Formula
The mathematical engine measures point-to-centroid similarity by calculating the hypotenuse across spatial properties.

```python
# Euclidean Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
dist_to_c1 = math.sqrt((target_star[0] - centroid1[0])**2 + (target_star[1] - centroid1[1])**2)
