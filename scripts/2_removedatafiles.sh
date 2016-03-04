while read p; do
	cd $p
	mv * ..
	cd /home/epy00n/Desktop/admb-developers
	rm -r $p
done <datafiles.txt
