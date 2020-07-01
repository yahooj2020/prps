for url in `cat t1.txt`
do
    wget "$url"
    sleep 0.5
done 
