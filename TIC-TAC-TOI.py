#project tic-tac-toi
#start 6_july_2018
#name : dhruvik navadiya

player1_simbole = input("choose X or O : ")
player2_simbole = "O"
main_list = []
checker = " "

def check_win():
	for i in range(0,5,2):
		if main_list[i][0] == main_list[i][2] == main_list[i][4] :
			if main_list[i][0] != checker:
				print(f"{moveer_name} is win...")
				return True

	for i in range(0,5,2):
		if main_list[0][i] == main_list[2][i] == main_list[4][i] :
			if main_list[0][i] != checker:
				printf(f"{moveer_name} is win....")
				return True

	if main_list[0][0] == main_list[2][2] == main_list[4][4]:
		if main_list[0][0] != checker:
			print(f"{moveer_name} is win.....")
			return True

	if main_list[0][4] == main_list[2][2] == main_list[4][0]:
		if main_list[0][4] != checker:
			print(f"{moveer_name} is win.....")		
			return True

	return False



list_1 = [" " , "|" , " ","|"," "]
list_2 = ["-" , "|" , "-","|","-"]
list_3 = [" " , "|" , " ","|"," "]
list_4 = ["-" , "|" , "-","|","-"]
list_5 = [" " , "|" , " ","|"," "]

def set_player_simbole():
	global player2_simbole
	if player1_simbole == 'O':
		player2_simbole = 'X'
	print(f"player one simbole is :{player1_simbole} \n player two simbole is : {player2_simbole}")
set_player_simbole()

def print_bord():
	main_list.append(list_1)
	main_list.append(list_2)
	main_list.append(list_3)
	main_list.append(list_4)
	main_list.append(list_5)

	a=0
	while a<5:
		print_line(main_list[a])
		a+=1


def print_line(line_list):
	print(f"{line_list[0]}{line_list[1]}{line_list[2]}{line_list[3]}{line_list[4]}")

print_bord()

counter = 0
first_move = "X"
moveer_name = "X"

while counter < 9:
	print("write {} any number 1-9 :".format(moveer_name))
	move = int(input())


	if move == 1:
		if list_1[0] == checker:
			list_1[0] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 2:
		if list_1[2] == checker:
			list_1[2] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 3:
		if list_1[4] == checker:
			list_1[4] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 4:
		if list_3[0] == checker:
			list_3[0] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 5:
		if list_3[2] == checker:
			list_3[2] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 6:
		if list_3[4] == checker:
			list_3[4] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	elif move == 7:
		if list_5[0] == checker:
			list_5[0] = moveer_name
		else:
			print("this place is allready fild...")
			continuew
	elif move == 8:
		if list_5[2] == checker:
			list_5[2] = moveer_name
		else:
			print("this place is allready fild...")
			continue
	else:
		if list_5[4] == checker:
			list_5[4] = moveer_name
		else:
			print("this place is allready fild...")
			continue

	print_bord()
	
	if check_win():
		break

	if(moveer_name == "X"):
		moveer_name = "O"
	else:
		moveer_name = "X"
	counter+=1


