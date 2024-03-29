
dule for say_my_name method."""


def say_my_name(first_name, last_name=""):
        """Prints the first and last name.

            Args:
                        first_name: String representing the first name.
                                last_name: String representing the last name.

                                    Raises:
                                                TypeError: If first_name is not a string.
                                                        TypeError: If last_name is not a string.
                                                            """
                                                                if not isinstance(first_name, str):
                                                                        raise TypeError("first_name must be a string")

                                                                            if not isinstance(last_name, str):
                                                                                    raise TypeError("last_name must be a string")

                                                                                        print("My name is {:s} {:s}".format(first_name, last_name))

                                                                                        if __name__ == "__main__":
                                                                                            import doctest
                                                                                                doctest.testfile("tests/3-say_my_name.txt")
