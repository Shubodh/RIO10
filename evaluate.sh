#/bin/bash

for i in data/predictions/*.txt ; do 
	src/eval/build/eval data data/predictions/${i##*/} data/errors/${i##*/}
done