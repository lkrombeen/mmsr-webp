mkdir -p output
mkdir -p magicktemp

export MAGICK_TMPDIR=./magicktemp
for file in input/*
do
  filename=$(basename $file | cut -d. -f1)
  output=output/$filename/$filename.webp
  mkdir -p output/$filename
  cwebp $file -lossless -quiet -o $output
  inputsize=$(du --bytes $file | cut -f -1)
  outputsize=$(du --bytes $output | cut -f -1)
  diffsize=$(($inputsize-$outputsize))
  echo $file has been compressed using webp by $(bc <<< "scale=2; (1.0-$outputsize/$inputsize)*100") percent
done
