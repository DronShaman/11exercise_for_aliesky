# In a given company, its employees are evaluated at the end of each year. The points
# they can obtain in the evaluation start at 0.0 and can increase, resulting in better
# benefits. The points that employees can achieve can be 0.0, 0.4, 0.6 or more, but
# not intermediate values between the above-mentioned figures. Below is a table with
# the levels corresponding to each score. The amount of money earned at each level
# is €2400 multiplied by the score of the level.

# Write a program that reads the user's score and indicates the user's performance
# level, as well as the amount of money the user will receive.

point_input = float(input())
if point_input >= 0 and point_input <= 0.4:
    print("Your level: Unacceptable")
    print("Your money: ", point_input * 2400)
elif point_input > 0.4 and point_input < 0.6:
    print("Your level: Acceptable")
    print("Your money: ", point_input * 2400)
elif point_input >= 0.6:
    print("Your level: Meritorio")
    print("Your money:", point_input * 2400)