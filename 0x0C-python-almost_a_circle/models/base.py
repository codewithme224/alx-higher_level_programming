#!/usr/bin/python3
""" Module for Base class """
import json
import csv
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method """
        if list_objs is None:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string method """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create method """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load_from_file method """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_objs = cls.from_json_string(f.read())
                list_objs = [cls.create(**obj) for obj in list_objs]
                return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv method """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv method """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw method """
        t = turtle.Turtle()
        t.speed(1)
        t.screen.bgcolor("#3C486B")
        t.color("#F2F2F2")
        t.pensize(2)
        t.hideturtle()
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
        turtle.mainloop()
