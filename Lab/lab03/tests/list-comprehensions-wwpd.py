test = {
  'name': 'Comprehensions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [2 * x for x in range(4)]
          40628ea906dbaef22f25b053c4dd1e1e
          # locked
          >>> [y for y in [6, 1, 6, 1] if y > 2]
          8ae6b17af6c622a7cfbec1195f908e66
          # locked
          >>> [[1] + s for s in [[4], [5, 6]]]
          a22a76380a1633184ba1bf89a1bf4c84
          # locked
          >>> [z + 1 for z in range(10) if z % 3 == 0]
          dbf8e492916cf93036bf7fef23a4c3e0
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
