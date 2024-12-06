test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tail_points(25)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(52)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(0)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(7)
          15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(22)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(122)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(584)
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = tail_points(23)
          >>> a # check that the value is being returned, not printed
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(12345)
          3
          >>> # ban str and indexing (lists)
          >>> test.check('hog.py', 'tail_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
