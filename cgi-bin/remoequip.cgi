#!/bin/bash

read VAR

echo "content-type: text/html"
echo

IP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<script lang='javascript'>"
if [[ $IP != '' ]] ; then
	if [[ $CIP != '' ]] ; then
		if [[ $IP == $CIP ]] ; then
			grep -v "$IP$;" registrados.csv > registrados.new
			mv registrados.new registrados.csv
			chmod 777 equi.csv
			echo "$(date);$IP;REMOVIDO" >> registrados.log
			echo "alert('Equipamento removido.');"
			echo "location.href='../menu.html'"
		else
			echo "alert('Campos não coincidem.');"
			echo "location.href='../menu.html'"
		fi
	else
		echo "alert('Campos vazios.');"
		echo "location.href='../menu.html'"
	fi
else
	echo "alert('Campos vazios.');"
	echo "location.href='../menu.html'"
fi
echo "</script>"
