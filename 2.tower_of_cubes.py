
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

    cube_data = {}
    # 1: 123456
    # 1: FBLRtb

    for i in range(number_of_cubes, 0, -1):
        cube = input().strip()
        cube_data[i] = cube

    cube_id_list = sorted([int(x) for x in cube_data.keys()])
    cube_id_list = [str(x) for x in cube_id_list]
    # print(cube_id_list)

    print(cube_data)
