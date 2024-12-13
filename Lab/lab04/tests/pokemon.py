test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          6958307009d94c1d298ae9f450f606ff
          # locked
          >>> len(pokemon)
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> 'mewtwo' in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'pikachu' in pokemon
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 25 in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 148 in pokemon.values()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 151 in pokemon.keys()
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'mew' in pokemon.keys()
          46d1f016b6482a76a74835354edaab71
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
