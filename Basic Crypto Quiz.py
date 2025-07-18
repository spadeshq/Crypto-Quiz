# Crypto Quiz.py
print("Welcome to the Cryptocurrency Quiz!")
input("Press Enter to start the quiz!")

def run_quiz():
    questions = {
        "What is the max supply of Bitcoin? ": ["21000000", "21 million", "21 Million"],
        "What is the max supply of Ethereum? ": ["120000000", "120 million", "120 Million"],
        "What is the max supply of Dogecoin? ": ["100000000000", "100 billion", "100 Billion"],
        "What is the max supply of Cardano? ": ["45000000000", "45 billion", "45 Billion"],
        "What is the max supply of Solana? ": ["5000000000", "5 billion", "5 Billion"],
        "What is the max supply of Polkadot? ": ["1000000000", "1 billion", "1 Billion"],
        "What is the max supply of Chainlink? ": ["1000000000", "1 billion", "1 Billion"],
        "What is the max supply of Litecoin? ": ["84000000", "84 million", "84 Million"],
        "What is the max supply of XRP? ": ["100000000000", "100 billion", "100 Billion"],
        "What is the max supply of Stellar? ": ["50000000000", "50 billion", "50 Billion"],
        "What does ETH stand for? ": ["ethereum"],
        "Which token has a dog as its logo? ": ["dogecoin"],
        "What does DEX stand for? ": ["decentralized exchange"],
    }

    score = 0
    for question, answers in questions.items():
        user_answer = input(question).strip().lower()
        # Normalize all acceptable answers to lowercase too
        normalized_answers = [ans.lower() for ans in answers]
        if user_answer in normalized_answers:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answers were: {', '.join(answers)}\n")
    
    print(f"🎯 You got {score}/{len(questions)} right.\n")

# Game loop
play_again = 'yes'
while play_again == 'yes':
    run_quiz()
    play_again = input("Play again? (yes/no): ").strip().lower()
