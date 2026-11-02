print("================================")
print("     PARTH AI ASSISTANT")
print("================================")

print("নমস্কার স্যার!")
print("আমি PARTH AI Assistant।")
print("আমি আপনার ব্যক্তিগত AI Assistant হওয়ার জন্য তৈরি হচ্ছি।")

while True:
    command = input("\nআপনি: ")

    if command.lower() in ["exit", "quit", "বন্ধ"]:
        print("PARTH AI: আবার কথা হবে, স্যার!")
        break

    elif "নাম" in command:
        print("PARTH AI: আমার নাম PARTH AI Assistant।")

    elif "hello" in command.lower() or "হ্যালো" in command:
        print("PARTH AI: হ্যালো স্যার! আমি কীভাবে সাহায্য করতে পারি?")

    else:
        print("PARTH AI: আমি এখনও শেখার পর্যায়ে আছি, স্যার।")
