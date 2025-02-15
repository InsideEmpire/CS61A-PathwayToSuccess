test = {
  'name': 'my-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4))
          2e37dffeac959437a227984e265073d8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(1 3 5))
          4937c69c365e96f0a6c22b735cfbca8c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(2 4 6 1))
          4fbb2195709ce6677a192b31dd920a41
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter even? '(3))
          7e44d32911eb855f7a970358ab156a57
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? nil)
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
          2e37dffeac959437a227984e265073d8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil)
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
