cp /mnt/c/SiYuan/data/widgets/temp/custom-dark.css  ./
cp /mnt/c/SiYuan/data/widgets/temp/custom-light.css ./
cp /mnt/c/SiYuan/data/widgets/temp/custom.css       ./

python convert.py

cp README.md main.js  manifest.json  ../siyuan-plugins/DarkPlusConcise 
cp README.md main.js  manifest.json  /mnt/c/SiYuan/data/plugins/DarkPlusConcise
