import pyttsx3


def initialize_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Index 0 for male voice, 1 for female voice
    return engine


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def main():
    engine = initialize_engine()
    print("Robo Speaker is ready! Type 'quit' to exit.")

    while True:
        text = input("What should I say? ")
        if text.lower() == 'quit':
            speak(engine, "Goodbye!")
            break
        speak(engine, text)


if __name__ == "__main__":
    main()

# Test the Robo Speaker
main()