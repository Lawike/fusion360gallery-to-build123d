from build123d import Sketch, make_face, Line, Circle, Pos, Mode


def fusion360_sequence_to_build123d(fusion360_json: dict) -> list:
    """Creates a sequence of operations between build123d objects from a JSON object describing a sequence of fusion360 CAD operations.

    Args:
        fusion360_json (dict): The JSON object containing the sequence information of the CAD operation performed in fusion360.

    Returns:
        list: The sequence of build123d objects and operations to perform to reconstruct the final CAD model.
    """
    build123d_sequence: list = None

    return build123d_sequence


def fusion360_sketch_to_build123d_sketch(fusion360_sketch: dict) -> Sketch:
    """Creates a Build123D Sketch from a JSON object describing a Fusion360 Sketch.

    Args:
        fusion360_sketch (dict): The JSON Object containing the Fusion360 Sketch data.

    Returns:
        Sketch: A build123d Sketch object
    """
    if fusion360_sketch == None:
        return None

    sketch = Sketch(label=fusion360_sketch["name"])
    # To make a sketch we need to at first create a profile (a closed face) to be abel to operate on it
    for profile_key in fusion360_sketch["profiles"].keys():
        profile = fusion360_sketch["profiles"][profile_key]
        loops = profile["loops"]
        profile = Sketch()
        for loop in loops:
            curves = loop["profile_curves"]
            lines = []
            for curve in curves:
                b3d_curve = process_fusion360_curve(curve)
                lines.append(b3d_curve)
            if loop["is_outer"]:
                profile += make_face(lines)
            else:
                profile -= make_face(lines)
        sketch += profile
    return sketch


def process_fusion360_curve(curve):
    """Process a JSON object representing a Fusion360 curve, depending on its type.

    Args:
        curve (dict): the JSON like object containing the curve informations
    Returns:
        (Compounds): The corresponding build123d object.
    """
    b3d_curve = None
    if curve["type"] == "Circle3D":
        center_point = curve["center_point"]
        b3d_ct_point = (center_point["x"], center_point["y"], center_point["z"])
        b3d_curve = Pos(b3d_ct_point) * Circle(curve["radius"])
    elif curve["type"] == "Line3D":
        start_point = curve["start_point"]
        end_point = curve["end_point"]

        b3d_st_point = (start_point["x"], start_point["y"], start_point["z"])
        b3d_ed_point = (end_point["x"], end_point["y"], end_point["z"])

        b3d_curve = Line([b3d_st_point, b3d_ed_point])
    return b3d_curve
