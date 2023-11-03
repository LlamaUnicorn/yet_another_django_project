from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    """
    Represents a book in the book store.

    Args:
        title (str): The title of the book.
        rating (int): The rating of the book (1-5).
        author (str, optional): The author of the book.
        is_bestselling (bool, optional): Indicates if the book is a bestseller.

    Returns:
        str: A string representation of the book.

    Examples:
        >>> book = Book(title="The Great Gatsby", rating=4, author="F. Scott Fitzgerald")
        >>> str(book)
        "The Great Gatsby (4)"
    """

    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
