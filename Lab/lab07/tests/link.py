test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1000)
          >>> link.first
          edb6f8e1ec6e1bc0b2deae8f8cd333bf
          # locked
          >>> link.rest is Link.empty
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> link = Link(1000, 2000)
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> link = Link(1000, Link())
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> link.rest.rest.rest is Link.empty
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> link.first = 9001
          >>> link.first
          2c9f5ddf74d01d9aa3f7f14577718d55
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest is Link.empty
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> link.rest.rest.rest.rest.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link2.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          a353eddb3d8856d2db7bf086df685a3d
          # locked
          >>> print(link)          # Look at the __str__ method of Link
          aa98ad5fd41e907f0178362d6e9cf5b7
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
