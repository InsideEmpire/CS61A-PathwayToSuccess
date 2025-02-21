test = {
  'name': 'by_parent_height',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM by_parent_height;
          hank
          finn
          ace
          daisy
          ginger
          bella
          charlie
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
