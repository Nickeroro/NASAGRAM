#!/bin/bash

while getopts "mrh" option; do
	echo " _____________________________________"
	echo "<          NASAGRAM Project          >"
	echo "<       CALVEZ Tony - TB Nicolas     >"
	echo " _____________________________________"
	echo "        \   ^__^"
	echo "         \  (oo)\_______"
	echo "            (__)\       )\/\ "
	echo "                ||----w |"
	echo "                ||     ||"
	case $option in
		m)
		python manage.py makemigrations home
   		python manage.py migrate
   		python manage.py runserver
		;;
		r)
		python manage.py runserver
		;;
    		h)
		echo "Command help - start nasagram "
		echo "========================="
		echo "-m command: make migrations and run the server"
		echo "-r command: only run the server" 
  		echo "-h command: prompt help"
		;;
		?)
		echo "illegal option :(..."
		exit 1
		;;
	esac
done
