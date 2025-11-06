from build123d import *
from src.f360_to_b123d import *
from mock_data.mock_data_f360 import (
    empty_fusion360_data,
    empty_fusion360_sketch_data,
    square_fusion360_sketch_data,
    circle_fusion360_sketch_data,
)


from ocp_vscode import show


# ---------------------------------------------------------------------------------
# Test fusions360_to_build123d function
def test_fusion360_to_build123d_dummy() -> None:
    build123d_sequence = fusion360_sequence_to_build123d(None)

    assert build123d_sequence == None


# ---------------------------------------------------------------------------------
# Test fusions360_sketch_to_build123d function
def test_fusion360_sketch_to_build123d_dummy() -> None:
    build123d_sketch = fusion360_sketch_to_build123d_sketch(None)

    assert build123d_sketch == None


def test_fusion360_sketch_to_build123d_empty() -> None:
    build123d_sketch = fusion360_sketch_to_build123d_sketch(empty_fusion360_sketch_data)

    assert isinstance(build123d_sketch, Sketch)


# Manually checked 06/11/2025
def test_fusion360_sketch_to_build123d_square() -> None:
    build123d_sketch = fusion360_sketch_to_build123d_sketch(
        square_fusion360_sketch_data
    )
    show(build123d_sketch)
    assert True


# Manually checked 06/11/2025
def test_fusion360_sketch_to_build123d_circle() -> None:
    build123d_sketch = fusion360_sketch_to_build123d_sketch(
        circle_fusion360_sketch_data
    )
    show(build123d_sketch)
    assert True
