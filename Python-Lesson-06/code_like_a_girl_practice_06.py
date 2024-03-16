Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/arabellahooper/Documents/School of Code /PYTHON_PRIMER_ASSIGNMENT_CODE_ARABELLA_HOOPER/Python-Lesson-06/code_like_a_girl_06.py
My name is Arabella.
My age is 28.
My occupation is Project management.
My location is Berlin.
My hobbies is Swimming.
My language is German.
>>> about_me["location"] = "Melbourne"
>>> about_me["age"] = "29"
>>> del about_me["hobbies"]
>>> print_info(about_me)
My name is Arabella.
My age is 29.
My occupation is Project management.
My location is Melbourne.
My language is German.
>>> about_me.clear()
>>> print_info(about_me)
