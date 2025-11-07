import build123d as b3d
from build123d import Sketch, make_face, Line, Circle, Pos, RadiusArc, extrude, Part
from src.curve_type import *    

def fusion360_sequence_to_build123d(fusion360_json: dict) -> list:
    """Creates a sequence of operations between build123d objects from a JSON object describing a sequence of fusion360 CAD operations.

    Args:
        fusion360_json (dict): The JSON object containing the sequence information of the CAD operation performed in fusion360.

    Returns:
        list: The sequence of build123d objects and operations to perform to reconstruct the final CAD model.
    """
    build123d_sequence: list = None

    return build123d_sequence


def fusion360_to_build123d_sketch(fusion360_sketch: dict) -> Sketch:
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

def fusion360_to_build123d_extrude(fusion360_extrude:dict, base_sketch:Sketch):
    """Perform a Build123D extrude operation on an existing Build123D Sketch, it takes the data from a fusion360 extrude operation as parameters.

    Args:
        fusion360_extrude (dict): The fusion360 extrude operation data as a JSON object.
        base_sketch (Sketch): The build123d sketch to be extruded

    Returns:
        Part: A build123d Part object decribing the shape after the extrude operation
    """
    if fusion360_extrude == None:
        return None
    
    both = None

    if fusion360_extrude["extent_type"] == "OneSideFeatureExtentType":
        both = False

    distance = fusion360_extrude["extent_one"]["distance"]["value"]
    taper = fusion360_extrude["extent_one"]["taper_angle"]["value"]

    extruded:Part = extrude(to_extrude=base_sketch, amount=distance, both=both, taper=taper)

    return extruded


def process_fusion360_curve(curve):
    """Process a JSON object representing a Fusion360 curve, depending on its type.

    Args:
        curve (dict): the JSON like object containing the curve informations
    Returns:
        (Compounds): The corresponding build123d object.
    """
    b3d_curve = None
    if curve["type"] == CIRCLE:
        center_point = curve["center_point"]
        b3d_ct_point = (center_point["x"], center_point["y"], center_point["z"])
        b3d_curve = Pos(b3d_ct_point) * Circle(curve["radius"])

    elif curve["type"] == LINE:
        start_point = curve["start_point"]
        end_point = curve["end_point"]

        b3d_st_point = (start_point["x"], start_point["y"], start_point["z"])
        b3d_ed_point = (end_point["x"], end_point["y"], end_point["z"])

        b3d_curve = Line([b3d_st_point, b3d_ed_point])

    elif curve["type"] == ARC:
        start_point = curve["start_point"]
        end_point = curve["end_point"]
        center_point = curve["center_point"]

        b3d_st_point = (start_point["x"], start_point["y"], start_point["z"])
        b3d_ed_point = (end_point["x"], end_point["y"], end_point["z"])

        b3d_curve = RadiusArc(start_point=b3d_st_point, end_point=b3d_ed_point, radius=curve["radius"], short_sagitta=False)

    return b3d_curve
