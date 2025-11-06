empty_fusion360_data = {
    "metadata": {},
    "timeline": [],
    "entities": {},
    "properties": {},
    "sequence": [],
}


empty_fusion360_sketch_data = {
    "name": "",
    "type": "Sketch",
    "points": {},
    "curves": {},
    "constraints": {},
    "dimensions": {},
    "profiles": {},
    "transform": {},
    "reference_plane": {},
}


square_fusion360_sketch_data = {
    "name": "Square",
    "type": "Sketch",
    "points": {
        "p0": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
        "p1": {"type": "Point3D", "x": 1.0, "y": 0.0, "z": 0.0},
        "p2": {"type": "Point3D", "x": 1.0, "y": 1.0, "z": 0.0},
        "p3": {"type": "Point3D", "x": 0.0, "y": 1.0, "z": 0.0},
    },
    "curves": {
        "c0": {
            "type": "SketchLine",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p0",
            "end_point": "p1",
        },
        "c1": {
            "type": "SketchLine",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p1",
            "end_point": "p2",
        },
        "c2": {
            "type": "SketchLine",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p2",
            "end_point": "p3",
        },
        "c3": {
            "type": "SketchLine",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p3",
            "end_point": "p0",
        },
    },
    "constraints": {},
    "dimensions": {},
    "profiles": {
        "p1": {
            "loops": [
                {
                    "is_outer": True,
                    "profile_curves": [
                        {
                            "type": "Line3D",
                            "start_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 0.0,
                                "z": 0.0,
                            },
                            "end_point": {
                                "type": "Point3D",
                                "x": 1.0,
                                "y": 0.0,
                                "z": 0.0,
                            },
                            "curve": "c0",
                        },
                        {
                            "type": "Line3D",
                            "start_point": {
                                "type": "Point3D",
                                "x": 1.0,
                                "y": 0.0,
                                "z": 0.0,
                            },
                            "end_point": {
                                "type": "Point3D",
                                "x": 1.0,
                                "y": 1.0,
                                "z": 0.0,
                            },
                            "curve": "c1",
                        },
                        {
                            "type": "Line3D",
                            "start_point": {
                                "type": "Point3D",
                                "x": 1.0,
                                "y": 1.0,
                                "z": 0.0,
                            },
                            "end_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 1.0,
                                "z": 0.0,
                            },
                            "curve": "c2",
                        },
                        {
                            "type": "Line3D",
                            "start_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 1.0,
                                "z": 0.0,
                            },
                            "end_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 0.0,
                                "z": 0.0,
                            },
                            "curve": "c3",
                        },
                    ],
                    "properties": {
                        "area": 1,
                        "centroid": {
                            "type": "Point3D",
                            "x": 0.5,
                            "y": 0.5,
                            "z": 0.0,
                        },
                        "perimeter": 4,
                    },
                }
            ]
        }
    },
    "transform": {},
    "reference_plane": {
        "type": "ConstructionPlane",
        "name": "XZ",
        "plane": {
            "type": "Plane",
            "origin": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
            "normal": {"type": "Vector3D", "x": 0.0, "y": 0.0, "z": 1.0, "length": 1.0},
            "u_direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": 1.0,
                "length": 1.0,
            },
            "v_direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 1.0,
                "z": 0.0,
                "length": 1.0,
            },
        },
        "corrective_transform": {
            "origin": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
            "x_axis": {"type": "Vector3D", "x": 1.0, "y": 0.0, "z": 0.0, "length": 1.0},
            "y_axis": {"type": "Vector3D", "x": 0.0, "y": 1.0, "z": 0.0, "length": 1.0},
            "z_axis": {"type": "Vector3D", "x": 0.0, "y": 0.0, "z": 1.0, "length": 1.0},
        },
    },
}

circle_fusion360_sketch_data = {
    "name": "Square",
    "type": "Sketch",
    "points": {
        "p0": {
            "type": "Point3D",
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
        }
    },
    "curves": {
        "c0": {
            "type": "SketchCircle",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "center_point": "p0",
            "radius": 0.5,
        }
    },
    "constraints": {},
    "dimensions": {},
    "profiles": {
        "p0": {
            "loops": [
                {
                    "is_outer": True,
                    "profile_curves": [
                        {
                            "type": "Circle3D",
                            "center_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 0.0,
                                "z": 0.0,
                            },
                            "radius": 0.5,
                            "normal": {
                                "type": "Vector3D",
                                "x": 0.0,
                                "y": 0.0,
                                "z": 1.0,
                                "length": 1.0,
                            },
                            "curve": "c0",
                        }
                    ],
                }
            ]
        }
    },
    "transform": {
        "origin": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
        "x_axis": {"type": "Vector3D", "x": 1.0, "y": 0.0, "z": 0.0, "length": 1.0},
        "y_axis": {"type": "Vector3D", "x": 0.0, "y": 1.0, "z": 0.0, "length": 1.0},
        "z_axis": {"type": "Vector3D", "x": 0.0, "y": 0.0, "z": 1.0, "length": 1.0},
    },
    "reference_plane": {
        "type": "ConstructionPlane",
        "name": "XZ",
        "plane": {
            "type": "Plane",
            "origin": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
            "normal": {"type": "Vector3D", "x": 0.0, "y": 0.0, "z": 1.0, "length": 1.0},
            "u_direction": {
                "type": "Vector3D",
                "x": 1.0,
                "y": 0.0,
                "z": 0.0,
                "length": 1.0,
            },
            "v_direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 1.0,
                "z": 0.0,
                "length": 1.0,
            },
        },
        "corrective_transform": {
            "origin": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
            "x_axis": {"type": "Vector3D", "x": 1.0, "y": 0.0, "z": 0.0, "length": 1.0},
            "y_axis": {"type": "Vector3D", "x": 0.0, "y": 1.0, "z": 0.0, "length": 1.0},
            "z_axis": {"type": "Vector3D", "x": 0.0, "y": 0.0, "z": 1.0, "length": 1.0},
        },
    },
}
