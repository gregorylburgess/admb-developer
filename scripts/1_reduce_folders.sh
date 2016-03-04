while read p; do
	mkdir $p/../datafiles
	mv $p/at_download/*.* $p/../datafiles/
	rm -r $p/at_download
	rm $p
	rm -r $p
	cd ~/Desktop/admb-developers
done <folders.txt
