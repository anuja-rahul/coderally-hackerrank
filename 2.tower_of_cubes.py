
def get_opposite(current_face: str, all_faces: str) -> str:
    face_map = {
        all_faces[0]: all_faces[1],
        all_faces[1]: all_faces[0],
        all_faces[2]: all_faces[3],
        all_faces[3]: all_faces[2],
        all_faces[4]: all_faces[5],
        all_faces[5]: all_faces[4],
    }
    return face_map.get(current_face, "Invalid face")


if __name__ == '__main__':
    number_of_cubes = int(input().strip())
    cube_stack = []

    cube_data = {}
    # 1: 123456
    # 1: FBLRtb

    for i in range(number_of_cubes, 0, -1):
        cube = input().strip()
        cube_data[i] = cube

    cube_id_list = sorted([int(x) for x in cube_data.keys()], reverse=True)
    # cube_id_list = [str(x) for x in cube_id_list]
    # print(cube_id_list)

    current_side = cube_data[cube_id_list[0]][1]    # yata whotto
    cube_stack.append([cube_id_list[0], current_side])
    for i in range(1, len(cube_id_list)):
        if current_side in cube_data[cube_id_list[i]]:
            current_side = get_opposite(current_side, cube_data[cube_id_list[i]])
            cube_stack.append([cube_id_list[i], current_side])
        # current_side = get_opposite(current_side, cube_data[cube_id_list[i]])    # uda whotto
        # print(current_side, cube_id_list[i])

    print(cube_stack[0])
    print(sorted(cube_stack, key=lambda x: x[1]))
    print(cube_stack)
