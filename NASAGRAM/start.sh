#!/bin/bash
while getopts "mrh" option; do
	echo -e "\033[33;5m _________________________\033[0m"
	echo -e "\033[33;5m<    NASAGRAM Project    >\033[0m"
	echo -e "\033[33;5m<CALVEZ Tony - TB Nicolas>\033[0m"
	echo -e "\033[33;5m _________________________\033[0m"
	echo -e "\033[33;5m        +   /\            \033[0m"
	echo -e "\033[33;5m    +     ..  ..   *      \033[0m"
	echo -e "\033[33;5m  *      /======\      +  \033[0m"
	echo -e "\033[33;5m        |:.  _   |        \033[0m"
	echo -e "\033[33;5m        |:. (_)  |        \033[0m"
	echo -e "\033[33;5m        |:.  _   |        \033[0m"
	echo -e "\033[33;5m     +  |:.  N   |   *    \033[0m"
	echo -e "\033[33;5m        |:.      |        \033[0m"
	echo -e "\033[33;5m      .. \:.    / ..      \033[0m"
	echo -e "\033[33;5m     / .-..:._...-. \     \033[0m"
	echo -e "\033[33;5m     |/    /||\    \|     \033[0m"
	echo -e "\033[33;5m   _..--|||....|||--.._   \033[0m"
	echo -e "\033[33;5m                          \033[0m"

	case $option in
		m)
		while true; do
			read -p "READY FOR THE TAKE OFF (and migrate)? [Y/n]" yn
			case $yn in
				[Yy]* ) python3 manage.py makemigrations home; python3 manage.py migrate; python3 manage.py runserver;;
				[Nn]* ) exit;;
				* ) echo "Please answer yes or no.";;
			esac
		done;;
		r)
		while true; do
			read -p "READY FOR THE TAKE OFF (and migrate)? [Y/n]" yn
			case $yn in
				[Yy]* ) python3 manage.py runserver;;
				[Nn]* ) exit;;
				* ) echo "Please answer yes or no.";;
			esac
		done;;
    	h)
		while true; do
			read -p "READY FOR THE TAKE OFF (and migrate)? [Y/n]" yn
			case $yn in
				[Yy]* ) echo "Command help - start nasagram ";
						echo "=========================";
						echo "-m command: make migrations then run the server";
						echo "-r command: run the server (typical usage)" ;
						echo "-h command: prompt help";break;;
				[Nn]* ) exit;;
				* ) echo "Please answer yes or no.";;
			esac
		done;;
		?)
		echo "illegal option :(..."
		exit 1;;
	esac
done
