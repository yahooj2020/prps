for url in `cat t2.txt`
do
    wget "$url"
    sleep 0.5
done 
