from django.db import models

class Assignment(models.Model):
    """
    This model represents an assignment in the course. It stores its name,
    description, and the fields that make up its rubric.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=40)
    description = models.TextField()


class RubricField(models.Model):
    """
    This is an intermediate model that defines fields w/ weights and
    human readable names for rubrics.
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,
                                   related_name='rubric_fields')

    tag = models.SlugField(max_length=30)
    # This is a number representing the percentage this field takes up wrt
    # the entire assignment grade, from 0.0 to 1.0
    weight = models.FloatField()
    # This is a number representing the percentage the student scored in this
    # category, from 0.0 to 1.0
    value = models.FloatField(default=0.0)
    readable_name = models.CharField(max_length=40)


class AssignmentSubmission(models.Model):
    """
    This model represents the student's completed submission of an assignment.
    It stores the original assignment for reference, as well as the rubric field
    scores, the repository link, the student themself, and the completion
    status.
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,
                                   related_name='submissions')

    graded_rubric_fields = models.ManyToManyField(RubricField)
    repository_url = models.URLField()
    #student = models.ForeignKey() # TODO: Implement Student
    grading_complete = models.BooleanField(default=False)
