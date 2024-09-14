# Ex1
Andersen = {"The Emperors New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen"}
print(Andersen)

# Ex2
Shakespeare = {"Romeo and Juliet", "Hamlet", "King Lear", "Macbeth", "A Midsummer Nights Dream", "A Comedy of Errors"}
print(Shakespeare)

# Ex3
Tragedy = {"Medea", "Octavia", "Oedipus", "Ur-Hamlet"}
Comedy = {"The Three Musketeer", "The Clouds"}
Uncategory = {"Don Quixote", "Rapunzel", "Cinderella"}
print(Tragedy, Comedy, Uncategory)

# Ex4
Shakespeare_Tragedy = Tragedy.difference(Shakespeare)
print(Shakespeare_Tragedy)

# Ex5
Andersen_Comedy = Comedy.intersection(Andersen)
print(Andersen_Comedy)

# Ex6
Andersen_Comedy.issubset(Comedy)  # True
Andersen_Comedy.issuperset(Andersen)  # False
Andersen_Comedy.isdisjoint(Tragedy)  # True
Shakespeare_Tragedy.issubset(Tragedy)  # True
Shakespeare_Tragedy.issuperset(Shakespeare)  # False
Shakespeare_Tragedy.isdisjoint(Comedy)  # True
print(Andersen_Comedy.issubset(Comedy), Andersen_Comedy.issuperset(Andersen), Andersen_Comedy.isdisjoint(Tragedy), Shakespeare_Tragedy.issubset(Tragedy), Shakespeare_Tragedy.issuperset(Shakespeare), Shakespeare_Tragedy.isdisjoint(Comedy))

# Ex7
Work = Andersen.union(Shakespeare, Tragedy, Comedy, Uncategory)
print(Work)

# Ex8
Author = {"Hans Christian Andersen", "Shakespeare", "Unknown"}
print(Author)

# Ex9
Author_Of = {
    "The Emperors New Clothes": "Hans Christian Andersen",
    "The Little Mermaid": "Hans Christian Andersen",
    "The Little Match Girl": "Hans Christian Andersen",
    "The Snow Queen": "Hans Christian Andersen",
    "Romeo and Juliet": "Shakespeare",
    "Hamlet": "Shakespeare",
    "King Lear": "Shakespeare",
    "Macbeth": "Shakespeare",
    "A Midsummer Nights Dream": "Shakespeare",
    "A Comedy of Errors": "Shakespeare",
    "Medea": "Unknown",
    "Octavia": "Unknown",
    "Oedipus": "Unknown",
    "Ur-Hamlet": "Unknown",
    "The Three Musketeer": "Unknown",
    "The Clouds": "Unknown",
    "Don Quixote": "Unknown",
    "Rapunzel": "Unknown",
    "Cinderella": "Unknown"
}
print(Author_Of)

# Ex10
Writen_By = {value: key for key, value in Author_Of.items()}
print(Writen_By)

# Ex11
Work_Count = {work: sum(work in s for s in [Andersen, Shakespeare, Tragedy, Comedy, Uncategory]) for work in Work}
print(Work_Count)

# Ex12
exercise_content = """
In the span of humanity, writing are what enabled humans to pass on many knowledge to their next generation. Via writing, the art of telling stories; both fictional and real; evolved and became a huge part of humanity culture. Among them, there are stories that transcend languages, culture and history to reach people far away both in spaces and times. Some prominent examples are the works of Shakespeare, Andersen, Homer,...
 1. Han Christian Andersen is famous for fairy tales such as: "The Emperors NewClothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen". Create a set in Python named Andersen and put his fairy tales' names as elements.
 2. Shakespeare is mostly famous for his tragedies such as: "Romeo and Juliet", "Hamlet", "King Lear", "Macbeth". Meanwhile, he also wrote comedies such as:"A Midsummer Nights Dream"and "A Comedy of Errors". Create a set in Python named Shakespeare and put his plays' names as elements.
 3. Given the tragedies such as: "Medea", "Octavia", "Oedipus", "Ur-Hamlet". Comedies such as: "The Three Musketeer", "The Clouds". Meanwhile there are some stories that is hard to put in either comedies or tragedies such as: "Don Quixote", "Rapunzel", "Cinderella". Create 3 sets named Tragedy, Comedy and Uncategory then put the above works, included Andersen and Shakespeare's works, names in the right categories.
 4. Create a set named Shakespeare_Tragedy by taking the difference of 2 related sets.
 5. Create a set named Andersen_Comedy by taking the intersection of 2 related sets.
 6. Determine the relationship of Andersen_Comedy and Shakespeare_Tragedy with Shakespeare, Andersen, Tragedy, Comedy, and Uncategory set. The relations needed to be test is: issubset, issuperset, isdisjoint.
 7. Create a set named Work by combine all the above set.
 8. Create a set named Author taking authors names and Unknown as it's elements.
 9. Using python Dict named Author_Of to represent the relation between Work and Author. Which mean, print(Author_Of['Hamlet']) should print Shakespeare.
 10. Using python Dict named Writen_By to represent the invert relation of Author_Of.
 11. Using python Dict named Work_Count to count how many sets each Work appeared.
 12. Within the content of Exercise section count how many words are in this section of the Lab.
 13. Count how many times each words appeared and sorted the word by
 number of times they appeared descending.
"""
word_count = len(exercise_content.split())
print(word_count)

# Ex13
text = "Within the content of Exercise section count how many words are in this section of the Lab. Count how many times each word appeared and sort the words by the number of times they appeared in descending order."
words = text.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_word_count)