<h1 align="center">
  <br>
  <img src="https://github.com/AlmogShKt/IMSWeatherApi/blob/master/WeatherLogo.png" alt="WeatherMsiApiLogo" width="200"></a>
  <br> IMS Weather API  <br>
</h1>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#stations-id">Stations ID</a> •
  <a href="#rights">Rights</a> •
</p>

## About
Are you interested in keeping up with the local weather?
* Are you wondering when there is snow on the ground?
* Are you wondering if you should book a place in El-Rom?
* Are you tired of opening telegram groups and weather apps on your phone?  
> You are in the right place!  

By using this project, you can easily get a weather update on your terminal, at any of the IMS measurement stations.
___
# COMMING UP SOON - Online Dashboars to see all the data !!
___
## Features
*Receive the following data from IMS stations:
  * Measurement time
  * Rain amount (mm)
  * Ground temperature(°)
  * Max temperature(°)
  * Min temperature(°)
___
  ## How to use:
1. clone the repository to your local computer
2. install or make sure you have:
    ```bash
    pip install 
    pip install json
    pip install os
    pip install python-dateutil
    pip install python-dotenv
    ```

3. Ask for ApiToken from IMS: <a href="mailto:ims@ims.gov.il">Email</a> , and follow the <a href = "https://ims.gov.il/he/ObservationDataAPI)">instructions</a>


4. Open new file, called `.env` and enter this line:  
`IMS_TOKEN = ApiToken replace_with_your_token`

5. Open terminal and run:  
`~cd /yourLocalPath/WeatherApi/`  

6. Run the `main.py` file:   
`~python3 main.py`

6. Enter the station id you wish to follow, and enjoy!

Example of result:
```
_________________________
Station Name: merom golan picman | id: 10
Measurement time is: 15:40:00
The amount of rain is: 10.2mm
The Max temperature is: -1.5°
The Min temperature is: -2.1°
The ground temperature is: -1.4°
**There is snow conditions!!**
_________________________
```
___

## Stations ID
> In some of the stations, not all channels available.  

Station Name  | Station ID
--------------|----------
AVNE ETAN     | 2
BET ZAYDA     | 6
ZEMAH         | 8
MEROM GOLAN PICMAN | 10
YAVNEEL       | 11
TAVOR KADOORIE | 13
AFULA NIR HAEMEQ | 16
TEL YOSEF 20060907 | 17
EDEN FARM 20080706 | 18
QARNE SHOMERON | 20
ARIEL         | 21
JERUSALEM GIVAT RAM | 22
JERUSALEM CENTRE | 23
HAR HARASHA    | 24
NETIV HALAMED HE | 25
HAIFA PORT    | 26
SHANI         | 28
ARAD          | 29
GILGAL        | 30
NEWE ZOHAR UNI | 32
HAZEVA        | 33
PARAN 20060124 | 35
YOTVATA       | 36
HAIFA REFINERIES | 41
HAIFA UNIVERSITY | 42
HAIFA TECHNION | 43
EN KARMEL      | 44
ZIKHRON YAAQOV | 45
HADERA PORT   | 46
BET DAGAN     | 54
BESOR FARM    | 58
BEER SHEVA    | 59
BEER SHEVA UNI | 60
ZEFAT HAR KENAAN | 62
ELAT          | 64
SEDOM         | 65
EN HASHOFET   | 67
MIZPE RAMON 20080514 | 69
ELON          | 73
QEVUZAT YAVNE | 74
BEIT JIMAL    | 75
ROSH ZURIM    | 77
AFEQ          | 78
DOROT         | 79
NEGBA         | 82
BET DAGAN RAD | 85
ITAMAR        | 90
SEDE BOQER    | 98
DEIR HANNA    | 99
ROSH HANIQRA  | 106
EN HAHORESH   | 107
ZOMET HANEGEV | 112
LEV KINERET   | 115
HAFEZ HAYYIM  | 121
AMMIAD        | 123
ASHDOD PORT   | 124
TEL AVIV COAST | 178
| NEWE YAAR     | 186        |
| ZOVA          | 188        |
| KEFAR BLUM    | 202        |
| ESHHAR        | 205        |
| EDEN FARM     | 206        |
| PARAN         | 207        |
| ASHQELON PORT | 208        |
| METZOKE DRAGOT | 210       |
| EN GEDI       | 211        |
| BET DAGAN_1m  | 212        |
| MAALE ADUMMIM | 218        |
| MAALE GILBOA  | 224        |
| GAMLA         | 227        |
| BET HAARAVA   | 228        |
| NEOT SMADAR   | 232        |
| KEFAR NAHUM   | 233        |
| GAT           | 236        |
| ZEFAT HAR KENAAN_1m | 238  |
| ELON_1m       | 239        |
| ARAD_1m       | 240        |
| KEFAR GILADI  | 241        |
| ARIEL_1m      | 242        |
| ASHDOD PORT_1m | 243       |
| BESOR FARM_1m | 244        |
| DOROT_1m      | 245        |
| EN HAHORESH_1m | 246       |
| QARNE SHOMERON_1m | 247    |
| JERUSALEM CENTRE_1m | 248  |
| JERUSALEM GIVAT RAM_1m | 249 |
| SEDOM_1m      | 250        |
| SEDE BOQER_1m | 251        |
| NEGBA_1m      | 252        |
| NAHSHON       | 259        |
| GALED         | 263        |
| MIZPE RAMON 20120927 | 265  |
| HARASHIM      | 269        |
| SHAARE TIQWA 20161205 | 270 |
| AVDAT         | 271        |
| NIZZAN        | 274        |
| HAKFAR HAYAROK | 275       |
| GILGAL_1m     | 276        |
| ITAMAR_1m     | 277        |
| HAR HARASHA_1m | 278       |
| BET HAARAVA_1m | 279       |
| MAALE ADUMMIM_1m | 280     |
| ZOVA_1m       | 281        |
| NAHSHON_1m    | 282        |
| HAFEZ HAYYIM_1m | 283      |
| QEVUZAT YAVNE_1m | 284     |
| GAT_1m        | 285        |
| ROSH ZURIM_1m | 286        |
| NETIV HALAMED HE_1m | 287   |
| BEIT JIMAL_1m | 288        |
| METZOKE DRAGOT_1m | 289    |
| EN GEDI_1m    | 290        |
| ASHQELON PORT_1m | 291     |
| SHANI_1m      | 292        |
| BEER SHEVA_1m | 293 |
BEER SHEVA_1m | 293
ZOMET HANEGEV_1m | 294
HAZEVA_1m | 295
MIZPE RAMON_1m | 296
PARAN_1m | 297
HARASHIM_1m | 298
TEL AVIV COAST_1m | 299
AVNE ETAN_1m | 300
BET ZAYDA_1m | 301
ZEMAH_1m | 302
MEROM GOLAN PICMAN_1m | 303
YAVNEEL_1m | 304
TAVOR KADOORIE_1m | 305
AFULA NIR HAEMEQ_1m | 306
EDEN FARM_1m | 307
YOTVATA_1m | 309
HAIFA REFINERIES_1m | 310
HAIFA UNIVERSITY_1m | 311
HAIFA TECHNION_1m | 312
EN KARMEL_1m | 313
ZIKHRON YAAQOV_1m | 314
HADERA PORT_1m | 315
ELAT_1m | 316
EN HASHOFET_1m | 317
AFEQ_1m | 318
DEIR HANNA_1m | 319
ROSH HANIQRA_1m | 320
AMMIAD_1m | 322
NEWE YAAR_1m | 323
KEFAR BLUM_1m | 324
ESHHAR_1m | 325
GAMLA_1m | 327
MAALE GILBOA_1m | 328
NEOT SMADAR_1m | 329
KEFAR NAHUM_1m | 330
GALED_1m | 332
AVDAT_1m | 335
NIZZAN_1m | 336
EZUZ_1m | 344
SHAVE ZIYYON_1m | 345
KEFAR GILADI_1m | 346
NEVATIM_1m | 370
MASSADA_1m | 373
MIZPE RAMON | 379
TEL YOSEF_1m | 443
ASHALIM_1m | 480
DAFNA_1m | 498
___

# Rights

* Using IMS API - all rights reserve to ©<a href ="https://ims.gov.il/he">IMS<a/>
