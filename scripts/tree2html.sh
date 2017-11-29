#! /bin/bash

IN=$1
OUT=$2
STYLE=$3

WIDTH=$(wc -L $IN | cut -d' ' -f 1)
HEIGHT=$(wc -l $IN | cut -d' ' -f 1)

LEAF="<div class='pixel leaf'><\/div>"
FOLIAGE="<div class='pixel foliage'><\/div>"
BRANCH="<div class='pixel branch'><\/div>"
TRUNK="<div class='pixel trunk'><\/div>"
SKY="<div class='pixel sky'><\/div>"
LIGHT_ROCK="<div class='pixel rock light'><\/div>"
DARK_ROCK="<div class='pixel rock dark'><\/div>"

echo "
<!doctype html>
<html>
  <head>
    <style type="text/css">
" >> $OUT
cat $STYLE >> $OUT
echo "
.world {
  grid-template-columns: repeat(${WIDTH}, 1fr);
}" >> $OUT
echo "
    </style>
  </head>
  <body>
    <div class="world">
" >> $OUT

cat $IN |
sed -e "s/[^-orTtfFT]/@z/g" |
sed -e "s/f/@f/g" |
sed -e "s/F/@F/g" |
sed -e "s/t/@t/g" |
sed -e "s/[rT]/@T/g" |
sed -e "s/-/@-/g" |
sed -e "s/o/@o/g" |
sed -e "s/@z/${SKY}/g" |
sed -e "s/@f/${LEAF}/g" |
sed -e "s/@F/${FOLIAGE}/g" |
sed -e "s/@t/${BRANCH}/g" |
sed -e "s/@T/${TRUNK}/g" |
sed -e "s/@-/${LIGHT_ROCK}/g" |
sed -e "s/@o/${DARK_ROCK}/g" >> $OUT
echo >> $OUT

echo "
    </div>
  </body>
</html>
" >> $OUT

