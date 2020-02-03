.PHONY: show-test show
TESTTXT=2020-02-02T14:35:42,761335425+09:00.txt

%.txt: 
	-tcpdump -n -v -r $*  >$@

debug-HostUnreachableMatcher:
	python3 HostUnreachableMatcher.py

debug-store:
	python3 store.py $(TESTTXT)

match.py-test:
	python3 match.py 2019-12-19T18:08:29,790809551+09:00.txt 

multiline-sample:
	python3 multiline-sample.py 2*txt

TcpdumpFileReadetTest:
	python3 TcpdumpFileReader.py 2*txt

matchtest:
	python3 matchtest.py


