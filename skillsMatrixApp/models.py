from django.db import models
from django.urls import reverse


class employee(models.Model):
    firstName = models.CharField(max_length=100, verbose_name="First Name")
    lastName = models.CharField(max_length=100, verbose_name="Last Name")
    role = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('skillsMatrixApp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' - ' + self.role

    class Meta:
        verbose_name_plural = "employee"


class skills(models.Model):
    # employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    skillName = models.CharField(max_length=150, verbose_name="Skill Name")
    technology = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    dateAdded = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    dateModified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    lastModifiedByID = models.CharField(max_length=10, verbose_name="Last Modified By")

    def get_absolute_url(self):
        return reverse('skillsMatrixApp:skills-list')

    def __str__(self):
        return self.skillName + ' - ' + self.technology

    class Meta:
        verbose_name_plural = "skills"


class organization(models.Model):
    organizationEmployee = models.ForeignKey(employee, on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    segment = models.CharField(max_length=100)
    lob = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.lob + ' - ' + self.department + ' - ' + self.team

    class Meta:
        verbose_name_plural = "organization"


class skillsMatrix(models.Model):
    skillsMatrixEmployee = models.ForeignKey(employee, on_delete=models.CASCADE, verbose_name="Employee Name")
    skillsMatrixSkills = models.ForeignKey(skills, on_delete=models.CASCADE, verbose_name="Skill")
    trained = 'No Experience (P0)'
    novice = 'Novice (P1)'
    intermediate = 'Intermediate (P2)'
    advanced = 'Advanced  (P3)'
    superior = 'Superior (P4)'
    proficiency_choice = ((trained, 'No Experience (P0)'),
                          (novice, 'Novice (P1)'),
                          (intermediate, 'Intermediate (P2)'),
                          (advanced, 'Advanced  (P3)'),
                          (superior, 'Superior (P4)'),)
    proficiency = models.CharField(max_length=100
                                   , choices=proficiency_choice)

    noAtAll = 'Not at all interested'
    slightly = 'Slightly interested'
    somewhat = 'Somewhat interested'
    very = 'Very interested'
    extremely = 'Extremely interested'
    interest_choice = ((noAtAll, 'Not at all interested'),
                       (slightly, 'Slightly interested'),
                       (somewhat, 'Somewhat interested'),
                       (very, 'Very interested'),
                       (extremely, 'Extremely interested'),)
    levelOfInterest = models.CharField(max_length=100
                                       , verbose_name="Level Of Interest"
                                       , choices=interest_choice)

    def __str__(self):
        return 'Record ID ' + str(
            self.pk) + ': ' + self.skillsMatrixEmployee.firstName + ' ' + self.skillsMatrixEmployee.lastName + ' - ' + self.proficiency + '/' + self.levelOfInterest

    class Meta:
        verbose_name_plural = "skillsMatrix"

    def get_absolute_url(self):
        return reverse('skillsMatrixApp:skills-matrix')
