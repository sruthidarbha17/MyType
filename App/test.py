def personality_test():
    print("🔹 Welcome to the Personality Test! Answer with 1 or 2.\n")

    questions = [
        ("How do you prefer to spend your weekend?", ["1. At home reading", "2. Going out with friends"]),
        ("Do you enjoy meeting new people?", ["1. No, I prefer familiar faces", "2. Yes, I love socializing"]),
        ("What kind of activities do you enjoy?", ["1. Solo activities like reading/drawing", "2. Group activities like team sports"]),
        ("Do you often feel drained after social interactions?", ["1. Yes", "2. No"]),
        ("Would you rather work alone or in a team?", ["1. Alone", "2. In a team"]),
        ("How do you recharge?", ["1. Spending time alone", "2. Being around people"]),
        ("Do you prefer deep conversations over small talk?", ["1. Yes", "2. No"]),
        ("Are you more comfortable in familiar environments?", ["1. Yes", "2. No"]),
        ("Do you like being the center of attention?", ["1. No", "2. Yes"]),
        ("Do you enjoy public speaking?", ["1. No", "2. Yes"])
    ]

    score = 0
    for question, options in questions:
        print("\n" + question)
        for option in options:
            print(option)
        
        while True:
            try:
                answer = int(input("Your choice (1 or 2): "))
                if answer in [1, 2]:
                    score += answer - 1  # 1 gives 0 points, 2 gives 1 point
                    break
                else:
                    print("❌ Please enter 1 or 2 only.")
            except ValueError:
                print("❌ Invalid input. Please enter a number (1 or 2).")

    # Determine personality type based on score
    if score <= 3:
        result = "Introvert"
    elif 4 <= score <= 6:
        result = "Ambivert"
    else:
        result = "Extrovert"

    print(f"\n🎉 Your Personality Type: {result} 🎉")

if __name__ == "__main__":
    personality_test()