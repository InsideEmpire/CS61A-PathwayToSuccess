test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> s = [6, 7, 8]
          >>> print(s.append(6))
          84065bc2161626528de8ac041e7b4659
          # locked
          >>> s
          ee5bbac9b7c275f4e302977fc4fa36cf
          # locked
          >>> s.insert(0, 9)
          >>> s
          83a4325e933b3579e994d93825052779
          # locked
          >>> x = s.pop(1)
          >>> s
          0796af3f349d61609034bb7d27ec8028
          # locked
          >>> s.remove(x)
          >>> s
          bcfc5b735efb7da84d01a012acd2817d
          # locked
          >>> a, b = s, s[:]
          >>> a is s
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> b == s
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> b is s
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> a.pop()
          1399d9a7e3e505d23edf2a8008d52474
          # locked
          >>> a + b
          75c70659bcfa1183c7fa83ac12489296
          # locked
          >>> s = [3]
          >>> s.extend([4, 5])
          >>> s
          64a560a48df30fb585341a84030995f3
          # locked
          >>> a
          ebbc4ce3f02bb524db6606ccd8bb5438
          # locked
          >>> s.extend([s.append(9), s.append(10)])
          >>> s
          eb32275e5742fa24d3632207e4fe0e18
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
