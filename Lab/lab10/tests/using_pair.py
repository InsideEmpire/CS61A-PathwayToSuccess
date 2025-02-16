test = {
  'name': 'using-pair',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '444b726568312f6761d05afbc3ef8701',
          'choices': [
            "Pair('+', Pair('-', Pair(2, Pair(4, Pair(6, Pair(8, nil))))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4))), Pair(6, Pair(8))))",
            'Pair(+, Pair(Pair(-, Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))',
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Write out the Python expression that returns a `Pair` representing the given expression: (+ (- 2 4) 6 8)'
        },
        {
          'answer': '37670e4b00633084aa22d884c6c9326d',
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What is the operator of the previous part's call expression?"
        },
        {
          'answer': 'f691e16231ded18eebfd3f4f5ef545cd',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed in the previous part was bound to the name `p`,
          how would you retrieve the operator?
          """
        },
        {
          'answer': 'df97a47b2518e72a265467bdb7e64aff',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed was bound to the name `p`, 
          how would you retrieve a list containing all of the operands?
          """
        },
        {
          'answer': '47cc7a335c0fc0140c6aabcbbdbce2f6',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How would you retrieve only the first operand?'
        },
        {
          'answer': 'fe8dc26395203a70e6223893495ce598',
          'choices': [
            "'-'",
            "'+'",
            '2',
            '4',
            '-2',
            "Pair('-', Pair(2, Pair(4, nil)))",
            'Pair(2, Pair(4, nil))'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the first operand of the call expression (+ (- 2 4) 6 8) prior to evaluation?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
