import re

def analyze_strength(password: str) -> dict:
    score = 0
    feedback = []

    checks = {
        "Length ≥ 8":     len(password) >= 8,
        "Length ≥ 12":    len(password) >= 12,
        "Uppercase":      bool(re.search(r'[A-Z]', password)),
        "Lowercase":      bool(re.search(r'[a-z]', password)),
        "Digits":         bool(re.search(r'\d', password)),
        "Special chars":  bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "No common words":password.lower() not in ["password","123456","admin"]
    }

    for check, passed in checks.items():
        if passed:
            score += 1
        else:
            feedback.append(f"Missing: {check}")

    strength = ["Very Weak","Weak","Fair","Moderate","Strong","Very Strong","Excellent"][min(score,6)]
    
    return {"score": score, "strength": strength, "feedback": feedback}