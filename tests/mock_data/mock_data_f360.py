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
    "name": "Circle",
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

curved_face_fusion360_sketch_data = {
    "name": "Curved Face",
    "type": "Sketch",
    "points": {
        "p0": {"type": "Point3D", "x": 0.0, "y": 0.0, "z": 0.0},
        "p1": {"type": "Point3D", "x": 1.0, "y": 0.0, "z": 0.0},
        "p2": {"type": "Point3D", "x": 1.0, "y": 1.0, "z": 0.0},
        "p3": {"type": "Point3D", "x": 0.5, "y": 1.0, "z": 0.0},
        "p4": {"type": "Point3D", "x": 0.0, "y": 1.0, "z": 0.0},
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
            "type": "SketchArc",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p2",
            "end_point": "p4",
            "center_point": "p3",
            "radius": 0.5,
            "reference_vector": {
                "type": "Vector3D",
                "x": 1,
                "y": 0,
                "z": 0.0,
                "length": 1.0
            },
            "start_angle": 0.0,
            "end_angle": 0.0
        },
        "c3": {
            "type": "SketchLine",
            "construction_geom": False,
            "fixed": False,
            "fully_constrained": False,
            "reference": False,
            "visible": True,
            "start_point": "p4",
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
                            "type": "Arc3D",
                            "start_point": {
                                "type": "Point3D",
                                "x": 1.0,
                                "y": 1.0,
                                "z": 0.0
                            },
                            "end_point": {
                                "type": "Point3D",
                                "x": 0.0,
                                "y": 1.0,
                                "z": 0.0
                            },
                            "center_point": {
                                "type": "Point3D",
                                "x": 0.5,
                                "y": 1.0,
                                "z": 0.0
                            },
                            "radius": 0.5,
                            "normal": {
                                "type": "Vector3D",
                                "x": 0.0,
                                "y": 0.0,
                                "z": 1.0,
                                "length": 1.0
                            },
                            "start_angle": 0.0,
                            "end_angle": 0,
                            "reference_vector": {
                                "type": "Vector3D",
                                "x": 1,
                                "y": 0,
                                "z": 0.0,
                                "length": 1.0
                            },
                            "curve": "c2"
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

cube_fusion360_data = {
    "entities":  {
        "sketch0": square_fusion360_sketch_data,
        "extrude0": {
            "name": "Extrude0",
            "type": "ExtrudeFeature",
            "profiles": [
                {
                    "profile": "p0",
                    "sketch": "sketch0"
                }
            ],
            "operation": "NewBodyFeatureOperation",
            "start_extent": {
                "type": "ProfilePlaneStartDefinition"
            },
            "extent_type": "OneSideFeatureExtentType",
            "extent_one": {
                "distance": {
                    "type": "ModelParameter",
                    "value": 1,
                    "name": "d3",
                    "role": "AlongDistance"
                },
                "taper_angle": {
                    "type": "ModelParameter",
                    "value": 0.0,
                    "name": "d4",
                    "role": "TaperAngle"
                },
                "type": "DistanceExtentDefinition"
            },
            "faces": {
                "d1f49562-e29c-11ea-acd1-54bf646e7e1f": {
                    "index": 0,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 6.35,
                        "y": 5.08,
                        "z": 1.27
                    }
                },
                "d1f4bc6e-e29c-11ea-94d8-54bf646e7e1f": {
                    "index": 1,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 12.7,
                        "y": 2.54,
                        "z": 1.27
                    }
                },
                "d1f4e37a-e29c-11ea-81ed-54bf646e7e1f": {
                    "index": 2,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 6.35,
                        "y": 0.0,
                        "z": 1.27
                    }
                },
                "d1f50a8c-e29c-11ea-be9c-54bf646e7e1f": {
                    "index": 3,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 2.54,
                        "z": 1.27
                    }
                },
                "d1f5319e-e29c-11ea-9253-54bf646e7e1f": {
                    "index": 4,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 6.35,
                        "y": 2.54,
                        "z": 2.54
                    }
                },
                "d1f558b0-e29c-11ea-8c5a-54bf646e7e1f": {
                    "index": 5,
                    "surface_type": "PlaneSurfaceType",
                    "point_on_face": {
                        "type": "Point3D",
                        "x": 6.35,
                        "y": 2.54,
                        "z": 0.0
                    }
                }
            },
            "bodies": {
                "d1f46e2e-e29c-11ea-964e-54bf646e7e1f": {
                    "index": 0,
                    "name": "Body1",
                    "faces": [
                        "d1f49562-e29c-11ea-acd1-54bf646e7e1f",
                        "d1f4bc6e-e29c-11ea-94d8-54bf646e7e1f",
                        "d1f4e37a-e29c-11ea-81ed-54bf646e7e1f",
                        "d1f50a8c-e29c-11ea-be9c-54bf646e7e1f",
                        "d1f5319e-e29c-11ea-9253-54bf646e7e1f",
                        "d1f558b0-e29c-11ea-8c5a-54bf646e7e1f"
                    ]
                }
            },
            "extrude_bodies": [
                "d1f46e2e-e29c-11ea-964e-54bf646e7e1f"
            ],
            "extrude_faces": [
                "d1f4bc6e-e29c-11ea-94d8-54bf646e7e1f",
                "d1f558b0-e29c-11ea-8c5a-54bf646e7e1f",
                "d1f49562-e29c-11ea-acd1-54bf646e7e1f",
                "d1f4e37a-e29c-11ea-81ed-54bf646e7e1f",
                "d1f50a8c-e29c-11ea-be9c-54bf646e7e1f",
                "d1f5319e-e29c-11ea-9253-54bf646e7e1f"
            ],
            "extrude_side_faces": [
                "d1f4bc6e-e29c-11ea-94d8-54bf646e7e1f",
                "d1f49562-e29c-11ea-acd1-54bf646e7e1f",
                "d1f4e37a-e29c-11ea-81ed-54bf646e7e1f",
                "d1f50a8c-e29c-11ea-be9c-54bf646e7e1f"
            ],
            "extrude_end_faces": [
                "d1f5319e-e29c-11ea-9253-54bf646e7e1f"
            ],
            "extrude_start_faces": [
                "d1f558b0-e29c-11ea-8c5a-54bf646e7e1f"
            ]
        }
    }
}

cylinder_fusion360_data = {
    "metadata": {
    },
    "timeline": [
        {
            "index": 0,
            "entity": "sketch0"
        },
        {
            "index": 1,
            "entity": "extrude0"
        },
    ],
    "entities": {
        "sketch0": {
            "name": "Sketch0",
            "type": "Sketch",
            "points": {
                "p0": {
                    "type": "Point3D",
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0
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
                    "radius": 1
                }
            },
            "profiles": {
                "f0": {
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
                                        "z": 0.0
                                    },
                                    "radius": 1,
                                    "normal": {
                                        "type": "Vector3D",
                                        "x": 0.0,
                                        "y": 0.0,
                                        "z": 1.0,
                                        "length": 1.0
                                    },
                                    "curve": "c0"
                                }
                            ]
                        }
                    ],
                }
            },
            "reference_plane": {
                "type": "ConstructionPlane",
                "name": "XZ",
                "plane": {
                    "type": "Plane",
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "normal": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 1.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "u_direction": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 1.0,
                        "length": 1.0
                    },
                    "v_direction": {
                        "type": "Vector3D",
                        "x": 1.0,
                        "y": 0.0,
                        "z": 0.0,
                        "length": 1.0
                    }
                },
                "corrective_transform": {
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "x_axis": {
                        "type": "Vector3D",
                        "x": 1.0,
                        "y": 0.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "y_axis": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 1.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "z_axis": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 1.0,
                        "length": 1.0
                    }
                }
            }
        },
        "extrude0": {
            "name": "Extrude0",
            "type": "ExtrudeFeature",
            "profiles": [
                {
                    "profile": "f0",
                    "sketch": "sketch0"
                }
            ],
            "operation": "NewBodyFeatureOperation",
            "start_extent": {
                "type": "ProfilePlaneStartDefinition"
            },
            "extent_type": "OneSideFeatureExtentType",
            "extent_one": {
                "distance": {
                    "type": "ModelParameter",
                    "value": 1.0,
                    "name": "d0",
                    "role": "AlongDistance"
                },
                "taper_angle": {
                    "type": "ModelParameter",
                    "value": 0.0,
                    "name": "d1",
                    "role": "TaperAngle"
                },
                "type": "DistanceExtentDefinition"
            },
            "faces": {
            },
            "bodies": {
            },
            "extrude_bodies": [
            ],
            "extrude_faces": [
            ],
            "extrude_side_faces": [
            ],
            "extrude_end_faces": [
            ],
            "extrude_start_faces": [
            ]
        },
    },
    "properties": {
    },
    "sequence": [
        {
            "index": 0,
            "type": "Sketch",
            "entity": "sketch0",
            "curve": "c0",
            "timeline": 0
        },
        {
            "index": 1,
            "type": "ExtrudeFeature",
            "entity": "extrude0",
            "timeline": 1,
        }
    ]
}