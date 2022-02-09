#!/bin/sh

links=$( echo "https://www.x-kom.pl/p/636842-procesory-intel-core-i5-intel-core-i5-11400f.html\nhttps://www.x-kom.pl/p/693248-plyta-glowna-socket-1200-gigabyte-b560m-ds3h-v2.html?gclid=Cj0KCQiA_8OPBhDtARIsAKQu0gZoICa15PHxYUBS4ULFrt9sAuKJy5JA0tCXszr8vX6KcGa5cz7v9WMaAvPNEALw_wcB\nhttps://www.x-kom.pl/p/497386-pamiec-ram-ddr4-patriot-32gb-2x16gb-3200mhz-cl16-viper-steel.html\nhttps://www.x-kom.pl/p/667489-pamiec-ram-ddr4-kingston-fury-32gb-1x32gb-3200mhz-cl16-beast-black.html\nhttps://www.x-kom.pl/p/266765-pamiec-ram-ddr4-gskill-32gb-2x16gb-3200mhz-cl16-ripjaws-v-black.html" | sed 's/&/\&/g' )

for link in $(echo -e $links); do
	page=$(curl -s --user-agent 'Chrome/79' "$link")
	title=$( echo $page | grep -o -P 'class="sc-1bker4h-4 PFbyR".{0,200}' | tr '>' '\n' | tr '<' '\n' | head -2 | tail -1)
       	price=$( echo $page | grep -o -P 'n4n86h-4 eKNYud.{0,20}')
	price=$(echo $price | tr '<' '\n' | tr '>' '\n' | head -2 | tail -1 | tr ',' '\n' | head -1)
	echo $title -- price = $price zl
done
