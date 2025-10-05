'''
TDEE calculator
User have to input WEIGHT, HEIGHT, AGE and select GENDER
Based on these inputs, user gets its TDEE (Total Daily Energy Expenditure), after calculation, User should see calories to:
1) Maintain weight,
2) Lose weight,
3) Gain weight,

User should also see what is his current situation according to TDEE.
User should be put in:
1) Under weight
2) Normal weight
3) Over weight

category, this should be also noted in different colors (Spectrum from red - yellow - green - yellow - red)
'''

def get_gender():
    while True:
        gender = input("What gender are you? male/female ").lower()
        if gender in ["male", "female"]:
            return gender
        print("❌ Please enter 'male' or 'female'!")


def get_age():
    while True:
        try:
            age = int(input("What is your age? "))
            if 0 < age < 120:
                return age
            print("❌ Enter a realistic age (1–120).")
        except ValueError:
            print("❌ Enter a valid NUMBER!")


def get_weight():
    while True:
        try:
            weight = float(input("What is your weight in KGs? "))
            if 30 <= weight <= 300:
                return weight
            print("❌ Enter a realistic weight (30–300 kg).")
        except ValueError:
            print("❌ Enter a valid NUMBER!")


def get_height():
    while True:
        try:
            height = float(input("What is your height in CMs? "))
            if 100 <= height <= 250:
                return height
            print("❌ Enter a realistic height (100–250 cm).")
        except ValueError:
            print("❌ Enter a valid NUMBER!")

class BmrCalculation:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
    
    def calculate_bmr(self):
        if self.gender == "male":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161


bmr_calc = BmrCalculation(weight, height, age)

# volání metody a výpis výsledku
bmr_value = bmr_calc.calculate_bmr()
print(f"Your BMR is: {bmr_value:.2f}")



#BMR = 10 × váha (kg) + 6.25 × výška (cm) - 5 × věk (roky) + 5   (muži)
#BMR = 10 × váha (kg) + 6.25 × výška (cm) - 5 × věk (roky) - 161 (ženy)
# potom x aktivní faktor
'''
Aktivita	Popis	Faktor
Sedavý způsob života	Minimum pohybu	1.2
Lehká aktivita	Cvičení 1–3× týdně	1.375
Střední aktivita	Cvičení 3–5× týdně	1.55
Vysoká aktivita	Cvičení 6–7× týdně	1.725
Velmi vysoká aktivita	Intenzivní tréninky 2× denně	1.9
'''