test = {
  'name': 'sentences',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sentences;
          The two siblings, bella and charlie, have the same size: standard
          The two siblings, ace and ginger, have the same size: toy
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
