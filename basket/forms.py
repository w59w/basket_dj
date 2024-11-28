from django import forms
from .models import Order, Book

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'email', 'book']

    def clean_book(self):
        book = self.cleaned_data.get('book')
        if book.quantity <= 0:  # Проверка доступности книги
            raise forms.ValidationError("This book is currently unavailable.")
        return book