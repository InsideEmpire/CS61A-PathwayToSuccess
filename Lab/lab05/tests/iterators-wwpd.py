test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Enter StopIteration if StopIteration exception occurs, Error for other errors
          >>> # Enter Iterator if the output is an iterator object.
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          66901ed5775b51743d745870a1a883e3
          # locked
          >>> next(t)
          35926b8dc788659825b34f78c7f76f91
          # locked
          >>> next(t)
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> next(iter(s))
          35926b8dc788659825b34f78c7f76f91
          # locked
          >>> next(iter(s))
          35926b8dc788659825b34f78c7f76f91
          # locked
          >>> next(t)
          74689fcda5421388b764b40ec8de8ccd
          # locked
          >>> next(t)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          # locked
          >>> [x + 1 for x in r]
          650bdb2b36c8f995df90e9ba89bc6296
          # locked
          >>> [x + 1 for x in r_iter]
          d5ac882300cb5dba818dba62ad445078
          # locked
          >>> next(r_iter)
          5ae3a662faab36325ff2515dae9b0edd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          c3fb2b60594bc44d1fb463ee64add7e4
          # locked
          >>> next(map_iter)
          b175ff944106bc551fe6cd7d299a8a62
          # locked
          >>> list(map_iter)
          432189140c9520338be16c9d678a44d5
          # locked
          >>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
          ...     print(e)
          3dab7ee8f513b748e8368e1dbd9ae002
          c4498dd9e0ddf4e9c57b1a6b498e7087
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          7242aed8fdd814d9456c884eda215d73
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
