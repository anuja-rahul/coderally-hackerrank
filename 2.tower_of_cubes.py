import pprint


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
        cube_data[i] = {"front": cube[0], "back": cube[1], "left": cube[2], "right": cube[3],
                        "top": cube[4], "bottom": cube[5]}

    pprint.pprint(cube_data)


