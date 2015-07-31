# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from companies.models.company import Company
from common.models.city import City


class CompanyInternshipReview(models.Model):
    user = models.ForeignKey(User, db_index=True)
    company = models.ForeignKey(Company, db_index=True)
    office = models.ForeignKey(City, db_index=True)
    recommendation = models.FloatField()
    apply_skills = models.FloatField()
    learn_new = models.FloatField()
    tasks = models.TextField(null=True, default=None, blank=True)
    most_liked_things = models.TextField(null=True, default=None, blank=True)
    least_liked_things = models.TextField(null=True, default=None, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Review from {} on {}'.format(unicode(self.user), self.date.strftime('%d-%m-%Y %H:%M'))

    class Meta:
        db_table = 'company_internship_review'
        verbose_name = 'Company internship review'
        verbose_name_plural = 'Company internships reviews'
