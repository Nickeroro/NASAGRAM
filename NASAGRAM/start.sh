#!/bin/bash

while getopts "mrh" option; do
	echo " _________________________"
	echo "<    NASAGRAM Project    >"
	echo "<CALVEZ Tony - TB Nicolas>"
	echo " _________________________"
	echo "        +   /\            "
	echo "    +     ..  ..   *      "
	echo "  *      /======\      +  "
	echo "        |:.  _   |        "
	echo "        |:. (_)  |        "
	echo "        |:.  _   |        "
	echo "     +  |:.  N   |   *    "
	echo "        |:.      |        "
	echo "      .. \:.    / ..      "
	echo "     / .-..:._...-. \     "
	echo "     |/    /||\    \|     "
	echo "   _..--|||....|||--.._   "

	echo " READY FOR THE TAKE OFF ? "
	case $option in
		m)
		python3 manage.py makemigrations home
   		python3 manage.py migrate
   		python3 manage.py runserver
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
