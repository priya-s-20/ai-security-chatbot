from phishing_model import detect_phishing

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "otp" in user_input or "bank" in user_input:
        return detect_phishing(user_input)

    elif "password" in user_input:
        return "🔐 Use strong passwords with uppercase, lowercase, numbers, and symbols."

    elif "hacked" in user_input:
        return (
            "🚨 ACCOUNT HACKED STEPS:\n"
            "1️⃣ Change password immediately\n"
            "2️⃣ Enable two-factor authentication\n"
            "3️⃣ Check login activity\n"
            "4️⃣ Report to platform support"
        )

    elif "phishing" in user_input:
        return "🎣 Phishing is a cyber attack where attackers trick users into revealing sensitive information."

    elif "hello" in user_input or "hi" in user_input:
        return "👋 Hello! I am your AI Security Chatbot. Ask me about cyber safety."

    else:
        return "🤖 I can help with phishing detection, password safety, hacked accounts, and cyber awareness."
