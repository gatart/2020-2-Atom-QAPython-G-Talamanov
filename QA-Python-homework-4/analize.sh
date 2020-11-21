#!/usr/bin/env bash

outfile=analyzed

print_help(){
    cat <<EOF
usage: analyze.sh  -a | -m | -b | -c | -s  <FILE> | <DIR>
-a
    кол-во всех запросы
-m
    кол-во запросов по методам
-b
    топ самых больших запросов
-c
    топ запросов с клиентской ошибкой
-s
    топ с серверной ошибкой
FILE
    входной файл
DIR
    использовать рекурсивно файлы из DIR
Имя выходного файла - $outfile.
EOF
}

err(){
    if [ $# -ne 0 ] ;then exit $1; fi
    exit 1
}

methods='^(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT)$'

if [ ! $# -eq 2 ]; then
	print_help
	err
fi

for last_arg in $@; do :; done
if [ -f $last_arg ]; then
    file="$last_arg"
elif [ -d $last_arg ]; then
    file=$(find "$last_arg" -type f)
    if [test -z "$file"]; then err; fi
else
    echo 'No such file or directory' >&2
    err 2
fi

if [ -f analyzed ]; then
    echo -n "File '$outfile' exists, overwrite? (yes/NO): " >&2
    read answer
    if [ ! "$answer" = "y" ] && [ ! "$answer" = "yes" ]; then
        err 17
    fi
fi

exec 1>$outfile

case "$1" in
    --help)
        rm $outfile
        print_help >&2
        ;;
    -h)
        rm $outfile
        print_help >&2
        ;;
    -a)
        egrep -w 'OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT' $file | wc -l
        ;;
    -m)
        egrep -w 'OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT' $file | awk -F '[ "]' '{print $7}' | sort | grep -E $methods | uniq -c | sort -rg | awk '{print $2,$1}'
        ;;
    -b)
        egrep -w 'OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT' $file | awk -F '[ "]' '{print $12,$11,$8}' | sort -k 3,3 -k 1,1rn | uniq -c -f 2 | sort -k 2,2rn | head -10 | awk '{print $4,$3,$1}'
        ;;
    -c)
        egrep -w 'OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT' $file | awk -F '[ "]' '$11>=400 && $11<500 {print $11,$1,$8}' | sort -k 3,3 | uniq -c -f 2 | sort -k 1,1rn | head -10 | awk '{print $4,$2,$3}'
        ;;
    -s)
        egrep -w 'OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT' $file | awk -F '[ "]' '$11>=500 && $11<600 {print $12,$8,$11,$1}' | sort -rnk 1,1 | head -10 | awk '{print $4, $3, $2}'
        ;;
    *)
        rm $outfile
        print_help >&2
        err
        ;;
esac