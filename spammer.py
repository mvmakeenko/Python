import requests
import random
from faker import Faker


url = "https://finance-ru.experience-of-marketing.com/registerr333.php"
payload = {
    "source": "",
    "click_id": "",
    "country_code": "",
    "description": "",
    "currency": "eur",
    "country": "RU",
    "comment": "",
    "campaign_name": "Google Finance",
    "custom2": "",
    "custom1": ""
}
mails = [
	"@gmail.com",
	"@mail.ru",
	"@yandex.ru",
	"@tut.by",
	"@protonmail.com",
	"@yahoo.com",
	"@edu.ru",
	"@icloud.com", 
	"@titan.email",
	"@aim.com",
	"@pm.com",
	"@zoho.com",
	"@hubspot.com"
]

fake = Faker("ru_RU")
status = 200

while status == 200:
	name = fake.first_name()
	surname = fake.last_name()
	phone = str(fake.msisdn()[:10])
	email = fake.email()

	payload["name"] = f"{name} {surname}"
	payload["email"] = email.split("@")[0] + random.choice(mails)
	payload["phone"] = payload["fphone"] = f"+7{phone}"
	payload["phone1"] = f"{phone[:3]} {phone[3:6]}-{phone[6:8]}-{phone[8:10]}"

	response = requests.post(url, json=payload)
	status = response.status_code
	print(f"{status:^10} | {payload['name']:^30} | {payload['email']:^40} | {payload['phone']:^30}")
