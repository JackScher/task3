from service import Speaker
from utils import roles, person_additional_data_fields, main_fields


sp = Speaker(roles, main_fields, person_additional_data_fields)
sp.execute()
