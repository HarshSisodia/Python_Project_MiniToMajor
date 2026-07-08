def play_game():
    Questions = [
        "1. What is the capital of India?",
        "2. Which function is used to display output in Python?",
        "3. What is the national animal of India?"
    ]

    Option = [
        "[Mumbai, New Delhi, Kolkata, Chennai]",
        "[input(), show(), print(), output()]",
        "[Lion, Elephant, Tiger, Cheetah]"
    ]

    Answer = ["New Delhi", "print()", "Tiger"]
    FiftyOption=["(New Delhi, Kolkata)","(print(), output())","(Tiger, Cheetah)"]
    PrizeMoney=[100,200,500]
    Prize=0
    FiftyUsed = False

    for i in range(len(Questions)):
        print(Questions[i])
        print(Option[i])
        while True:
                UserInput = input("Enter your Answer, 50-50, or Quit: ")

                if UserInput.strip().lower() == "quit":
                     return f"The Final Prize You Won is: {Prize}"   

                elif UserInput.strip().lower() == Answer[i].lower():
                    print("Sahi Jawab!")
                    Prize=PrizeMoney[i]
                    print(Prize)
                    break

                elif UserInput.strip().lower()=="50-50" and FiftyUsed == False :
                    print(FiftyOption[i])
                    FiftyUsed=True # Lifeline use hote hi True
                    UserInput2=(input("Enter the UserInput2: "))
                    if UserInput2.strip().lower() == Answer[i].lower():
                        print("Sahi Jawab!")
                        Prize=PrizeMoney[i]
                        print(Prize)
                        break
                        
                    else:
                        print("Galat Jawab!")
                        Prize=0
                        print(Prize)
                        return f"The Final Prize You Won is: {Prize}"
                
                elif UserInput.strip().lower() == "50-50" and FiftyUsed == True:
                        print("50-50 Lifeline already used!")
 
                    
                else:
                    print("Galat Jawab!")
                    Prize=0
                    print(Prize)
                    return f"The Final Prize You Won is: {Prize}"
    return f"The Final Prize You Won is: {Prize}"


print(play_game())