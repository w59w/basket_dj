
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)  # количество доступных книг

    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.quantity})"

    def decrease_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.save()

    def increase_quantity(self):
        self.quantity += 1
        self.save()


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order by {self.name} for {self.book.title}"
