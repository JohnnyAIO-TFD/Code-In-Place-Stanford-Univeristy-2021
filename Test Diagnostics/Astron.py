meters = float(input("Enter your height in meters: "))
if meters >= 1.6 and meters <= 1.9:
    print("Correct height to be an astronaut")
elif meters < 1.6:
    print("Below minimum astronaut height")
else:
    print("Above maximum astronaut height")
