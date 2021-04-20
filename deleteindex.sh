#!/bin/bash
today=`date +%Y%m%d`
beforeday=`date -d "today 30days ago" +%Y%m%d`
echo $beforeday
workdir=`cd $(dirname $0);pwd`
echo $workdir
if [ ! -d "$workdir/logs" ];then
mkdir logs
fi
echo `date` ":beginning" >> ./logs/$today.log
indexname=`curl http://139.99.40.186:9200/_cat/indices|awk '{if ($1=="close") print$2}'|awk '/_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$/ {print $0}'|awk -F"_" '{indexdate=$NF;beforeday='''$beforeday'''; if (indexdate<beforeday) print $0;}'`
for i in $indexname
do 
echo -e "curl -XDELETE http://192.168.21.92:9200/"$i""  >> ./logs/$today.log
curl -XDELETE  http://192.168.21.92:9200/"$i"  >> ./logs/$today.log
echo -e "\n" >> ./logs/$today.log
done
echo `date` ':done'>> ./logs/$today.log
