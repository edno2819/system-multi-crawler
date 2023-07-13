## Documento para identificar análises do site Arezzo

Este documento visa descrever as tomadas de decições e tecnicas utilizadas para 
crawlear o site da Arezzo.

O site da Arezzo tem dois tipos de produtos Bolsa e Sapatos.
As outras categrias são subcategorias destas ou eventos como promoções e número de vendas.

Para percorre todos o melhor caminho que eu encontrei foi ir nas categorias bolsas e sapatos e selecionar todos.
    - https://www.arezzo.com.br/c/bolsas
    - https://www.arezzo.com.br/c/sapatos

index.json tem as informações de cada produto



curl 'https://www.arezzo.com.br/arezzocoocc/v2/arezzo/products/search?category=SAPATOS&currentPage=11&pageSize=24&fields=FULL&storeFinder=false' \
  -H 'authority: www.arezzo.com.br' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H $'cookie: nlbi_2612518=d01RCunIX15SeoOCmrsFigAAAABTgbqneFhIuXQbpLaPkuYm; visid_incap_2612518=VjDrcL9CQcyZIu+/lfY62dK3rmQAAAAAQUIPAAAAAACBElMoJCptJWXsd2cFdYyC; cart_id=51c65dad-85ad-4eec-b84a-6f8f5140a0c3; _gaexp=GAX1.3.wuTrXhidTk-FCXwnyotI1A.19627.1\u0021zZ4zaCJoRJ2_NETI5abh7A.19627.0\u00213tUQE7dSTIqIw5Ox9JoSLw.19602.1; _gcl_au=1.1.353683540.1689171925; gtm_cookie_is_first_omni_geo_evt_fired=true; _gid=GA1.3.234629106.1689171925; _gac_UA-60371343-1=1.1689171925.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; scarab.visitor=%224D6E75E3AFA71113%22; FPLC=k7%2FuzAZgu9RXT1Bzpm0zGLRjxcNe01oaQQ5yBQr6ivNX7w%2FDyc8%2FO71YuCOre6ns637K63lCS5im%2F9hG8BMOZxv%2BhjOAZdtuWlXLHmaoAFdrVWr9AYRus4gEVaYZGw%3D%3D; FPID=FPID2.3.xyFcKrMQHP7rys7O8t44s5T1rl7CFlOXPWW1%2B5EFcXc%3D.1689171925; _gcl_aw=GCL.1689171926.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; __utmzzses=1; @oli-validated=6e1a7709-5357-4c34-8cb6-ba7e025bc514; _tt_enable_cookie=1; _ttp=iAIlM9-B9fuylO8LgqytnLGM6v3; _cvhash={"hash":"49ad5b46-b012-7cea-1974","identified":false}; blueID=cca7638d-654f-4db1-b63e-aaf1cdeb8910; va_uid=767af222-f000-4c2d-accc-166ec5db0678; _gac_UA-60371343-2=1.1689171932.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; _clck=1kfzyyb|2|fd8|0|1288; scarab.profile=%22g%252F1282300200002U%7C1689174401%22; __utmzz=utmcsr=blue|utmcmd=retargeting|utmccn=AREZZO_MIRUM_ECOM_RETARGETING_CONVERSAO_BLUE_VENDAS-DE-CATALOGO_PERFORMANCE_RMKT|utmcct=BR_RMKT_DINAMICO_NA|utmctr=DINAMICO_ONGOING_SEM-TEMPLATE_MISTO; __utmzzsesid=1689179955787.6ogxknkdffs; blueULC=blue; incap_ses_1620_2612518=MRS7PsSNuwtWNDbgwGV7Fh7zrmQAAAAA34VmIXMluLkT1BnjpBYkXg==; va_ses=64aef725b2724a3c99761459; JSESSIONID=721F9BFE1308453FE31CEC3195D121BD.node107; _ga_X=GS1.1.1689188133.4.1.1689188804.0.0.0; _ga=GA1.3.923213511.1689171925; gtm_cookie_pageview_session_sequence=66; _uetsid=f1ecb1c020bf11ee97d991323d95eff5; _uetvid=f1ecbde020bf11ee83f61b03e82670d4; cto_bundle=6lNzxV85NjJOZ3NMOE52SXRGMFhXTzZFeDRtMHQzWXZ5YWJQalppd1gzUmtwT0JIbE5MbzFOcWtPU2pScWF6YWVJdlhLWkVQZSUyQk5qTmxyTm5vRjRMQiUyRlZ3VHFEYTV0QVZUSHliMVlDN0dUdiUyQm1OODhub0FsYkZ1eE41MExWZEdjMlhmRVk0d0hnd0h3SmxOUHUzekFrMmUzekElM0QlM0Q; _clsk=1wtwvqv|1689189385679|8|1|v.clarity.ms/collect; _dc_gtm_UA-60371343-2=1; _dc_gtm_UA-60371343-1=1; _ga_S6X24FQ6FL=GS1.1.1689188132.4.1.1689189385.60.0.0' \
  -H 'headless: true' \
  -H 'referer: https://www.arezzo.com.br/c/sapatos?q=&page=11' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
  --compressed



CURL para obtenção de produto:
    curl 'https://www.arezzo.com.br/_next/data/hpdxxj5iM7QtyfYBnBK9f/bolsa-nude-tiracolo-pequena/p/5710023320007U.json?n1=bolsa-nude-tiracolo-pequena&sku=5710023320007U' \
    -H 'authority: www.arezzo.com.br' \
    -H 'accept: */*' \
    -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
    -H $'cookie: visid_incap_2612518=VjDrcL9CQcyZIu+/lfY62dK3rmQAAAAAQUIPAAAAAACBElMoJCptJWXsd2cFdYyC; cart_id=51c65dad-85ad-4eec-b84a-6f8f5140a0c3; _gcl_au=1.1.353683540.1689171925; _gid=GA1.3.234629106.1689171925; _gac_UA-60371343-1=1.1689171925.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; FPID=FPID2.3.xyFcKrMQHP7rys7O8t44s5T1rl7CFlOXPWW1%2B5EFcXc%3D.1689171925; _gcl_aw=GCL.1689171926.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; @oli-validated=6e1a7709-5357-4c34-8cb6-ba7e025bc514; _tt_enable_cookie=1; _ttp=iAIlM9-B9fuylO8LgqytnLGM6v3; _cvhash={"hash":"49ad5b46-b012-7cea-1974","identified":false}; blueID=cca7638d-654f-4db1-b63e-aaf1cdeb8910; va_uid=767af222-f000-4c2d-accc-166ec5db0678; _gac_UA-60371343-2=1.1689171932.Cj0KCQjwnrmlBhDHARIsADJ5b_l972IVr_AmvNPGLBeilV-jadABHzDlAgoWSV26WemqQoWFNLPzsdkaAhy8EALw_wcB; __utmzz=utmcsr=blue|utmcmd=retargeting|utmccn=AREZZO_MIRUM_ECOM_RETARGETING_CONVERSAO_BLUE_VENDAS-DE-CATALOGO_PERFORMANCE_RMKT|utmcct=BR_RMKT_DINAMICO_NA|utmctr=DINAMICO_ONGOING_SEM-TEMPLATE_MISTO; blueULC=blue; nlbi_2612518=S6/RW+K5vEgCKNC6mrsFigAAAAD8kr64n9LaAyCiPOPnqAKW; incap_ses_1620_2612518=D4LBFId2rghLRNXgwGV7FiXrr2QAAAAAE5AtrHYWlHvOU4xWp4nRmg==; JSESSIONID=1094274164DCC0D02DCCF4D71BB3E5AE.node103; gtm_cookie_is_first_omni_geo_evt_fired=true; __utmzzses=1; __utmzzsesid=1689250599962.8ssiyqxb1ue; scarab.visitor=%224D6E75E3AFA71113%22; va_ses=64afeb28b2724a3364473ab2; FPLC=jMCtHNfsjKV83GZal8mOOISi%2F9BsCDlTRwd%2BmE18j%2BJ57cfVyTEZ3usCZrdCHeL349%2BmIXHcE2izNsOYAopSkcyCwscZmfAuTIMBGnc9BtHFHgZnesgoUJ%2Bk58nuhg%3D%3D; _clck=1kfzyyb|2|fd9|0|1288; _gaexp=GAX1.3.wuTrXhidTk-FCXwnyotI1A.19627.1\u0021zZ4zaCJoRJ2_NETI5abh7A.19627.0\u00213tUQE7dSTIqIw5Ox9JoSLw.19602.1\u0021-m7FsTaMSV672kUkDdBfNg.19643.2; _ga=GA1.3.923213511.1689171925; gtm_cookie_pageview_session_sequence=12; _uetsid=f1ecb1c020bf11ee97d991323d95eff5; _uetvid=f1ecbde020bf11ee83f61b03e82670d4; cto_bundle=QLt_uV85NjJOZ3NMOE52SXRGMFhXTzZFeDRuVnZRdXhZQjF3dVVoaUplUVRmUkxJQWVwdHZGN1R3OTV3RTVwbjBJbGdEQ1BMMFhkU2lPaUh3cVpvVXVRYWV3ZFVubUZzczhGOXk2UTFTTzk3bWVqRzklMkYlMkZPZSUyQktybThsZ3RWZUhJVGhpR2taWm1sSVlxb1lFbFIlMkZQSjMlMkZxb0VRJTNEJTNE; _clsk=1w7oewf|1689252015663|11|1|q.clarity.ms/collect; _ga_S6X24FQ6FL=GS1.1.1689250599.7.1.1689252025.60.0.0; _ga_X=GS1.1.1689250599.7.1.1689252025.0.0.0' \
    -H 'if-none-match: "8oy6idii9ynqk"' \
    -H 'purpose: prefetch' \
    -H 'referer: https://www.arezzo.com.br/bolsa-nude-tiracolo-pequena/p/5710023320007U' \
    -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Linux"' \
    -H 'sec-fetch-dest: empty' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-site: same-origin' \
    -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
    -H 'x-nextjs-data: 1' \
    --compressed