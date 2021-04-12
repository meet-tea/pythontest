import datetime

x = datetime.datetime.now()
if x.strftime("%H") >= "12":
	if x.strftime("%H") < "18":
		z = "afternoon"
	elif x.strftime("%H") > "18":
		z = "night"
elif x.strftime("%H") <= "13":
	if x.strftime("%H") <= "5":
		z = "midnight"
	elif x.strftime("%c") >= "6":
		z = "morning"


def uwu(time):
	print(f'its {x.strftime("%c")} so its {time}')


if __name__ == '__main__':
	uwu(z)

input('Press Enter to exit')
