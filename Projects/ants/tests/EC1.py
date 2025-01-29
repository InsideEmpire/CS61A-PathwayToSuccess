test = {
  'name': 'Problem EC 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing status parameters
          >>> slow = SlowThrower()
          >>> SlowThrower.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> slow.health
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # slow causes slowness when gamestate.time is odd. bee should take no action (moving or stinging)
          >>> bee.place.name
          46f9851313dc368f747e69f1670450da
          # locked
          >>> gamestate.time += 1
          >>> bee.action(gamestate) # bee is not affected when gamestate.time is even. bee should take its regular action
          >>> bee.place.name
          040b6ad98a7360eba8d493c250a9b82e
          # locked
          >>> for _ in range(5):
          ...    gamestate.time += 1
          ...    bee.action(gamestate)
          >>> bee.place.name # hint: remember that the slow effect wears off after 5 turns. consider how many turns the bee was already affected before the for loop starts.
          7f44338412808161209e944b1ee0f78c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # slow causes slowness when gamestate.time is odd. bee should take no action (moving or stinging)
          >>> bee.place.name
          46f9851313dc368f747e69f1670450da
          # locked
          >>> gamestate.time += 1
          >>> bee.action(gamestate) # bee is not affected when gamestate.time is even. bee should take its regular action
          >>> bee.place.name
          040b6ad98a7360eba8d493c250a9b82e
          # locked
          >>> slow.action(gamestate) # slow throws syrup again. slow's effects will take place for 5 more turns
          >>> for _ in range(5):
          ...    gamestate.time += 1
          ...    bee.action(gamestate)
          >>> bee.place.name
          ba5c35f55ba3229d1eb021382d9d19c5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing that Bee.action was not modified
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate)
          >>> gamestate.time = 1
          >>> Bee.action(bee, gamestate) # uses original Bee.action
          >>> bee.place.name
          'tunnel_0_4'
          >>> gamestate.time += 1
          >>> Bee.action(bee, gamestate) # uses original Bee.action
          >>> bee.place.name
          'tunnel_0_3'
          >>> for _ in range(3):
          ...    gamestate.time += 1
          ...    bee.action(gamestate) # uses original new slowed action
          >>> bee.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing normal Bee movement after Slow effect
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_8"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 0
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_7'
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # Odd time, bee should not move
          >>> bee.place.name
          'tunnel_0_7'
          >>> gamestate.time = 2
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_6'
          >>> gamestate.time = 3
          >>> bee.action(gamestate) # Odd time, bee should not move
          >>> bee.place.name
          'tunnel_0_6'
          >>> gamestate.time = 4
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_5'
          >>> gamestate.time = 5
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_4'
          >>> gamestate.time = 6
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_3'
          >>> gamestate.time = 7
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_2'
          >>> gamestate.time = 8
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_1'
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
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
