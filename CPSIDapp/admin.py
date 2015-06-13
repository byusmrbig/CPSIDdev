from django.contrib import admin

# Register your models here.
from .models import Users
from .models import Groups
from .models import Incident
from .models import Means
from .models import Source
from .models import IncidentChange
from .models import Victim
from .models import Impact
from .models import SeverityOfImpact
from .models import DirectImpact
from .models import IndirectImpact
from .models import VictimSector

admin.site.register(Users)
admin.site.register(Groups)
admin.site.register(Incident)
admin.site.register(Means)
admin.site.register(Source)
admin.site.register(IncidentChange)
admin.site.register(Victim)
admin.site.register(Impact)
admin.site.register(SeverityOfImpact)
admin.site.register(DirectImpact)
admin.site.register(IndirectImpact)
admin.site.register(VictimSector)

