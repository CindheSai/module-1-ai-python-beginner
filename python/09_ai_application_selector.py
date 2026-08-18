applications = {
    "1": "Healthcare — medical image analysis and decision support",
    "2": "Finance — fraud detection and risk analysis",
    "3": "Education — adaptive learning and feedback",
    "4": "Transportation — route optimization and perception",
    "5": "Cybersecurity — anomaly and threat detection",
}

print("Choose an AI application:")
for key, value in applications.items():
    print(f"{key}. {value}")

choice = input("Enter 1-5: ").strip()
print(applications.get(choice, "Invalid choice."))
