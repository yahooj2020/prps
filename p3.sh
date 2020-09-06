for url in `cat t3.txt`
do
    wget "$url"
    sleep 0.5
done 

