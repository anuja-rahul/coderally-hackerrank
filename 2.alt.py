def tallest_tower(N, colors_array):
    # A dictionary to store the highest tower possible ending at each cube and face.
    dp = [[0 for _ in range(6)] for _ in range(N)]
    # A dictionary to track the previous cube and face for reconstructing the tower
    parent = [[(-1, -1) for _ in range(6)] for _ in range(N)]

    # Initialize base case: first cube can start a tower on any face
    for i in range(6):
        dp[0][i] = 1  # The height of a tower starting from cube 0 and face i is 1

    # Iterate over every cube starting from the second cube
    for i in range(1, N):
        # Compare cube i with all previous cubes
        for j in range(i):
            # Check all faces of cube i and cube j
            for face_i in range(6):
                for face_j in range(6):
                    # Check if the face colors match and allow stacking
                    if colors_array[i][face_i] == colors_array[j][(face_j + 3) % 6]:
                        # If a taller tower can be formed by placing cube i on cube j
                        if dp[j][face_j] + 1 > dp[i][face_i]:
                            dp[i][face_i] = dp[j][face_j] + 1
                            parent[i][face_i] = (j, face_j)

    # Now, find the maximum height and the corresponding cube and face
    max_height = 0
    top_cube = -1
    top_face = -1

    for i in range(N):
        for face in range(6):
            if dp[i][face] > max_height:
                max_height = dp[i][face]
                top_cube = i
                top_face = face

    # Mapping face index to face names
    face_names = ["front", "back", "left", "right", "top", "bottom"]

    # Reconstruct the sequence of cubes in the tallest tower
    tower_sequence = []
    current_cube = top_cube
    current_face = top_face

    while current_cube != -1:
        tower_sequence.append((current_cube, face_names[current_face]))  # Store face name
        current_cube, current_face = parent[current_cube][current_face]

    # Reverse the sequence since we built it backwards
    tower_sequence.reverse()

    # Print the tallest tower and the number of cubes in it
    print(tower_sequence)
    return max_height

# Example input
colors_array = [
    (1, 2, 3, 4, 5, 6),
    (2, 3, 4, 5, 6, 7),
    (3, 4, 5, 6, 7, 8),
    (4, 5, 6, 7, 8, 9),
    (5, 6, 7, 8, 9, 10)
]

print(tallest_tower(5, colors_array))