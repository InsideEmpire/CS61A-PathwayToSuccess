test = {
  'name': 'ascending?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          545654f52801dba9cbbe0347d265df09
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          8cd49ce066289d3b150d7b6108dda61e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          545654f52801dba9cbbe0347d265df09
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          8cd49ce066289d3b150d7b6108dda61e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '())  ; #t or #f
          545654f52801dba9cbbe0347d265df09
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
