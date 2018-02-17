from django.db import models


class Numbers(models.Model):
    def numbers_sort(q):
        n = q.replace(',', '')
        if n.isdigit():
            n = q.split(",")
            n.sort(key=int)
            numbers = ","
            message = numbers.join(n)
        else:
            message = 'Złe dane!'
        return message
