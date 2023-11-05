from django.db import models

class Book(models.Model):
    ACTUALITY = (
        ('Актуален', 'Актуален'),
        ('50 на 50', '50 на 50'),
        ('Стрем', 'Стрем'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class ReviewProgLang(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    title_lang = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Review for {self.title_lang.title}"

