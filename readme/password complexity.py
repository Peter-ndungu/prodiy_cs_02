import re

# Define the function to check password strength
def password_complexity_checker(password):
    # Initialize variables to track the presence of criteria
    min_length = 8
    length_criteria = len(password) >= min_length
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[@#$%^&*(),.?":{}|<>]', password))
    
    # Create feedback and check strength
    feedback = []
    
    if not length_criteria:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if not upper_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")
    
    # Calculate the strength score
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Classify password strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = password_complexity_checker(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")
