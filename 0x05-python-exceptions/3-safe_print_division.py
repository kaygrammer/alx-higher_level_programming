#!/usr/bin/python3


def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("inside result: {}".format(div))
        return div
