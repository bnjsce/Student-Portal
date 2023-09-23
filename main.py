from youtube_search import YoutubeSearch
import wikipedia
import time
import sys
import os


# MAIN MENU #
def main_menu():
	os.system("cls" if os.name=="nt" else "clear")
	print("Main Menu")
	print("----------------")
	print("1) Homework")
	print("2) Wikipedia")
	print("3) YouTube")
	print("4) Exit")
	print("----------------")
	option = input(">>> ")
	option = option.lower()
	option = option.strip()
	option = option.replace(" ", "")

	if (option == "1") or (option == "homework"):
		homework()
	elif (option == "2") or (option == "wikipedia") or (option == "wiki"):
		wiki()
	elif (option == "3") or (option == "youtube") or (option == "yt"):
		youtube()
	elif (option == "4") or (option == "exit") or (option == "quit"):
		exit()
	else:
		print("Invalid Option.")
		time.sleep(1)
		main_menu()


# HOMEWORK #
def homework():
	os.system("cls" if os.name=="nt" else "clear")
	print("Homework")
	print("----------------")
	print("1) Check homework")
	print("2) Add homework")
	print("3) Remove homework")
	print("4) Go back")
	print("----------------")
	option = input(">>> ")
	option = option.lower()
	option = option.strip()
	option = option.replace(" ", "")

	if (option == "1") or (option == "check") or (option == "checkhomework"):
		check()
	elif (option == "2") or (option == "add") or (option == "addhomework"):
		add()
	elif (option == "3") or (option == "remove") or (option == "removehomework"):
		remove()
	elif (option == "4") or (option == "back") or (option == "goback"):
		main_menu()
	else:
		print("Invalid Option.")
		time.sleep(1)
		homework()

# ADD HOMEWORK #
def add():
	os.system("cls" if os.name=="nt" else "clear")
	print("Add Homework")
	print("----------------")
	subject = input("Subject: ")
	task = input("Task: ")
	due = input("Due Date: ")
	print("----------------")
	add_hw(subject, task, due)

def add_hw(subject, task, due_date):
	subject = subject
	task = task
	due = due_date

	with open("hw.txt", "a") as f:
		f.write(f"{subject.capitalize()} , {task} , {due}\n")
		f.close()

	homework()

# CHECK HOMEWORK #
def check():
	os.system("cls" if os.name=="nt" else "clear")
	print("Check Homework")
	print("--------------------------\n")

	with open("hw.txt", "r") as f:
		data = f.readlines()
		for i in range(0, len(data)):
			section = data[i].split(" , ")
			subject = section[0]
			task = section[1]
			due = section[2]
			print(f"Subject: {subject}")
			print(f"Task: {task}")
			print(f"Due Date: {due}")
			print("--------------------------\n")
		f.close()

	input("Press enter to continue...")
	homework()

# REMOVE HOMEWORK #
def remove():
	os.system("cls" if os.name=="nt" else "clear")

	safety = []

	print("Remove Homework")
	print("--------------------------\n")
	sj = input("Subject: ")
	print("\n")

	with open("hw.txt", "r") as f:
		data = f.readlines()
		for i in range(0, len(data)):
			section = data[i].split(" , ")
			subject = section[0]
			task = section[1]
			due = section[2].replace("\n", "")

			if sj == subject:
				print(f"{i+1}:")
				print(f"Subject: {subject}")
				print(f"Task: {task}")
				print(f"Due: {due}")
				safety.append(data.index(data[i]))
				print("--------------------------\n")
		f.close()

		# option = input(">>> ")
		# option = option.lower()
		# option = option.strip()
		# option = option.replace(" ", "")

		input("Press enter to continue...")
		safety.clear()
	homework()


# WIKIPEDIA #
def wiki():
	os.system("cls" if os.name=="nt" else "clear")
	print("Wikipedia")
	print("----------------")
	print("1) Search")
	print("2) Summary")
	print("3) Go back")
	print("----------------")
	option = input(">>> ")
	option = option.lower()
	option = option.strip()
	option = option.replace(" ", "")

	if (option == "1") or (option == "check") or (option == "checkhomework"):
		sr()
	elif (option == "2") or (option == "add") or (option == "addhomework"):
		summ()
	elif (option == "3") or (option == "back") or (option == "goback"):
		main_menu()
	else:
		print("Invalid Option.")
		time.sleep(1)
		wiki()

# WIKIPEDIA SEARCH #
def sr():
	os.system("cls" if os.name=="nt" else "clear")
	print("Search Wikipedia")
	print("----------------------")
	query = input(">>> ")

	search_results = wikipedia.search(query, results=10, suggestion=False)
	for i in range(0, len(search_results)):
		print(f"{i+1}) {search_results[i]}")
	print("\n---------Suggestion:----------")
	print(f"{wikipedia.suggest(query)}")

	try:
		option = input(">>> ")
		option = option.lower()
		option = option.strip()
		option = option.replace(" ", "")

		os.system(f"start https://en.wikipedia.org/wiki/{str(search_results[int(option)-1]).replace(' ', '_')}")
	except:
		print("Invalid Option.")
		time.sleep(1)
		sr()
	wiki()

# WIKIPEDIA SUMMARY #
def summ():
	os.system("cls" if os.name=="nt" else "clear")
	print("Summary of Topic")
	print("----------------------")
	query = input(">>> ")
	
	print(wikipedia.summary(query, sentences=0, chars=0, auto_suggest=True, redirect=True))
	input("Press enter to continue...")
	wiki()


# YOUTUBE #
def youtube():
	os.system("cls" if os.name=="nt" else "clear")
	print("YouTube")
	print("----------------")
	print("1) Search for content")
	print("2) Go back")
	option = input(">>> ")
	option = option.lower()
	option = option.strip()
	option = option.replace(" ", "")

	if (option == "1") or (option == "search"):
		yt_sr()
	elif (option == "2") or (option == "back") or (option == "exit"):
		main_menu()
	else:
		print("Invalid Option.")
		time.sleep(1)
		youtube()

# YOUTUBE SEARCH #
def yt_sr():
	os.system("cls" if os.name=="nt" else "clear")

	url = []

	print("YouTube Search")
	print("----------------")
	query = input("Search: ")

	results = YoutubeSearch(query, max_results=10).to_dict()

	for i in range(0, len(results)):
		print(f"{i+1}) '{results[i]['title']}' [{results[i]['duration']}] by {results[i]['channel']}, {results[i]['publish_time']} ({results[i]['views']})")
		url.append(results[i]['url_suffix'])

	option = input(">>> ")
	try:
		os.system(f"start https://www.youtube.com{url[int(option)-1]}")
	except:
		print("Invalid Option.")
		time.sleep(1)
		yt_sr()

	url.clear()
	youtube()


# MAIN LOOP #
main_menu()