from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


#making a list of Question object
question_bank=[Question(question_data[i]["question"],question_data[i]["correct_answer"]) for i in range(len(question_data))]


#making QuizBrain object using question list
q_brain=QuizBrain(question_bank)
# print(q_brain.question_list)



while q_brain.still_has_questions():
    q_brain.next_question()
    
print("\nYou've completed the quiz")
print(f"your final score is {q_brain.score}/{q_brain.question_number}")
