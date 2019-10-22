#Stateless Password Manager

Generate strong and secure passwords that can be accessed anytime, anywhere. This app is not just a
common password manager; the generated passwords are not stored in the database.

User creates password matrices which contains the algorithm that is used to generate the password,
the number of the characters, if it is gonna contains digits or symbols and stuff like that. Then,
if he wants to access a password, it has to give the secret key in order to generate in real-time
the password based on the matrix configuration.

Users can use the same secret key for all their passwords, and for each matrix the generated password
will be different. This because in each matrix we store a salt which make the search space larger in
the case of brute forcing and also make the generated password unique.

![One to rule them all](project/static/images/lordoftherings.jpg)

**Remember one password to access all your passwords, anytime and anywhere**