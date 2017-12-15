#!/bin/bash
IFS=$'\n'
read SO
VAI=$(echo $SO | cut -d"=" -f2)
echo "content-type: text/html"
echo
um(){
	for x in $(cat ./arm_info.log); do
		echo "<p>$x</p>"
	done
}

dois(){
	for x in $(cat ./arm_infolog.log); do
		echo "<p>$x</p>"
	done
}

tres(){
	for x in $(cat ./registrados.csv); do
		echo "<p>$x</p>"
	done
}

if [[ $VAI == "atual" ]] ; then
um
if [[ $VAI == "completo" ]] ; then
dois
if [[ $VAI == "monitorados" ]] ; then
tres
else
echo "Opção Inexistente"
fi
fi
fi
