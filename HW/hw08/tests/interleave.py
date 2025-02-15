test = {
  'name': 'interleave',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (interleave (list 1 3 5) (list 2 4))
          412c86fdd30eb01c0f6c1406c57c1f4f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 2 4) (list 1 3 5))
          60907ae99fb65ba6572aef8d20f2d98f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 2) (list 1 2))
          97e297aeda7ca131b3ce5d660712ba37
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave '(1 2 3 4 5 6) '(7 8))
          68dcbeaae19114527ba0f3fa3158aa68
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (interleave (list 1 3 5) (list 2 4 6))
          79344590f746836ebf255704a9ec6a23
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (interleave (list 1 3 5) nil)
          4937c69c365e96f0a6c22b735cfbca8c
          # locked
          scm> (interleave nil (list 1 3 5))
          4937c69c365e96f0a6c22b735cfbca8c
          # locked
          scm> (interleave nil nil)
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
