test = {
  'name': 'wwsd-quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          7026b4496459392f36b9a5b9dc64e31d
          # locked
          scm> (define x 2)
          5ce45267887fa5dae1771a9b64b54929
          # locked
          scm> `(1 x 3)
          7026b4496459392f36b9a5b9dc64e31d
          # locked
          scm> `(1 ,x 3)
          f22d790116f4f90477aa1ae1655e6839
          # locked
          scm> `(1 x ,3)
          7026b4496459392f36b9a5b9dc64e31d
          # locked
          scm> `(1 (,x) 3)
          d6cbc2f9e22d26450e36a1a1389f6877
          # locked
          scm> `(1 ,(+ x 2) 3)
          e5fe7be032d6f20684f70e368a87a802
          # locked
          scm> (define y 3)
          847f7c178da2025ec82e39b01a424bfd
          # locked
          scm> `(x ,(* y x) y)
          92b9752dff87988634b6cb3ff6c6e1c4
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          ce6b93b75a78fd30ce0085c3355afe88
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
