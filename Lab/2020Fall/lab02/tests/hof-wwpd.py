test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> steven = lambda x: x
          >>> stewart = even(steven)
          >>> stewart
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> stewart(61)
          fca276f013f718468273f07db52f3ab7
          # locked
          >>> stewart(-4)
          ef6b0e7c554b5515158e88d1ee908645
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          0127137631d037670fa6a894e2d548ee
          # locked
          >>> chocolate
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> chocolate()
          28f5a700252060ec3bbc4bf4ca744c56
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          28f5a700252060ec3bbc4bf4ca744c56
          # locked
          >>> more_chocolate
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> snake(10, 20)()
          28f5a700252060ec3bbc4bf4ca744c56
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          c06666e98ec36af7add28e636f1488ee
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
