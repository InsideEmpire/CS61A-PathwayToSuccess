test = {
  'name': 'Extra Credit',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '4ab45f3b1ed6f2410bd43900b0d4ce6c',
          'choices': [
            'A type of design pattern',
            'A function that takes another function as an input and returns a new function that extends or modifies the behavior of the original function',
            'A method for declaring class properties',
            'A way to loop through an iterable'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is a decorator in Python?'
        },
        {
          'answer': 'b0d3e0af1a561c121fccba84d0661b3a',
          'choices': [
            'To add functionality to existing code',
            'To loop through arrays',
            'To declare variables',
            'To check for syntax errors in code'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Why do we use decorators in Python?'
        },
        {
          'answer': '034e5b537c8688d20accd6b4855b563a',
          'choices': [
            'Using the "#" symbol before the function',
            'By passing the decorator as a parameter to the function',
            'Using the "@decorator_name" syntax above the function definition',
            'By importing the decorator from a library'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How is a decorator applied to a function?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def my_decorator(func):
          ...   def wrapper():
          ...       print("Say Hello")
          ...       func()
          ...       print("Say Goodbye")
          ...   return wrapper
          
          >>> @my_decorator
          ... def say_hello():
          ...     print("Hello World")
          
          >>> say_hello()
          ee08fbbaadc005f518c9734ebaad6d62
          10e7a47b024506544a6149ffb292a283
          e1b47d1e24b420693a5874252bbe6018
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        },
        {
          'code': r"""
          >>> def magic_decorator(func):
          ...   def wrapper(x):
          ...     return func(x * 2)
          ...   return wrapper
          
          >>> @magic_decorator
          ... def myfunc(x):
          ...   return x * 3
          
          >>> print(myfunc(4))
          f972bfb90199a6a9af3501f0c47d4ef8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations.call_count = 0
          >>> minimum_mewtations("rlogcul", "logical", big_limit)    # rlogcul -> logcul -> logicul -> logical
          3
          >>> minimum_mewtations.call_count <= 350    # see if you removed redundant recursive calls
          True
          >>> minimum_mewtations.call_count = 0
          >>> minimum_mewtations("ckiteus", "kittens", big_limit)
          3
          >>> minimum_mewtations.call_count <= 320
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # check that you're only using the minimum_mewtations func
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "abc", "def", 3)
          ...     output = buf.getvalue()
          >>> lines = [line for line in output.split('\n') if 'funcname' in line]
          >>> func_names = set([l.split(",")[1].split(":")[1].strip() for l in lines])
          >>> func_names == {'counted', 'minimum_mewtations', 'memoized'}   # make sure you are not using any helper functions
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)
          'well'
          >>> minimum_mewtations.call_count <= 72000    # minimum_mewtations should be memoized
          True
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, furry_fixes, 4)
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)  # identical to the first call
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 3)
          'well'
          >>> minimum_mewtations.call_count < 2500
          True
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", all_words, minimum_mewtations, 2)
          'will'
          >>> minimum_mewtations.call_count < 2700000
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file
      >>> all_words = lines_from_file("data/words.txt")
      >>> common_words = lines_from_file("data/common_words.txt")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
