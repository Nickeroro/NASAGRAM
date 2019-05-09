#!/bin/bash
while getopts "mrh" option; do
	echo -e " _________________________"
	echo -e "<    NASAGRAM Project    >"
	echo -e "<CALVEZ Tony - TB Nicolas>"
	echo -e " _________________________"
	echo -e "        +   /\            "
	echo -e "    +     ..  ..   *      "
	echo -e "  *      /======\      +  "
	echo -e "        |:.  _   |        "
	echo -e "        |:. (_)  |        "
	echo -e "        |:.  _   |        "
	echo -e "     +  |:.  N   |   *    "
	echo -e "        |:.      |        "
	echo -e "      .. \:.    / ..      "
	echo -e "     / .-..:._...-. \     "
	echo -e "     |/    /||\    \|     "
	echo -e "   _..--|||....|||--.._   "

	case $option in
		m)
		while true; do
			read -p "READY FOR THE TAKE OFF ?" yn
			case $yn in
				[Yy]* ) python3 manage.py makemigrations home; python3 manage.py migrate; python3 manage.py runserver; break;;
				[Nn]* ) exit;;
				* ) echo "Please answer yes or no.";;
			esac
		done
		;;
		r)
		python3 manage.py runserver
		;;
    	h)
		echo "Command help - start nasagram "
		echo "========================="
		echo "-m command: make migrations then run the server"
		echo "-r command: run the server (typycal usage)" 
  		echo "-h command: prompt help"
		;;
		?)
		echo "illegal option :(..."
		exit 1
		;;
	esac
done
