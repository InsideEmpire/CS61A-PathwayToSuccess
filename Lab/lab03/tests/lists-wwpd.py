test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          73a9752b0761167119f7a8667ed17719
          # locked
          >>> s[2]
          1afb89c7c3638fdcfb05bd83099185e5
          # locked
          >>> s[-1]
          73a9752b0761167119f7a8667ed17719
          # locked
          >>> len(s)
          ad741b000d1cc7ef3beaaf650d8f371b
          # locked
          >>> 4 in s
          2c0f80cb8568e3a3420d4ba35d62aaf1
          # locked
          >>> 4 in s[2]
          89004d33a990b56fa372d4458651bf6c
          # locked
          >>> s[2] + [3 + 2]
          8e7dbe880f94dfb6da893a2d87538fb6
          # locked
          >>> 5 in s[2]
          2c0f80cb8568e3a3420d4ba35d62aaf1
          # locked
          >>> s[2] * 2
          67d2e296b226fa45f1c023e600959ff6
          # locked
          >>> list(range(3, 6))
          dd9ca721e5316fb1487def9988d5ca01
          # locked
          >>> range(3, 6)
          92a2e1824db4e21d25feb5639b0fb925
          # locked
          >>> r = range(3, 6)
          >>> [r[0], r[2]]
          a7015b3a9656bcdd8e23b1956be648eb
          # locked
          >>> range(4)[-1]
          c66c489c94f153ccc42909baf6da3202
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
