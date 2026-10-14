#!/bin/sh
# Prepara gli spot di Remotion per il sito (versioni leggere per il web) e li copia in assets/media/.
# Uso: sh tools/encode-spot.sh /percorso/progetto-remotion
# Usa l'ffmpeg incluso in Remotion (node_modules/@remotion/compositor-*), quindi non serve installarlo.
set -e
R="${1:?Indica la cartella del progetto Remotion}"
O="$R/out"
C=$(ls -d "$R"/node_modules/@remotion/compositor-* | head -n 1)
FF="$C/ffmpeg"
export DYLD_LIBRARY_PATH="$C" LD_LIBRARY_PATH="$C"
M="$(dirname "$0")/../assets/media"
mkdir -p "$M"

"$FF" -v error -y -i "$O/studioabact-promo.mp4" -vf scale=w=1280:h=720 -c:v libx264 -preset slow -crf 25 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "$M/spot-16x9.mp4"
"$FF" -v error -y -i "$O/studioabact-vertical.mp4" -vf scale=w=720:h=1280 -c:v libx264 -preset slow -crf 25 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "$M/spot-9x16.mp4"
"$FF" -v error -y -i "$O/studioabact-promo-poster.jpg" -vf scale=w=1280:h=720 -q:v 3 "$M/spot-16x9-poster.jpg"
"$FF" -v error -y -ss 3 -i "$M/spot-9x16.mp4" -frames:v 1 -q:v 3 "$M/spot-9x16-poster.jpg"
cp "$O/og-image.jpg" "$M/og-image.jpg"
cp "$O/app-icon-180.png" "$O/app-icon-512.png" "$(dirname "$0")/../assets/"
ls -la "$M"
