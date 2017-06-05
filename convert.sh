mkdir -p output
mkdir -p magicktemp

export MAGICK_TMPDIR=./magicktemp
for file in input/*
do
  filename=$(basename $file | cut -d. -f1)
  output=output/$filename/$filename
  mkdir -p output/$filename
  cwebp -quiet $file -lossless -o $output.webp
  for format in jpg png bmp gif
  do
    for quality in 100 80 50
    do
      convert -quiet $file -quality $quality% $output-quality$quality.$format
    done
  done
done
