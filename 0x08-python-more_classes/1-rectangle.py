#!/usr/bin/python3

"""
Define a class Rectangle that can define a rectangle probably
"""


class Rectangle:
        """Rectangle class"""

            def __init__(self, width=0, height=0):
                        """Initialize Rectangle"""
                                self.width = width
                                        self.height = height

                                            @property
                                                def width(self):
                                                            """wow this retrieve the width of Rectangle"""
                                                                    return self.__width

                                                                    @width.setter
                                                                        def width(self, value):
                                                                                    """this sett the width of Rectangle"""
                                                                                            if not isinstance(value, int):
                                                                                                            raise TypeError("width must be an integer")
                                                                                                                if value < 0:
                                                                                                                                raise ValueError("width must be >= 0")
                                                                                                                                    self.__width = value

                                                                                                                                        @property
                                                                                                                                            def height(self):
                                                                                                                                                        """this will retrieve the height of Rectangle"""
                                                                                                                                                                return self.__height

                                                                                                                                                                @height.setter
                                                                                                                                                                    def height(self, value):
                                                                                                                                                                                """this will sett the height of Rectangle"""
                                                                                                                                                                                        if not isinstance(value, int):
                                                                                                                                                                                                        raise TypeError("height must be an integer")
                                                                                                                                                                                                            if value < 0:
                                                                                                                                                                                                                            raise ValueError("height must be >= 0")
                                                                                                                                                                                                                                self
