
import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('QuizSubmissions')

# Correct answers for 50 questions
correct_answers = {
    "q1": "B",
    "q2": "B",
    "q3": "A",
    "q4": "B",
    "q5": "B",
    "q6": "B",
    "q7": "A",
    "q8": "A",
    "q9": "A",
    "q10": "B",
    "q11": "A",
    "q12": "A",
    "q13": "A",
    "q14": "A",
    "q15": "B",
    "q16": "C",
    "q17": "A",
    "q18": "B",
    "q19": "A",
    "q20": "A",
    "q21": "A",
    "q22": "A",
    "q23": "A",
    "q24": "B",
    "q25": "A",
    "q26": "A",
    "q27": "A",
    "q28": "A",
    "q29": "A",
    "q30": "A",
    "q31": "A",
    "q32": "A",
    "q33": "A",
    "q34": "A",
    "q35": "A",
    "q36": "A",
    "q37": "A",
    "q38": "A",
    "q39": "A",
    "q40": "A",
    "q41": "C",
    "q42": "A",
    "q43": "A",
    "q44": "A",
    "q45": "A",
    "q46": "A",
    "q47": "C",
    "q48": "A",
    "q49": "A",
    "q50": "A"
}

def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])

        name = body['name']
        email = body['email']
        phone = body['phone']
        answers = body['answers']

        score = 0
        attempted = 0

        for i in range(1,51):
            key = f"q{i}"

            if key in answers and answers[key] != "":
                attempted += 1

                if answers[key] == correct_answers[key]:
                    score += 1

        item = {
            "submissionId": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "phone": phone,
            "answers": answers,
            "totalQuestions": 50,
            "attemptedQuestions": attempted,
            "score": score,
            "submittedAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            "body": json.dumps({
                "message": "Quiz submitted successfully",
                "score": score,
                "attemptedQuestions": attempted
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
        
