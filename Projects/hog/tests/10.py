test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tail_strategy(40, 51, threshold=7, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 53, threshold=7, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 51, threshold=12, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 52, threshold=7, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = 0
          >>> while s < 100:
          ...     if tail_points(s) >= 10:
          ...         assert tail_strategy(90, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert tail_strategy(90, s, threshold=10, num_rolls=3) == 3
          ...     s += 1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
