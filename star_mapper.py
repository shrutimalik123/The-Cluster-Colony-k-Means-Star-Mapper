import math

def kmeans_star_game():
    # 1. Scenario: Deep-Space Exploration
    print("--- 🌌 THE CLUSTER COLONY: K-MEANS STAR MAPPER 🌌 ---")
    print("Mission: Group unknown stars into clusters using spatial distances.")
    print("Goal: Assign an anomaly to the nearest gravitational center (Centroid).")

    # 2. Unlabeled Spatial Data: Stars mapped by [Brightness, Temperature]
    stars = [
        [1.5, 2.0], [2.0, 1.5], [1.8, 2.5],  # System alpha (Low/Low)
        [8.5, 9.0], [9.0, 8.0], [8.8, 9.5],  # System beta (High/High)
    ]
    
    print("\n--- 🖥️ STAR COORDINATE MAP (UNLABELED DATA) ---")
    for idx, s in enumerate(stars):
        print(f"Object {idx+1}: Brightness = {s[0]} | Temperature = {s[1]}")

    # 3. Game Inputs: Setting the initial positions of the 2 Centroids (K=2)
    print("\n--- STEP 1: DEPLOY GRAVITATIONAL CENTROIDS (K=2) ---")
    print("Where should your 2 cluster tracking hubs begin searching?")
    try:
        c1_x = float(input("Centroid 1 Brightness guess (e.g., 0.0): "))
        c1_y = float(input("Centroid 1 Temperature guess (e.g., 0.0): "))
        
        c2_x = float(input("\nCentroid 2 Brightness guess (e.g., 10.0): "))
        c2_y = float(input("Centroid 2 Temperature guess (e.g., 10.0): "))
    except ValueError:
        c1_x, c1_y = 0.0, 0.0
        c2_x, c2_y = 10.0, 10.0

    centroid1 = [c1_x, c1_y]
    centroid2 = [c2_x, c2_y]

    # 4. Incoming Critical Object
    target_star = [2.2, 2.8]
    print(f"\n--- 🚨 TELEMETRY ALERT: UNCHARTED STAR DETECTED ---")
    print(f"Target Object Profile -> Brightness: {target_star[0]} | Temperature: {target_star[1]}")

    # 5. The Math: Calculating Euclidean Distance
    # Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    print("\n--- 🔄 COMPUTING EUCLIDEAN SPATIAL DISTANCES ---")
    
    dist_to_c1 = math.sqrt((target_star[0] - centroid1[0])**2 + (target_star[1] - centroid1[1])**2)
    dist_to_c2 = math.sqrt((target_star[0] - centroid2[0])**2 + (target_star[1] - centroid2[1])**2)
    
    print(f"Distance to Centroid 1 Hub: {dist_to_c1:.2f}")
    print(f"Distance to Centroid 2 Hub: {dist_to_c2:.2f}")

    # 6. Cluster Assignment Step
    if dist_to_c1 < dist_to_c2:
        assigned_cluster = 1
        verdict = "💫 SYSTEM ALPHA (COLD & DIM DWARF CLUSTER)"
    else:
        assigned_cluster = 2
        verdict = "🔥 SYSTEM BETA (HOT & BRIGHT GIANT CLUSTER)"

    print(f"\nModel Cluster Assignment: Point assigned to {verdict}")

    # 7. Ground Truth Evaluation
    # Visually, [2.2, 2.8] aligns natively closer to the System Alpha cluster pool
    actual_cluster = 1
    
    if assigned_cluster == actual_cluster:
        print("\n🏆 SUCCESS: Your Centroid configurations correctly mapped the constellation!")
        print("The star has been successfully categorized with its astronomical siblings.")
    else:
        print("\n💥 SYSTEM MISMATCH: Poor initialization! Your tracking centers distorted space coordinates.")

if __name__ == "__main__":
    kmeans_star_game()
