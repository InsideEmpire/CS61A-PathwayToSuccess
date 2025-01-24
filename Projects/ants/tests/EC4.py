test = {
  'name': 'Problem EC 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> ant = HarvesterAnt(2)
          >>> bee1 = Bee(2)
          >>> bee2 = Bee(2)
          >>> bee3 = Bee(2)
          >>> bee4 = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_0"].add_insect(bee4)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_4"].add_insect(ant)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee3)
          >>> laser.action(gamestate)
          >>> bee4.health
          0.0
          >>> bee1.health
          0.8125
          >>> bee2.health
          0.875
          >>> ant.health
          1.1875
          >>> bee3.health
          1.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> bee1 = Bee(1)
          >>> bee2 = Bee(2)
          >>> bee3 = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_1"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_2"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee3)
          >>> laser.action(gamestate)
          >>> bee1.health
          -0.75
          >>> bee2.health
          0.5625
          >>> bee3.health
          1.875
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> bee1 = Bee(3)
          >>> bee2 = Bee(3)
          >>> bee3 = Bee(3)
          >>> bee4 = Bee(3)
          >>> ant = HarvesterAnt(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_1"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_2"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee3)
          >>> gamestate.places["tunnel_0_4"].add_insect(bee4)
          >>> gamestate.places["tunnel_0_5"].add_insect(ant)
          >>> laser.action(gamestate)
          >>> bee1.health
          1.25
          >>> bee2.health
          1.5625
          >>> bee3.health
          1.875
          >>> bee4.health
          2.1875
          >>> ant.health
          2.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> container_laser = TankAnt()
          >>> bee2 = Bee(3)
          >>> harvester_ant = HarvesterAnt(3)
          >>> container_ant = BodyguardAnt()
          >>> bee3 = Bee(4)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_0"].add_insect(container_laser)
          >>> gamestate.places["tunnel_0_2"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_8"].add_insect(harvester_ant)
          >>> gamestate.places["tunnel_0_8"].add_insect(container_ant)
          >>> gamestate.places["tunnel_0_8"].add_insect(bee3)
          >>> laser.action(gamestate)
          >>> laser.health
          1
          >>> container_laser.health
          0.0
          >>> bee2.health
          1.5625
          >>> container_ant.health
          2
          >>> harvester_ant.health
          3
          >>> bee3.health
          4
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> LaserAnt.implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
