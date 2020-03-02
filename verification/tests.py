"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['ALL UPPER'],
            "answer": True,
        },
        {
            "input": ['all lower'],
            "answer": False,
        },
        {
            "input": ['mixed UPPER and lower'],
            "answer": False,
        },
        {
            "input": [''],
            "answer": True,
        }
    ],
    "Extra": [
        {
            "input": ['Hi'],
            "answer": False,
        },
        {
            "input": ['WORLD'],
            "answer": True,
        }
    ]
}
