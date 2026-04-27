suspicious_words = [
"login",
"verify",
"secure",
"update",
"bank",
"free",
"bonus",
"offer",
".xyz",
".tk",
".ml"
]

url = input("Enter website URL: ").lower()

score = 0

for word in suspicious_words:
    if word in url:
        score += 1

if score >= 2:
  print("⚠ Warning: Suspicious / Fake URL Detected")
else:
  print("✓ Safe URL")
