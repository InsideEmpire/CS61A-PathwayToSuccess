test = {
  'name': 'Problem 8a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'cf13df85d8ffea8b7928c6f0f860c5e1',
          'choices': [
            "In the ContainerAnt's ant_contained instance attribute",
            "In the ContainerAnt's ant_contained class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a ContainerAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Where is the ant contained by a ContainerAnt stored?'
        },
        {
          'answer': '22a2c7eb1d7adee7ea4eb970d3cc09e9',
          'choices': [
            'By protecting the ant from Bees and allowing it to perform its original action',
            'By attacking Bees that try to attack it',
            "By increasing the ant's health",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How does a ContainerAnt guard its ant?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> container = ContainerAnt(1)
          >>> container2 = ContainerAnt(2)
          >>> container3 = ContainerAnt(3)
          >>> throw_long = LongThrower(1)
          >>> container.can_contain(container2)
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> container3.can_contain(throw_long)
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> friend = HungryAnt()
          >>> container.ant_contained is None
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> container.ant_contained is not None
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> friend = HungryAnt()
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(container)
          >>> friend.place = place
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> container.action(gamestate)  # Container holds a HungryAnt that loves to eat!
          >>> bee.health
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> container.can_contain(FireAnt()) # Container already holds another ant!
          03456a09f22295a39ca84d133a26f63d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(1)
          >>> container.action(gamestate) # ContainerAnt does not have an ant contained, should not have any action taken!
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
