test = {
  'name': 'Inheritance ABCs',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   x, y = 0, 0
          ...   def __init__(self):
          ...         return
          >>> class B(A):
          ...   def __init__(self):
          ...         return
          >>> class C(A):
          ...   def __init__(self):
          ...         return
          >>> print(A.x, B.x, C.x)
          5dd1d444cfee04cb2069097fa040a660
          # locked
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          cfd0937eea29fcfd259be44001016aed
          # locked
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          49f2632a22ef174bac832e2a2ce85ff9
          # locked
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          e2e33f175e79ff7ff8d44b3176378b5d
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
