from lib.list_comprehension import return_evens, make_exclamation

class TestListComprehension:
    def test_return_evens(self):
        assert return_evens([0, 1, 3, 5, 7, 8, 9]) == [0, 8]
        assert return_evens([1, 3, 5]) == []
        assert return_evens([2, 4, 6]) == [2, 4, 6]
        assert return_evens([]) == []

    def test_make_exclamation(self):
        assert make_exclamation(["Hello", "I'm doing great", "Python is fun"]) == [
            "Hello!",
            "I'm doing great!",
            "Python is fun!",
        ]
        assert make_exclamation([]) == []
        assert make_exclamation(["Wow"]) == ["Wow!"]
