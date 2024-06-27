from pathlib import Path
import datetime


def get_file(filename, mode):
    filepath = Path(filename)
    f = open(filepath, encoding="utf-8", mode=mode)
    return f

def translate_mood(mood):
    mood_to_int = {"happy": 2,
        "relaxed": 1,
        "apathetic": 0,
        "sad": -1,
        "angry": -2
    }

    return mood_to_int[mood]
    



def mood_entry():
    date_today = datetime.date.today() 
    date_today = str(date_today)

    f = get_file("data/mood_diary.txt", "r")
    for line in f:
        if date_today in line:
            print("Sorry, you have already entered your mood today.")
            return
    
    done = False
    while not done:
        current_mood = input("What is your current mood? ").lower().strip()
        if current_mood in ["happy", "relaxed", "apathetic", "sad", "angry"]:
            f = get_file("data/mood_diary.txt", "a")
            f.write(f"{date_today}: {translate_mood(current_mood)}")
            f.close()
            done = True
         


def assess_mood():
    mood_entry()

    f = get_file("data/mood_diary.txt", "r")
    lines = len(f.readlines())
    if lines < 7:
        return
    
    lines = lines[:7]

    no_of_happy = 0
    no_of_sad = 0
    no_of_apathetic = 0
    
    average_mood = 0
    sum_of_moods = 0



    for line in lines:
        
        moods = line[0].split(": ")
        moods = int(moods)

        sum_of_moods += moods
    
        if moods == 2:
            no_of_happy += 1
        elif moods == -1:
            no_of_sad += 1
        elif moods == 0:
            no_of_apathetic += 1

    average_mood = sum_of_moods / 7
    
    if no_of_happy >= 5:
        print("Your diagnosis: manic!")
    elif no_of_sad >= 4:
        print("Your diagnosis: depressive!")
    elif no_of_apathetic >= 6:
        print("Your diagnosis: schizoid!")
    else:
        print(f"Your diagnosis: {average_mood}!")


