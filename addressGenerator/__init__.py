import random


def getRandomValue(addr):
    n = random.randint(0, len(addr))
    print(addr[n - 1])
def getRandomNumber(title, num):
    print(title + str(random.randint(0, 100)))
def getRandomEvenNumber():
    print(random.randrange(0, 1000, 2))
def getJapanZip():
    print(str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999)))
def getBrazilZip():
    print(str(random.randint(10000, 99999)) + "-" + str(random.randint(100, 999)))
def getCanadaUnit():
    print(str(random.randint(10, 99)) + "-" + str(random.randint(100, 999)))
def getRandomPostalCode():
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = len(abc)-1
    randstr = abc[random.randint(0,num)]
    randstr1 = abc[random.randint(0, num)]
    randstr2 = abc[random.randint(0, num)]
    randstr3 = abc[random.randint(0, num)]
    randstr4 = abc[random.randint(0, num)]
    randstr5 = abc[random.randint(0, num)]
    randstr6 = abc[random.randint(0, num)]

    print(randstr+randstr1+randstr2+randstr6+ " " +randstr3+randstr4+randstr5)
def getKoreaZip():
    print(str(random.randint(100, 999)) + "-" + str(random.randint(100, 999)))
countries = ["Brazil", "Canada", "Germany", "India", "Japan", "North and South Korea", "Mexico", "Spain", "UK", "USA"]
usaStates = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN",
             "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
             "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA",
             "WI", "WV", "WY"]
usaCities = ["New York", "Los Angelos", "Chicago", "Houston", "Phoenix", "San Antonio", "Philadelphia", "San Diego",
             "Dallas", "Austin", "San Jose", "Fort Worth", "Jacksonville", "Charlotte", "Columbus", "Indianapolis",
             "San Francisco", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", "Oklahoma City",
             "Las Vegas", "Portland", "Detroit", "Memphis"]
japanPrefectures = ["Aichi", "Akita", "Aomori", "Chiba", "Ehime", "Fukui", "Fukuoka", "Fukushima", "Gifu", "Gunma",
                    "Hiroshima", "Hokkaidō", "Hyōgo", "Ibaraki", "Ishikawa",
                    "Iwate", "Kagawa", "Kagoshima", "Kanagawa", "Kumamoto", "Kyōto", "Kōchi", "Mie", "Miyagi", "Tokyo",
                    "Niigata", "Yamanashi", "Nagasaki", "Saga", "Nagano",
                    "Miyazaki", "Nara", "Okayama", "Okinawa", "Saitama", "Shiga", "Shimane", "Shizuoka", "Tochigi",
                    "Tokushima", "Tottori", "Toyama", "Wakayama", "Yamagata",
                    "Yamaguchi", "Ōita", "Ōsaka"]
japanCities = ['Tokyo', 'Ōsaka', 'Nagoya', 'Yokohama', 'Fukuoka', 'Sapporo', 'Kyōto', 'Kōbe', 'Kawanakajima', 'Saitama',
               'Hiroshima', 'Sendai', 'Kitaku'
    , 'Chiba'
    , 'Niigata'
    , 'Hamamatsu'
    , 'Kumamoto'
    , 'Sagamihara'
    , 'Okayama'
    , 'Edogawa'
    , 'Shizuoka'
    , 'Adachi'
    , 'Kagoshima'
    , 'Hachiōji'
    , 'Utsunomiya'
    , 'Matsuyama'
    , 'Matsudo'
    , 'Higashi-ōsaka'
    , 'Nishinomiya-hama'
    , 'Ōita'
    , 'Kanazawa'
    , 'Fukuyama'
    , 'Machida'
    , 'Toyota'
    , 'Takamatsu'
    , 'Toyama'
    , 'Nagasaki'
    , 'Gifu'
    , 'Miyazaki'
    , 'Okazaki'
    , 'Ichinomiya'
    , 'Toyohashi'
    , 'Nagano'
    , 'Wakayama'
    , 'Nara'
    , 'Koshigaya'
    , 'Ōtsu'
    , 'Tokorozawa'
    , 'Tamuramachi-moriyama'
    , 'Kawagoe'
    , 'Iwaki'
    , 'Maebashi'
    , 'Asahikawa'
    , 'Kōchi'
    , 'Naha'
    , 'Yokkaichi'
    , 'Kasugai'
    , 'Akita'
    , 'Ōakashichō'
    , 'Toshima'
    , 'Morioka'
    , 'Fukushima'
    , 'Tsu'
    , 'Aomori'
    , 'Mito'
    , 'Ichihara'
    , 'Fuchū'
    , 'Fukui'
    , 'Minato'
    , 'Hiratsuka'
    , 'Tokushima'
    , 'Shinozaki'
    , 'Hakodate'
    , 'Sōka'
    , 'Yamagata'
    , ',Tsukuba-kenkyūgakuen-toshi'
    , 'Fuji'
    , 'Chigasaki'
    , 'Chōfugaoka'
    , 'Yato'
    , 'Hachimanchō'
    , 'Sato'
    , 'Saga'
    , 'Neya'
    , 'Ageoshimo'
    , 'Minamiōzuma'
    , 'Arakawa'
    , 'Kure'
    , 'Taitō'
    , 'Matsue'
    , 'Yachiyo'
    , 'Ashino'
    , 'Higashi-Hiroshima'
    , 'Naka'
    , 'Suzuka'
    , 'Kamirenjaku'
    , 'Kumagaya'
    , 'Hino'
    , 'Anjōmachi'
    , 'Tottori'
    , 'Jōetsu'
    , 'Kōfu'
    , 'Izuo'
    , 'Tachikawa'
    , 'Narashino'
    , 'Ōbiraki'
    , 'Takaoka'
    , ',Beppuchō'
    , ',Hitachi'
    , 'Izumo'
    , 'Nishio'
    , 'Takaoka'
    , 'Iwata'
    , 'Niiza'
    , 'Ube'
    , 'Matsuzaka'
    , 'Ōgaki'
    , 'Hitachi-Naka'
    , 'Tochigi'
    , 'Kariya'
    , 'Ueda'
    , 'Higashimurayama'
    , 'Kukichūō'
    , 'Sayama'
    , 'Komaki'
    , 'Tama'
    , 'Yonago'
    , 'Iruma'
    , 'Kakamigahara'
    , 'Kusatsu'
    , 'Shimotoda'
    , 'Misato'
    , 'Fukayachō'
    , 'Ishizaki'
    , ',Kuwana'
    , 'Koga'
    , 'Kisarazu'
    , 'Yaizu'
    , 'Inazawa'
    , 'Ōme'
    , 'Zama'
    , 'Narita'
    , 'Abiko'
    , 'Onomichi'
    , 'Kokubunji'
    , 'Seto'
    , 'Ōmiyachō'
    , 'Iizuka'
    , 'Ise'
    , 'Kashiwara'
    , 'Tsuruoka'
    , 'Ebetsu'
    , 'Daitōchō'
    , 'Kadoma'
    , 'Nobeoka'
    , 'Kōnosu']
japanTowns = ['Zaō',
              'Yuzawa',
              'Yuza',
              'Yūsui',
              'Yusuhara',
              'Yurihama',
              'Yura',
              'Yunomae',
              'Yuni',
              'Yugawara',
              'Yūbetsu',
              'Yuasa',
              'Yoshitomi',
              'Yoshioka',
              'Yoshinogari',
              'Yoshino',
              'Yoshimi',
              'Yoshika',
              'Yoshida',
              'Yosano',
              'Yoron',
              'Yōrō',
              'Yorii',
              'Yonaguni',
              'Yonabaru',
              'Yokoze',
              'Yokoshibahikari',
              'Yokohama',
              'Yoichi',
              'Yazu',
              'Yasuda',
              'Yaotsu',
              'Yanaizu',
              'Yamatsuri',
              'Yamato',
              'Yamanouchi',
              'Yamanobe',
              'Yamamoto',
              'Yamakita',
              'Yamada',
              'Yakushima',
              'Yakumo',
              'Yakage',
              'Yahaba',
              'Yaese',
              'Yachiyo',
              'Yabuki',
              'Wazuka',
              'Watari',
              'Watarai',
              'Wassamu',
              'Wanouchi',
              'Wakuya',
              'Waki',
              'Wake',
              'Wakasa',
              'Wakasa',
              'Wadomari',
              'Utazu',
              'Uryū',
              'Urausu',
              'Urakawa',
              'Urahoro',
              'Umi',
              'Ujitawara',
              'Ugo',
              'Uchinada',
              'Uchiko',
              'Tsuwano',
              'Tsuruta',
              'Tsurugi',
              'Tsuno',
              'Tsuno',
              'Tsunan',
              'Tsunagi',
              'Tsukigata',
              'Tsubetsu',
              'Tsubata',
              'Toyoyama',
              'Toyoura',
              'Toyotomi',
              'Toyosato',
              'Toyono',
              'Toyokoro',
              'Tōyō',
              'Tōyako',
              'Tosa',
              'Tōnoshō',
              'Tonoshō',
              'Tone',
              'Tomioka',
              'Tomika',
              'Tomamae',
              'Tōma',
              'Tokunoshima',
              'Tokigawa',
              'Tōin',
              'Tōhoku',
              'Tōgō',
              'Togitsu',
              'Tōei',
              'Tōbetsu',
              'Tobe',
              'Teshio',
              'Teshikaga',
              'Tawaramoto',
              'Tatsuno',
              'Tatsugō',
              'Tateyama',
              'Tateshina',
              'Tarui',
              'Taragi',
              'Tara',
              'Tano',
              'Tanagura',
              'Tamamura',
              'Tamaki',
              'Tako',
              'Takko',
              'Takinoue',
              'Taki',
              'Taketoyo, Mihama',
              'Taketomi',
              'Takatori',
              'Takasu',
              'Takanezawa',
              'Takanabe',
              'Takamori',
              'Takamori',
              'Takahata',
              'Takaharu',
              'Takahama',
              'Takachiho',
              'Taka',
              'Tajiri',
              'Taiwa',
              'Taishi',
              'Taishi',
              'Taiki',
              'Taiki',
              'Taiji',
              'Tagami',
              'Taga',
              'Tadotsu',
              'Tadaoka',
              'Tadami',
              'Tachiarai',
              'Tabuse',
              'Suttsu',
              'Susami',
              'Suōōshima',
              'Sumita',
              'Sugito',
              'Sue',
              'Sotogahama',
              'Soeda',
              'Sōbetsu',
              'Shōwa',
              'Shōō',
              'Shōnai',
              'Shōdoshima',
              'Shizukuishi',
              'Shiwa',
              'Shitara',
              'Shisui',
              'Shirosato',
              'Shiroishi',
              'Shiriuchi',
              'Shirataka',
              'Shiraoi',
              'Shiranuka',
              'Shirako',
              'Shirakawa',
              'Shirahama',
              'Shioya',
              'Shintotsukawa',
              'Shintomi',
              'Shintoku',
              'Shinkamigotō',
              'Shinhidaka',
              'Shingū',
              'Shinchi',
              'Shinano',
              'Shin',
              'Shimosuwa',
              'Shimonita',
              'Shimokawa',
              'Shimoichi',
              'Shimogō',
              'Shimizu',
              'Shimizu',
              'Shime',
              'Shimanto',
              'Shimamoto',
              'Shikaoi',
              'Shikama',
              'Shikabe',
              'Shika',
              'Shihoro',
              'Shichinohe',
              'Shichikashuku',
              'Shichigahama',
              'Shibetsu',
              'Shibecha',
              'Shibayama',
              'Shibata',
              'Shari',
              'Shakotan',
              'Setouchi',
              'Setana',
              'Sera',
              'Sekigahara',
              'Seirō',
              'Seika',
              'Saza',
              'Sayō',
              'Satsuma',
              'Satoshō',
              'Sasaguri',
              'Saroma',
              'Sannohe',
              'Sangō',
              'Samukawa',
              'Samani',
              'Sakuho',
              'Sakawa',
              'Sakaki',
              'Sakai',
              'Sakahogi',
              'Sakae',
              'Saka',
              'Ryūō',
              'Rokunohe',
              'Rishirifuji',
              'Rishiri',
              'Rikubetsu',
              'Rifu',
              'Reihoku',
              'Rebun',
              'Rausu',
              'Ranzan',
              'Rankoshi',
              'Pippu',
              'Ōzu',
              'Ōzora',
              'Ōyodo',
              'Ōyamazaki',
              'Oyama',
              'Ōwani',
              'Ōtsuki',
              'Ōtsuchi',
              'Ōtoyo',
              'Otofuke',
              'Otobe',
              'Ōtō',
              'Ōtaki',
              'Ōshima',
              'Oshamambe',
              'Ōsato',
              'Ōsakikamijima',
              'Ōsaki',
              'Ōra',
              'Ōno',
              'Ono',
              'Onjuku',
              'Onga',
              'Ōnan',
              'Onagawa',
              'Ōmu',
              'Ōmachi',
              'Ōma',
              'Okutama',
              'Okushiri',
              'Ōkuma',
              'Okuizumo',
              'Okoppe',
              'Okinoshima',
              'Ōki',
              'Oketo',
              'Okagaki',
              'Ojika',
              'Ōji',
              'Ōizumi',
              'Ōiso',
              'Ōishida',
              'Oirase',
              'Ōi',
              'Ōi',
              'Ōharu',
              'Oguni',
              'Oguni',
              'Ōguchi',
              'Ogose',
              'Ōgawara',
              'Ogawa',
              'Ogano',
              'Ōe',
              'Ōdai',
              'Ochi']
brazilProvinces = ['AC',
                   'AL',
                   'AM',
                   'AP',
                   'BA',
                   'CE',
                   'DF',
                   'ES',
                   'GO',
                   'MA',
                   'MG',
                   'MS',
                   'MT',
                   'PA',
                   'PB',
                   'PE',
                   'PI',
                   'PR',
                   'RJ',
                   'RN',
                   'RO',
                   'RR',
                   'RS',
                   'SC',
                   'SE',
                   'SP',
                   'TO']
brazilCities = ['São Paulo',
                'Rio de Janeiro',
                'Brasília',
                'Salvador',
                'Fortaleza',
                'Belo Horizonte',
                'Manaus',
                'Curitiba',
                'Recife',
                'Goiânia',
                'Belém',
                'Porto Alegre',
                'Guarulhos',
                'Campinas',
                'São Luís',
                'São Gonçalo',
                'Maceió',
                'Duque de Caxias',
                'Campo Grande',
                'Natal',
                'Teresina',
                'São Bernardo do Campo',
                'João Pessoa',
                'Nova Iguaçu',
                'São José dos Campos',
                'Santo André',
                'Ribeirão Preto',
                'Jaboatão dos Guararapes',
                'Uberlândia',
                'Osasco',
                'Sorocaba',
                'Contagem',
                'Aracaju',
                'Feira de Santana',
                'Cuiabá',
                'Joinville',
                'Aparecida de Goiânia',
                'Londrina',
                'Juiz de Fora',
                'Porto Velho',
                'Ananindeua',
                'Serra',
                'Caxias do Sul',
                'Macapá',
                'Niterói',
                'Florianópolis',
                'Belford Roxo',
                'Campos dos Goytacazes',
                'Vila Velha',
                'Mauá',
                'São João de Meriti',
                'São José do Rio Preto',
                'Mogi das Cruzes',
                'Betim',
                'Boa Vista',
                'Maringá',
                'Santos',
                'Diadema',
                'Jundiaí',
                'Rio Branco',
                'Montes Claros',
                'Campina Grande',
                'Piracicaba',
                'Carapicuíba',
                'Anápolis',
                'Olinda',
                'Cariacica',
                'Bauru',
                'Itaquaquecetuba',
                'São Vicente',
                'Vitória',
                'Caruaru',
                'Caucaia',
                'Blumenau',
                'Petrolina',
                'Ponta Grossa',
                'Franca',
                'Canoas',
                'Pelotas',
                'Vitória da Conquista',
                'Ribeirão das Neves',
                'Uberaba',
                'Paulista',
                'Praia Grande',
                'Cascavel',
                'São José dos Pinhais',
                'Guarujá',
                'Taubaté',
                'Palmas',
                'Limeira',
                'Camaçari',
                'Santarém',
                'Petrópolis',
                'Mossoró',
                'Suzano',
                'Taboão da Serra',
                'Versa Grande',
                'Sumaré',
                'Marabá',
                'Gravataí']
brazilNeighborhood = ['Falcão',
                      'Favela',
                      'Mangueira',
                      'Morro da Babilônia',
                      'Morro da Mineira',
                      'Morro da Providência',
                      'Morro do Estado',
                      'Vidigal, Rio de Janeiro',
                      'Vigário Geral',
                      'Vila do João',
                      'Vila Parisi',
                      'Cantagalo–Pavão–Pavãozinho',
                      'Cidade de Deus, Rio de Janeiro',
                      'Complexo do Alemão',
                      'Ondina, Salvador',
                      'Pajuçara',
                      'Ponta Verde',
                      'Praia do Gunga',
                      'Jatiúca',
                      'Parangaba',
                      'Rodolfo Teófilo, Fortaleza']

canadaProvince = ['AB',
                  'BC',
                  'MB',
                  'NB',
                  'NL',
                  'NT',
                  'NS',
                  'NU',
                  'ON',
                  'PE',
                  'QC',
                  'SK',
                  'YT']
canadaCities = ['Abbotsford',
                'Armstrong',
                'Burnaby',
                'Campbell River',
                'Castlegar',
                'Chilliwack',
                'Colwood',
                'Coquitlam',
                'Courtenay',
                'Cranbrook',
                'Dawson Creek',
                'Delta',
                'Duncan',
                'Enderby',
                'Fernie',
                'Fort St. John',
                'Grand Forks',
                'Greenwood',
                'Kamloops',
                'Kelowna',
                'Kimberley',
                'Langford',
                'Langley',
                'Maple Ridge',
                'Merritt',
                'Mission',
                'Nanaimo',
                'Nelson',
                'New Westminster',
                'North Vancouver',
                'Parksville',
                'Penticton',
                'Pitt Meadows',
                'Port Alberni',
                'Port Coquitlam',
                'Port Moody',
                'Powell River',
                'Prince George',
                'Prince Rupert',
                'Quesnel',
                'Revelstoke',
                'Richmond',
                'Rossland',
                'Salmon Arm',
                'Surrey',
                'Terrace',
                'Trail',
                'Vancouver[a]',
                'Vernon',
                'Victoria[b]',
                'West Kelowna',
                'White Rock',
                'Williams Lake']

germanyCities =['Berlin',
'Hamburg',
'München',
'Köln',
'Frankfurt',
'Essen',
'Dortmund',
'Stuttgart',
'Düsseldorf',
'Bremen',
'Hannover',
'Duisburg',
'Nürnberg',
'Leipzig',
'Dresden',
'Bochum',
'Wuppertal',
'Bielefeld',
'Bonn',
'Mannheim',
'Karlsruhe',
'Gelsenkirchen',
'Wiesbaden',
'Münster',
'Mönchengladbach',
'Chemnitz',
'Augsburg',
'Braunschweig',
'Aachen',
'Krefeld',
'Halle',
'Kiel',
'Magdeburg',
'Oberhausen',
'Lübeck',
'Freiburg',
'Hagen',
'Erfurt',
'Kassel',
'Rostock',
'Mainz',
'Hamm',
'Saarbrücken',
'Herne',
'Mülheim',
'Solingen',
'Osnabrück',
'Ludwigshafen',
'Leverkusen',
'Oldenburg',
'Neuss',
'Paderborn',
'Heidelberg',
'Darmstadt',
'Potsdam',
'Würzburg',
'Göttingen',
'Regensburg',
'Recklinghausen',
'Bottrop',
'Wolfsburg',
'Heilbronn',
'Ingolstadt',
'Ulm',
'Remscheid',
'Pforzheim',
'Bremerhaven',
'Offenbach',
'Fürth',
'Reutlingen',
'Salzgitter',
'Siegen',
'Gera',
'Koblenz',
'Moers',
'Bergisch Gladbach',
'Cottbus',
'Hildesheim',
'Witten',
'Zwickau',
'Erlangen',
'Iserlohn',
'Trier',
'Kaiserslautern',
'Jena',
'Schwerin',
'Gütersloh',
'Marl',
'Lünen',
'Esslingen',
'Velbert',
'Ratingen',
'Düren',
'Ludwigsburg',
'Wilhelmshaven',
'Hanau',
'Minden',
'Flensburg',
'Dessau',
'Villingen-Schwenningen']

for x in range(200):
    #getRandomValue(germanyCities)
    # getRandomNumber("", 200)
     #getRandomNumber("Flat No. ",1000)
    # getCanadaUnit()
    #getRandomNumber("Postfach ",999)
    #getKoreaZip()
    getRandomPostalCode();


