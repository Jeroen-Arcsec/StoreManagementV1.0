from django import template

register = template.Library()

@register.filter
def addstr(nulls, string):
    if string < 10:
        return "00000" + str(string)
    if 10 <= string < 100:
        return "0000" + str(string)
    if 100 <= string < 1000:
        return "000" + str(string)
    if 1000 <= string < 10000:
        return "00" + str(string)
    if 10000 <= string < 100000:
        return "0" + str(string)
