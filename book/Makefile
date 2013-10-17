#
# reminders how to make the ADASS book, but without all the dependancies
# create for ADASS 2012 proceedings - Peter Teuben



p = main_volume


# b = editor

all:	pdf

pdf:	$(p).pdf 

dvi:	$(p).dvi

$(p).pdf:  $(p).dvi
	dvipdf $(p)

$(p).dvi:  step1 step2 step3


step1:	$(p).tex 
	latex $(p) > log1

step2:	bibtex
	latex $(p) > log2

step3:  index
	latex $(p) > log3

index:
	makeindex < $(p).adx > $(p).and
	makeindex < $(p).odx > $(p).ond
	makeindex < $(p).idx > $(p).ind
	makeindex < $(p).sdx > $(p).snd

clean:
	rm -f $(p).dvi $(p).bbl $(p).aux
	rm -f part*/*/*.aux

TEX = bibtex

bibtex:
	@for i in $(B); do\
	($(TEX) $$i); done

#   this the list of papers that have bibtex companions (not all do)
B = \
./part1/Brunner_O04/Brunner_O04 \
./part1/Feigelson_P051/Feigelson_P051 \
./part1/Krueger_P16/Krueger_P16 \
./part1/Mann_O22/Mann_O22 \
./part2/Badenhorst_O01/Badenhorst_O01 \
./part2/Baxter_O02/Baxter_O02 \
./part2/Cardiel_P08/Cardiel_P08 \
./part2/Ceballos_P009/Ceballos_P009 \
./part2/Chang_O07/Chang_O07 \
./part2/Fan_P046/Fan_P046 \
./part2/Hack_O35/Hack_O35 \
./part2/Liang_P55/Liang_P55 \
./part2/Wang_P57/Wang_P57 \
./part3/Carrasco_Kind_O06/Carrasco_Kind_O06 \
./part3/Glotfelty_I04/Glotfelty_I04 \
./part3/Yang_P045/Yang_P045 \
./part4/Berriman_O03/Berriman_O03 \
./part4/Fabbro_O11/Fabbro_O11 \
./part4/Farivar_O12/Farivar_O12 \
./part4/Gheller_P013/Gheller_P013 \
./part4/Kamennoff_O18/Kamennoff_O18 \
./part4/Laidler_O20/Laidler_O20a \
./part4/Laidler_O20/Laidler_O20 \
./part4/Laidler_O20/Laidler_O20.pjt \
./part4/Warner_O31/Warner_O31 \
./part5/Costa_O08/Costa_O08 \
./part5/Ibarra_P015/Ibarra_P015 \
./part5/Massimino_O24/Massimino_O24 \
./part5/Schaaff_O28/Schaaff_O28 \
./part5/Stephens_P39/Stephens_P39 \
./part6/Arviset_P02/Arviset_P02 \
./part6/Becker_P41/Becker_P41 \
./part6/Bell_P04/Bell_P04 \
./part6/Durand_O13/Durand_O13 \
./part6/Haase_O16/Haase_O16 \
./part6/Knapic_O19/Knapic_O19 \
./part6/Redman_P025/Redman_P025 \
./part6/Royer_P63/Royer_P63 \
./part6/Teplitz_O29/Teplitz_O29 \
./part6/Winkelman_O33/Winkelman_O33 \
./part6/Wu_P34/Wu_P34 \
./part7/Berthoud_P006/Berthoud_P006 \
./part7/Chilingarian_P58/Chilingarian_P58 \
./part7/Friedel_P12/Friedel_P12 \
./part7/Masters_P66/Masters_P66 \
./part7/Ott_O25/Ott_O25 \
./part7/Zhao_P36/Zhao_P36 \
./part8/Anderson_P01/Anderson_P01 \
./part8/Dencheva_P11/Dencheva_P11 \
./part8/Foucaud_O14/Foucaud_O14 \
./part8/Landais_P44/Landais_P44 \
./part8/Lee_P40/Lee_P40 \
./part8/Lubow_O21/Lubow_O21 \
./part8/MICHEL_P18/MICHEL_P18 \
./part8/Moins_P64/Moins_P64 \
./part8/Viallefond_P52/Viallefond_P52 \
./part9/Ball_P062/Ball_P062 \
./part9/Barache_P03/Barache_P03 \
./part9/Berry_P05/Berry_P05 \
./part9/Eguchi_O10/Eguchi_O10 \
./part9/Jenness_P56/Jenness_P56 \
./part9/Jeschke_O17/Jeschke_O17 \
./part9/Kapadia_F4/Kapadia_F4 \
./part9/Kavelaars_I07/Kavelaars_I07 \
./part9/Kawasaki_P47/Kawasaki_P47 \
./part9/Laurino_P020/Laurino_P020 \
./part9/Mink_P019/Mink_P019 \
./part9/Pascual_P21/Pascual_P21 \
./part9/Radhuber_P23/Radhuber_P23 \
./part9/Rauch_P24/Rauch_p24 \
./part9/Roby_O27/Roby_O27 \
./part9/Shuping_P50/Shuping_P50 \
./part9/Smareglia_P28/Smareglia_P28 \
./part9/Song_P65/Song_P65 \
./part9/Teuben_P059/Teuben_P059 \
./part9/Teuben_P059/Teuben_P059.new \
./part9/Tibbetts_P030/Tibbetts_P030 \
./part9/Tollerud_O30/Tollerud_O30 \
./part10/Bulgarelli_O05/Bulgarelli_O05 \
./part10/Csepany_O09/Csepany_O09 \
./part10/Currie_P61/Currie_P61 \
./part10/Diaz_P54/Diaz_P54 \
./part10/Dowell_P42/Dowell_P42 \
./part10/Kuemmel_P049/Kuemmel_P049 \
./part10/Lorente_P048/Lorente_P048 \
./part10/Martinez-rubi_O23/Martinez-rubi_O23 \
./part10/Perez_P022/Perez_P022 \
./part10/Pramskiy_P038/Pramskiy_P038 \
./part10/Shortridge_P027/Shortridge_P027 \
./part10/Williams_O32/Williams_O32 \
./part10/Yamauchi_P35/Yamauchi_P35 \
./part10/Young_O15/Young_O15 \
./part11/Allen_B1/Allen_B1 \
./part11/Allen_D1/Allen_D1 \
./part11/Ball_F5/Ball_F5 \
./part11/Burger_F2/Burger_F2 \
./part11/Shirasaki_D5/Shirasaki_D5 \
./part11/Taylor_B2/Taylor_B2 
