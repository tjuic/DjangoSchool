from django.db import models

class Score(models.Model):       #name as 'Score'

    allSubject = (('Math', 'Math'),
                  ('Science', 'Science'),
                  ('Computer', 'Computer'),
                  ('Physical Edu', 'Physical Edu'),
                  ('Art', 'Art'),
                  ('Physics', 'Physics'),
                  ('Biology', 'Biology'),
                  ('English', 'English'))

    subject = models.CharField(max_length=200, choices=allSubject, default='Math')
    student_name = models.CharField(max_length=200)     #what type of info, char info
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name + '-' + self.subject + '-' + str(self.score)
