from django.db import models

# ------------------------------
# USER MODELI
# ------------------------------
class User(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    yosh = models.IntegerField()
    profil_rasm = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


# ------------------------------
# BLOG MODELI
# ------------------------------
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bloglar")
    nomi = models.CharField(max_length=150)
    rasmi = models.ImageField(upload_to='blog_images/')
    qisqa_tavsif = models.CharField(max_length=255)
    malumot = models.TextField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    # Blog ostidagi commentlarni olish uchun
    @property
    def comments(self):
        return self.izohlar.all()

    # BlogCommentlarni olish uchun
    @property
    def blog_comments(self):
        return self.blog_comments.all()


# ------------------------------
# COMMENT MODELI
# ------------------------------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="izohlar")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="izohlar")
    text = models.TextField()
    yaratilgan_kun = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.blog.nomi}"


# ------------------------------
# BLOGCOMMENT MODELI
# ------------------------------
class tlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user_comments")
    text = models.TextField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.blog.nomi} (tlogComment)"
