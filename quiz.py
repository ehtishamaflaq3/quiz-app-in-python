quize = {
    "1.What is the capital of Turkey?": "istanbul",
    "2.What is the largest planet in our solar system?": "jupiter",
    "3.What is 5 + 70.7?": "75.7",
    "4.Which is the largest continent?": "asia",
    "5.What gas do plants absorb from the atmosphere?": "carbon dioxide",
    "6.What is the boiling point of water in Celsius?": "100",
    "7.Who was the first man on the moon?": "neil armstrong",
    "8.Which planet is known as the Red Planet?": "mars",
    "9.What is the largest ocean in the world?": "pacific ocean",
    "10.What is the smallest prime number?": "2",
    "11.What is the national flower of Pakistan?": "jasmine",
    "12.What is H2O commonly known as?": "water",
    "13.How many legs does a spider have?": "8",
    "14.In which direction does the sun rise?": "east",
    "15.How many days are there in a leap year?": "366",
}
def load_high_score():
    try:
        with open("easyhigh_score.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    with open("easyhigh_score.txt", "w") as f:
        f.write(str(score))
def basquiz():
    score=0
    high_score = load_high_score()
    print("Welcome to the Easy Level Quiz!")
    print(f"THE HIGHEST SCORE IS {high_score}")
    for ques,ans in quize.items():
        print(ques)
        userans=input("WRITE THE ANSWER:- ")
        if userans.lower()==ans.lower():
            print("YOUR ANSWER IS CORRECT")
            score=score+1
        else:
            print(f"WRONG!! THE CORRECT ANSWER IS {ans}")
        print(f"Your Score: {score}/{len(quize)}")
    if score>high_score:
        save_high_score(score)
    else:
        print(f"High score remains {high_score}.")
# --------------------------------------------------------------------------
quizm = {
    "1.What is the capital of Turkey?": "ankara",
    "2.Which planet is known as the 'Blue Planet'?": "earth",
    "3.How many bones are there in the adult human body?": "206",
    "4.What is the hardest natural substance on Earth?": "diamond",
    "5.Who painted the Mona Lisa?": "leonardo da vinci",
    "6.Which is the smallest country in the world?": "vatican city",
    "7.Which language is the most spoken in the world?": "english",
    "8.Which animal is known as the 'Ship of the Desert'?": "camel",
    "9.How many continents are there on Earth?": "7",
    "10.What is the currency of Japan?": "yen",
    "11.Which part of the plant conducts photosynthesis?": "leaf",
    "12.Which country gifted the Statue of Liberty to the USA?": "france",
    "13.What is the chemical symbol for Gold?": "au",
    "14.What is the tallest mountain in the world?": "mount everest",
    "15.Which ocean is the largest?": "pacific ocean",
    "16.What do bees collect and use to make honey?": "nectar",
    "17.How many colors are there in a rainbow?": "7",
    "18.Who discovered gravity when he saw a falling apple?": "isaac newton",
    "19.Which instrument is used to measure temperature?": "thermometer",
    "20.Which famous scientist developed the theory of relativity?": "albert einstein"
}
def mload_high_score():
    try:
        with open("medium high_score.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def msave_high_score(score):
    with open("medium high_score.txt", "w") as f:
        f.write(str(score))

def medquiz():
    score=0
    mhigh_score = mload_high_score()
    print("Welcome to the Medium Level Quiz!")
    print(f"THE HIGHEST SCORE IS {mhigh_score}")
    for ques,ans in quizm.items():
        print(ques)
        userans=input("WRITE THE ANSWER:- ")
        if userans.lower()==ans.lower():
            print("YOUR ANSWER IS CORRECT")
            score=score+1
        else:
            print(f"WRONG!! THE CORRECT ANSWER IS {ans}")
    print(f"Your Score: {score}/{len(quizm)}")
    if score>mhigh_score:
            msave_high_score(score)
    else:
            print(f"High score remains {mhigh_score}.")

# ---------------------------------------------------------------------------
quizh={
    "1. Which element has the atomic number 82?": "lead",
    "2. Who developed the polio vaccine in 1952?": "jonas salk",
    "3. What is the capital of Kazakhstan?": "astana",
    "4. Which blood type is known as the universal recipient?": "ab positive",
    "5. What year did the Berlin Wall fall?": "1989",
    "6. What is the smallest country by land area?": "vatican city",
    "7. What is the second longest river in the world?": "amazon",
    "8. Which Nobel Prize winner discovered penicillin?": "alexander fleming",
    "9. What is the SI unit of pressure?": "pascal",
    "10. Which philosopher wrote 'Critique of Pure Reason'?": "immanuel kant",
    "11. Which layer of Earth lies just below the crust?": "mantle",
    "12. In which year did Pakistan conduct its nuclear tests?": "1998",
    "13. Which instrument measures humidity?": "hygrometer",
    "14. What is the longest bone in the human body?": "femur",
    "15. Which war ended with the Treaty of Versailles?": "world war i",
    "16. Which scientist proposed the three laws of motion?": "isaac newton",
    "17. What is the capital city of Sri Lanka?": "sri jayawardenepura kotte",
    "18. What is the main gas found in the Earth's atmosphere?": "nitrogen",
    "19. Which language has the most native speakers?": "mandarin",
    "20. What is the square root of 729?": "27",
    "21. Which vitamin is produced when sunlight hits the skin?": "vitamin d",
    "22. What is the largest internal organ in the human body?": "liver",
    "23. Which country has the highest number of time zones?": "france",
    "24. Which African country was formerly known as Abyssinia?": "ethiopia",
    "25. Which physicist is famous for the uncertainty principle?": "werner heisenberg"
}
def hload_high_score():
    try:
        with open("high level high_score.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def hsave_high_score(score):
    with open("high level high_score.txt", "w") as f:
        f.write(str(score))

def highquiz():
    score=0
    hhigh_score = hload_high_score()
    print("Welcome to the High Level Quiz!")
    print(f"THE HIGHEST SCORE IS {hhigh_score}")
    for ques,ans in quizh.items():
        print(ques)
        userans=input("WRITE THE ANSWER:- ")
        if userans.lower()==ans.lower():
            print("YOUR ANSWER IS CORRECT")
            score=score+1
        else:
            print(f"WRONG!! THE CORRECT ANSWER IS {ans}")
        print(f"Your Score: {score}/{len(quizh)}")
    if score>hhigh_score:
        hsave_high_score(score)
    else:
        print(f"High score remains {hhigh_score}.")
# ----------------------------------------------------------------------------
def main():
        print("==========CHOOSE YOUR LEVEL==========")
        print("1.EASY")
        print("2.MEDIUM")
        print("3.HARD")
        levelchoice=int(input("WRITE YOU LEVEL(1-3):- "))
        match levelchoice:
            case 1:
                basquiz()
            case 2:
                medquiz()
            case 3:
                highquiz()
            case _:
                print("INVALID CHOICE")
main()