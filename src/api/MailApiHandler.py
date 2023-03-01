from flask import make_response
from flask import request, render_template
from flask_restful import Resource

from src.tasks import send_html_email


class MailApiHandler(Resource):

    def post(self):
        try:
            subject = request.json.get("subject")
            body = request.json.get("body")
            address = request.json.get("address")
            # msg_email = render_template("registration.html", body=body)
            task = send_html_email.delay(body, address, subject, "celerymailtest@gmail.com")

            task_id = task.id
            task_response = f"""{{
        "TaskId": "{task_id}"
        }}"""
            response = make_response(task_response)
            response.headers['content-type'] = 'application/json'
            return response

        except Exception as e:
            print(e)
            response = {
                "displayMessage": "Something went wrong"
            }

            return response, 500
