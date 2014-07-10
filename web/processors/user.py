from django.contrib.auth.models import User
from django_countries import countries

def get_user(user_id):
    user = User.objects.get(id=user_id)
    return user

def get_user_profile(user_id):
    user = User.objects.get(id=user_id)
    return user.profile

def get_ambassadors():
	ambassadors = []
	aambassadors = User.objects.filter(groups__name='ambassadors').order_by('date_joined')
	for ambassador in aambassadors:
		ambassadors.append(ambassador.profile)
	return ambassadors

def get_ambassadors_for_countries():
	ambassadors = get_ambassadors()
	countries_ambassadors = []
	# list countries minus two CUSTOM_COUNTRY_ENTRIES
	for code, name in list(countries)[2:]:
		readable_name = unicode(name)
		found_ambassadors = []
		for ambassador in ambassadors:
			if ambassador.country == code:
				found_ambassadors.append(ambassador)
		countries_ambassadors.append((readable_name,found_ambassadors))
	countries_ambassadors.sort()
	return countries_ambassadors

def update_user_email(user_id, new_email):
	user = User.objects.get(id=user_id)
	user.email = new_email
	user.save(update_fields=["email"]) 
	return user
