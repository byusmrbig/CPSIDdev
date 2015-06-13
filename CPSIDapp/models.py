from django.db import models

# Create your models here.

class Groups(models.Model):
	GroupName = models.CharField(max_length=1024)
	Email = models.CharField(max_length=1024)
	GroupAddress = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.GroupName

	class Meta:
		verbose_name_plural = "Groups"

class Users(models.Model):
	Group = models.ForeignKey(Groups)
	FirstName = models.CharField(max_length=1024)
	LastName = models.CharField(max_length=1024)
	Position = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.FirstName

	class Meta:
		verbose_name_plural = "Users"

class Incident(models.Model):
	Group = models.ForeignKey(Groups)
	Title = models.CharField(max_length=1024)
	Description = models.TextField(max_length=9064)
	ReviewStatus = models.CharField(max_length=1024)
	User = models.IntegerField()
	def __unicode__(self):              # __unicode__ on Python 2
        	return self.Title
	class Meta:
		verbose_name_plural = "Incidents"

class IncidentChange(models.Model):
	IncidentID = models.ForeignKey(Incident)
	DateOfChange = models.DateTimeField()
	User = models.IntegerField()
	ChangesMade = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.ChangesMade

	class Meta:
		verbose_name_plural = "IncidentChanges"

class Victim(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Type = models.CharField(max_length=1024)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "Victims"

class Source(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Type = models.CharField(max_length=1024)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "Sources"

class Means(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Type = models.CharField(max_length=255)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "Means"

class Impact(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Immediacy = models.CharField(max_length=255)
	Details = models.CharField(max_length=1024)
	RecoveryTime = models.CharField(max_length=1024)
	financialImpact = models.IntegerField()
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "Impacts"

class VictimSector(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Sector = models.CharField(max_length=255)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "VictimSectors"

class DirectImpact(models.Model):
	IncidentID = models.ForeignKey(Incident)
	DirectImpact = models.CharField(max_length=255)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "DirectImpacts"

class IndirectImpact(models.Model):
	IncidentID = models.ForeignKey(Incident)
	IndirectImpact = models.CharField(max_length=255)
	Details = models.CharField(max_length=1024)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Details

	class Meta:
		verbose_name_plural = "IndirectImpacts"

class SeverityOfImpact(models.Model):
	IncidentID = models.ForeignKey(Incident)
	Severity = models.CharField(max_length=255)
	def __unicode__(self):              # __unicode__ on Python 2
                return self.Severity

	class Meta:
		verbose_name_plural = "SeverityOfImpacts"

