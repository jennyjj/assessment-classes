"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   OO can provide abstraction -- that is, not all methods that are called
   need to be understood in detail.  Programmers can go through the code
   at a high level and overpass certain details.

   OO can also provide encapsulation.  Rather than methods and attributes being
   assigned in different places throughoug the code, they are bundled together 
   or encapsulated in one place, under the class function.  It is easier
   to call methods and draw on attributes therefore.

   Finally, OO provides polymorphism.  If there are objects which are similar
   but differ at different points, they can inherit from a parent class 
   similar attributes, but differ (as indicated in coding for subclasses)
   in some attributes and for some methods.  Polymorphism rids the need
   to have much repeated code.

2. What is a class?

A class is type of function that allows functions and variables to
interact with one another.  Classes can have instances (when
a class is instantiated or created), and these instances can have attributes
and methods that can be called, affecting in turn often the attributes.

3. What is an instance attribute?

An instance attribute is a characteristic of an instance, that was
created by the instance itself, versus the class.  It is often created
by the command self.attribute.

4. What is a method?

A method is like a function, but it is inside a class.  It can be called
in the syntax instance.method.

5. What is an instance in object orientation?

An instance is a copy or object made from a class function.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is given as part of the class itself.  An instance 
attribute is created by calling on the instance itself (created by 
the syntax self.attribute).  We would use class attribute when creating
a parent class and setting attributes that will be given to instances
upon initialization.  We can use instance attributes to changes certain 
inherited class attributes, or we can use these instance attributes (and
changed them) within methods.


"""

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
	"""Creates a student with name and addres."""

	def __init__(self, first_name, last_name, address):
		"""Initializes an instance."""

		self.first_name = first_name
		self.last_name = last_name
		self.address = address


class Question(object):
	"""Creates a question with answer."""

	def __init__(self, question, correct_answer):
		"""Initializes an instances of a Question."""

		self.question = question
		self.correct_answer = correct_answer

	def ask_and_evaluate(self):
		"""Asks a question and returns True if answer right."""

		answer = raw_input(self.question + " > ")
		if answer == self.correct_answer:
			return True
		else:
			return False


class Exam(object):
	"""Creates an exam with name and can add questions and administer exam."""

	def __init__(self, name_of_exam):
		"""Initializes an instance of an Exam."""

		self.name_of_exam = name_of_exam
		self.questions = []
	def add_question(self, question):
		"""Adds a question."""

		self.questions.append(question)

	def administer(self):
		"""Administers the exam and gives back a score."""

		tally = 0
		num_of_questions = len(self.questions)
		
		for question in self.questions:
			answer = raw_input(question.question + " > ")
			if answer == question.correct_answer:
				tally += 1

		print float(tally)	
		print float(num_of_questions)	
		return tally / float(num_of_questions)		


class StudentExam(Exam):
	"""Creates an instance which subclasses Exam."""

	def __init__(self, student, exam, score=None):
		"""Initializes an instance of a StudentExam."""

		super(StudentExam, self).__init__(exam.name_of_exam)
		self.exam = exam
		self.student = student
		self.score = score
		self.questions = exam.questions

	def take_test(self):
		"""Administers the test and gives back a score."""

		self.score = self.administer()
		print "The score is " + str(self.score) + "."
	

class Quiz(Exam):
	"""Creates a quiz, which subclasses Exam."""

	def administer(self):
		"""Administers the exam and gives back pass("1") or fail("0")."""
		
		tally = 0
		num_of_questions = len(self.questions)
		
		for question in self.questions:
			answer = raw_input(question.question + " > ")
			if answer == question.correct_answer:
				tally += 1

		if tally / num_of_questions >= .5:
			return "1"
		else:
			return "0"


def example(exam_name, question1, question2, question3,
	correct_answer1, correct_answer2, correct_answer3, 
	first_name, last_name, address):
	"""Gives a student an exam and returns a score."""

	exam = Exam(exam_name)

	question1 = Question(question1, correct_answer1)
	question2 = Question(question2, correct_answer2)
	question3 = Question(question3, correct_answer3)

	exam.add_question(question1)
	exam.add_question(question2)
	exam.add_question(question3)

	student = Student(first_name, last_name, address)

	student_exam1 = StudentExam(student, exam)

	student_exam1.take_test()


example('midterm', 'What command gives back len of string?', 
	'What is it called to create a copy of a class?', 
	'What is the best engineering school for women?',
	'len()', 'instantiate', 'Hackbright',
	'Jenny', 'Justh', 
	'100 Seed Ave., Pittsburgh, PA 66685')







