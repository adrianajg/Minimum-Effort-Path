import pytest
from graphs.minimum_effort_path import *

@pytest.mark.skip(reason="some reason")
def test_initialize_result_dict():
    # Arrange
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

    # Act
    answer = initialize_result_dict(heights, 0)

    # Assert
    assert answer == {
        "previous": [None, None, None, None, None, None, None, None, None],
        "heights": [
            0,
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
        ],
    }


def test_create_empty_graph():
    # Arrange
    num_nodes = 3

    # Act
    answer = create_empty_graph(num_nodes)

    # Assert
    assert answer == [
        [float('inf'), float('inf'), float('inf')], 
        [float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf')]
    ]

def test_given_i_j_adjust_node_num_height_diffs():
    # Arrange
    i = 0 
    j = 1
    heights = [
        [4, 2],
        [3, 8]
    ]
    row = [0, 0, 0, 0]
    # Act
    given_i_j_adjust_node_num_height_diffs(i, j, heights, row)

    # Assert
    assert row == [2, 0, 0, 6]

def test_create_graph():
    # Arrange
    heights = [
        [4, 2],
        [3, 8]
    ]
    # Act
    graph = create_graph(heights)

    # Assert
    assert graph == [
        [float('inf'), 2, 1, float('inf')],
        [2, float('inf'), float('inf'), 6],
        [1, float('inf'), float('inf'), 5],
        [float('inf'), 6, 5, float('inf')]
    ]

def test_create_graph_2():
    # Arrange
    heights = [
        [4, 2],
        [4, 8]
    ]
    # Act
    graph = create_graph(heights)

    # Assert
    assert graph == [
        [float('inf'), 2, 0, float('inf')],
        [2, float('inf'), float('inf'), 6],
        [0, float('inf'), float('inf'), 4],
        [float('inf'), 6, 4, float('inf')]
    ]

def test_create_min_distances_dict_1():
    # Arrange
    heights = [
        [4, 2],
        [3, 8]
    ]
    # Act
    result = create_min_heights_dict(heights)

    # Assert
    assert result == {
        "min_heights": [float('inf'), 2, 1, 5],
        "previous": [None, 0, 0, 2]
    }

# @pytest.mark.skip(reason="UGH")
def test_create_min_distances_dict_2():
    # Arrange
    heights = [
        [1,1,2],
        [2,1,2],
        [2,1,1]
    ]
    # Act
    result = create_min_heights_dict(heights)

    # Assert
    assert result == {
        "min_heights": [float('inf'), 0, 1, 1, 0, 1, 1, 0, 0],
        "previous": [None, 0, 1, 0, 1, 4, 7, 4, 7]
    }

@pytest.mark.skip(reason="not ready to test this feature")
def test_will_return_min_effort_path_for_first_example():
    # Arrange
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 2


@pytest.mark.skip(reason="not ready to test this feature")
def test_will_return_min_effort_for_second_example():
    # Arrange
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 1


@pytest.mark.skip(reason="not ready to test this feature")
def test_will_return_min_effort_for_third_example():
    # Arrange
    heights = [
        [1, 2, 1, 1, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 1, 2, 1],
    ]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 0


@pytest.mark.skip(reason="not ready to test this feature")
def test_will_return_zero_for_empty_graph():
    # Arrange
    heights = None

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 0


@pytest.mark.skip(reason="not ready to test this feature")
def test_will_return_min_effort_for_rectangular_grid():
    # Arrange
    heights = [
        [1, 2, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 3],
        [1, 2, 1, 2, 1, 3],
        [1, 1, 1, 2, 1, 2],
    ]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 1
