#!/bin/sh
file_name="$1"

one_data=""
count=1
while read line; do
	[[ ${one_data} == "" ]] && enter="" || enter="\n"
	[[ $line =~ ":" ]] && data_rm=${line##*:} || data_rm=$line
	if [[ $(echo $data_rm | wc -w) -ge 6 && $(echo $data_rm | wc -w) -le 8 ]]; then
		one_data="${one_data}${enter}${data_rm}"
	elif [[ ${data_rm} == "EOF" ]]; then
		count=$((count+1))
		echo -e ${one_data} > output/${count}.txt
		one_data=""
	fi
done<$file_name