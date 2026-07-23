# STREAMLIT APP DINER SANNE 24072026

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageOps
import math 
from pathlib import Path


def maak_vierkant(afbeelding, grootte=250):
    afbeelding = ImageOps.exif_transpose(afbeelding)
    
    # Bereken de kleinste zijde en snij het midden eruit
    breedte, hoogte = afbeelding.size
    kleinste_zijde = min(breedte, hoogte)
    
    links = (breedte - kleinste_zijde) // 2
    boven = (hoogte - kleinste_zijde) // 2
    rechts = links + kleinste_zijde
    onder = boven + kleinste_zijde
    
    afbeelding = afbeelding.crop((links, boven, rechts, onder))
    afbeelding = afbeelding.resize((grootte, grootte))
    
    return afbeelding



st.set_page_config(page_title="Diner Sanne",
                  layout="wide")

st.title('Diner Sanne 24 juli 2026')


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Gang 1", "Gang 2", "Gang 3","Gang 4", "Gang 5", "Gang 6"])

# GANG 1 - Smoked rosemary cocktail
with tab1:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_cocktails = st.number_input("**Aantal cocktails**", value=1)
        mL_gin = 50
        mL_citroensap = 25
        mL_rozemarijnsiroop = 25
        aantal_takjes_rozemarijn = 2

        ingredienten = [f"{mL_gin*aantal_cocktails}mL Gin", f"{mL_citroensap*aantal_cocktails}mL Citroensap", f"{mL_rozemarijnsiroop*aantal_cocktails}mL rozemarijnsiroop", 
                        "IJsblokjes", f"{aantal_takjes_rozemarijn*aantal_cocktails} takje(s) rozemarijn"]
        beschikbaar = [ing for ing in ingredienten if st.checkbox(ing, key=f'key_{ing}_tab1')]

        st.write("**Voor de rozemarijnsiroop:**")
        mL_suiker_rms = 100
        mL_water_rms = 100
        aantal_takjes_rozemarijn_rms = 3
        ingredienten_rms = [f"{mL_suiker_rms}mL Suiker", f"{mL_water_rms}mL Water", f"{aantal_takjes_rozemarijn_rms} takjes rozemarijn"]
        beschikbaar_rms = [ing for ing in ingredienten_rms if st.checkbox(ing, key=f"key_{ing}_rms_tab1")]


    with col2:
        st.header("Smoked rosemary cocktail - Bereiding")
        IMG_DIR = Path("Afbeeldingen eten")
        img_path = IMG_DIR / "smoked rosemary gin.png"
        # afbeelding = Image.open(r"C:\Users\Gebruiker\OneDrive\Privé\Programmeren\Diner Sanne app\Afbeeldingen eten\smoked rosemary gin.png")
        afbeelding = Image.open(img_path)
        st.image(maak_vierkant(afbeelding, grootte=300))
        st.write("""
                **1.** Zet een takje rozemarijn in de rook en plaats het cocktailglas daar omgekeerd op.
                \n**2.** Meng in een cocktailshaker de gin, citroensap en rozemarijnsiroop samen met de ijsblokjes.
                \n**3.** Schenk in het cocktailglas en serveer met een takje rozemarijn erin.
                 """)

# GANG 2 - Scampi's in kerriesaus
with tab2:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_servings = st.number_input("**Aantal servings**", value=1)
        aantal_scampis = 6
        mL_room = 200
        aantal_ui = 0.5
        aantal_knoflook = 2
        ingredienten = [f"{aantal_scampis*aantal_servings} scampi's", f"{mL_room*aantal_servings}mL room culinair", "Kerriepoeder", 
                        f"{int(aantal_ui*aantal_servings) if (aantal_ui*aantal_servings).is_integer() else (aantal_ui*aantal_servings)} Ui",
                         f"{aantal_knoflook*aantal_servings} teentjes knoflook", "Roomboter", "Stokbrood"]
        beschikbaar = [ing for ing in ingredienten if st.checkbox(ing, key=f'key_{ing}_tab2')]

    with col2:
        st.header("Scampi's in kerriesaus - Bereiding")
        afbeelding = Image.open("C:/Users/Gebruiker/Downloads/afbeelding_scampi_test.jpg")
        afbeelding_vierkant = maak_vierkant(afbeelding, grootte=300)
        st.image(afbeelding_vierkant)
        st.write("""
                 **1.** Dep de scampi's droog en bestrooi met peper, zout.
                 \n**2.** Zet ondertussen de serveerborden in de oven om warm te maken.
                 \n**3.** Snijd de ui en knoflook fijn.
                 \n**4.** Bak de scampi's in ruim roomboter. Neem ze uit de pan als ze klaar zijn.
                 \n**5.** Bak de ui in de aangekoekte smaak van de scampi's.
                 \n**6.** Voeg de knoflook toe en myoneer de kerriepoeder. 
                 \n**7.** Voeg slagroom toe en laat licht inkoken.
                 \n**8.** Voeg de scampi's weer terug toe in de panen breng extra op smaak indien nodig.
                 """)


# GANG 3 - Crispy rice met zalmtartaar
with tab3:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_porties = st.number_input("**Aantal servings**", value=10, step=2)
        initial_porties = 10
        st.write('**Voor de rijst:**')
        sushirijst = 250*(2/3)
        eetlepel_rijstazijn = 2*(2/3)
        theelepel_suiker = 2*(2/3)
        theelepel_sesamolie = 1*(2/3)
        ingredienten_rijst = [f"{round(sushirijst*(aantal_porties/initial_porties))}g sushirijst", 
                              f"{round((eetlepel_rijstazijn*(aantal_porties/initial_porties))*2)/2:g} eetlepels rijstazijn",
                               f"{round((theelepel_suiker*(aantal_porties/initial_porties))*2)/2:g} theelepels suiker", 
                               f"{round((theelepel_sesamolie*(aantal_porties/initial_porties))*2)/2:g} theelepels sesamolie"]
        
        beschikbaar = [ing for ing in ingredienten_rijst if st.checkbox(ing, key=f'key_{ing}_tab3_rijst')]

        st.write('**Voor de zalm:**')
        g_zalm = 150*(2/3)
        aantal_bosui = 0.5
        eetlepel_japanse_mayo = 1*(2/3)
        theelepel_sriracha = 1*(2/3)
        theelepel_sojasaus = 2*(2/3)
        theelepel_sesamolie_zalm = 1*(2/3)
        theelepel_citroensap = 1*(2/3)
        
        ingredienten_zalm = [f"{g_zalm*(aantal_porties/initial_porties)}g zalmfilet", 
                             f"{aantal_bosui*(aantal_porties/initial_porties)} bosui",
                             f"{round((eetlepel_japanse_mayo*(aantal_porties/initial_porties)) * 2) / 2:g} eetlepel japanse mayonaise",
                             f"{round((theelepel_sriracha*(aantal_porties/initial_porties)) * 2) / 2:g} theelepel sriracha",
                             f"{round((theelepel_sojasaus*(aantal_porties/initial_porties)) * 2) / 2:g} theelepel sojasaus",
                             f"{round((theelepel_sesamolie_zalm*(aantal_porties/initial_porties)) * 2) / 2:g} theelepel sesamolie",
                             f"{round((theelepel_citroensap*(aantal_porties/initial_porties)) * 2) / 2:g} theelepel citroensap"]
        

        beschikbaar_zalm = [ing for ing in ingredienten_zalm if st.checkbox(ing, key=f'key_{ing}_tab3_zalm')]


        st.write('**Voor de toppings:**')
        avocado = 1*(2/3)
        ingredienten_toppings = [f"{round(avocado*(aantal_porties/initial_porties)*2)/2:g} avocado",
                                 "Geroosterde sesamsaadjes"]
        beschikbaar_toppings = [ing for ing in ingredienten_toppings if st.checkbox(ing, key=f"key_{ing}_tab3_toppings")]




    with col2:
        st.header("Crispy rice met zalmtartaar - Bereiding")
        afbeelding = Image.open("C:/Users\/Gebruiker/OneDrive/Privé/Programmeren/Diner Sanne app/Afbeeldingen eten/433235a9-0dc4-4a23-9763-1928519cf433.JPG")
        st.image(maak_vierkant(afbeelding, grootte=300))

        st.write("""
            **1.** Begin met de rijst: was en kook de rijst.
            \n**2.** Meng suiker, rijstazijn en sesamolie in een kom. Voeg toe aan de gekookte rijst en meng goed. Schik de rijst in een rechthoekige ovenschaal. Druk de rijst goed aan en laat minsten één uur afkoelen in de koelkast.
            \n**3.** Meng in een andere kom de Japanse mayonaise, sojasaus, sriracha, bosui en de blokjes zalm. 
            \n**4.** Snijd de rijst in rechthoekige plakjes en frituur tot ze mooi goudbruin zijn. Laat vervolgens uitlekken op keukenpapier.
            \n**5.** Opmaken: Leg een paar plakjes avocado op de krokante rijst. Leg een lepel spicy zalm bovenop en werk af met geroosterde sezamzaadjes.
                 """)

        # st.write('bron: https://www.culy.nl/recepten/crispy-rice-met-zalm/')



# GANG 4 - Tapioca crisps & Basil smash
with tab4:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_servings = st.number_input("Aantal servings", value=2, step=2)
        initial_servings = 2
        st.write("**Voor de tapioca crisps:**")
        tapioca_pearls = 90 
        mL_water_tp = 590
        ingredienten_tc = [f"{int(tapioca_pearls*(aantal_servings/initial_servings))}g Tapioca pearls",
                           f"{int(mL_water_tp*(aantal_servings/initial_servings))}mL water", 
                           "Kerriepoeder", "Kurkumapoeder", "Paprikapoeder", "Knoflookpoeder", "Cayennepeper"]
        beschikbaar_tc = [ing for ing in ingredienten_tc if st.checkbox(ing, key=f'key_{ing}_tab4')]

        st.write("**voor de limoenmayonaise:**")
        # voor ca. 250 mL == 4 pers. --> als #servings * 4 dan verhogen met 1 deel.
        eidooier = 2.0
        theelepel_sushiazijn = 1.0
        theelepel_mosterd = 1.0
        theelepel_knoflookpoeder = 0.5
        limoensap = 0.5
        zonnebloemolie_mL = 200.0
        ingredienten_limoenmayo = [f"{eidooier*(max(aantal_servings / 4, 1))} eidooier",
                                   f"{theelepel_sushiazijn*(max(aantal_servings / 4, 1))} theelepel (sushi)azijn",
                                   f"{theelepel_mosterd*(max(aantal_servings / 4, 1))} eetlepel grove mosterd",
                                   f"{theelepel_knoflookpoeder*(max(aantal_servings / 4, 1))} theelepel knoflookpoeder",
                                   f"Sap van {limoensap*(max(aantal_servings / 4, 1))} limoen",
                                   f"{zonnebloemolie_mL*(max(aantal_servings / 4, 1))}mL zonnebloemolie"]
        beschikbaar_limoenmayo = [ing for ing in ingredienten_limoenmayo if st.checkbox(ing,key=f'key_{ing}_tab4_lm')]

        st.write("**Voor de gerooktepaprikamayonaise:**")
        mayonaise = 150 
        theelepel_gpp = 2
        aantal_knoflook = 1
        theelepel_citroensap = 1
        theelepel_suiker = 0.5
        ingredienten_gpmayo = [f"{mayonaise*(max(aantal_servings / 4, 1))}g mayonaise", 
                               f"{theelepel_gpp*(max(aantal_servings / 4, 1))} theelepel gerooktepaprikapoeder", 
                               f"{aantal_knoflook*(max(aantal_servings / 4, 1))} teenjes knoflook",
                               f"{theelepel_citroensap*(max(aantal_servings / 4, 1))} theelepel citroensap",
                               f"{theelepel_suiker*(max(aantal_servings / 4, 1))} theelepel suiker of honing"]
        beschikbaar_gpmayo = [ing for ing in ingredienten_gpmayo if st.checkbox(ing, key=f"key_{ing}_tab4_gpm")]


        aantal_servings_cocktail = st.number_input("Aantal cocktails", value=1)
        st.write('**Voor de cocktail:**') # basil smash (bs)
        mL_gin = 45
        mL_citroensap = 20
        mL_suikersiroop = 15
        basilicum_blaadjes = 10
        ingredienten_bs = [f"{mL_gin*aantal_servings_cocktail}mL Gin", 
                           f"{mL_citroensap*aantal_servings_cocktail}mL citroensap", 
                           f"{mL_suikersiroop*aantal_servings_cocktail}mL suikersiroop", 
                           f"{basilicum_blaadjes*aantal_servings_cocktail} basilicumblaadjes",
                           "IJsblokjes"]
        beschikbaar_bs = [ing for ing in ingredienten_bs if st.checkbox(ing, key=f"key_{ing}_tab4_bs")]

    with col2:
        st.header("Tapioca crisps met gerooktepaprikamayonaise & limoenmayonaise - Bereiding")
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            afbeelding = Image.open("C:/Users/Gebruiker/OneDrive/Privé/Programmeren/Diner Sanne app/Afbeeldingen eten/tapiocacrisps.jpeg")
            st.image(maak_vierkant(afbeelding, 300))

            st.write("""**Tapioca crisps:**
                     \n**1.** Verdeel de tapicoa pearls over twee pannen en kook deze met de het bijbehorende aandeel water.
                     \n**2.** Voeg de kruiden toe. In één pan de kerrie-, kurkuma- en knoflookpoeder. In de andere pan de paprika-, cayenne- en knoflookpoeder.
                     \n**3.** Laat al roerend indikken tot een gelei. Indien het te snel indikt, voeg extra water toe.
                     \n**4.** De parels zijn klaar als de meeste transparant zijn.
                     \n**5.** Was de parels goed af in een zeef met koud water. Voeg eventueel nog extra kruiden toe.
                     """)
            afbeelding_1 = Image.open(r"C:\Users\Gebruiker\OneDrive\Privé\Programmeren\Diner Sanne app\Afbeeldingen eten\IMG_0623.jpeg")
            st.image(maak_vierkant(afbeelding_1, 200))
            st.write("""
                    **6.** Sprijd de afgespoelde parels over een bakplaat.
                     \n**7.** Laat de parels in een voorverwarmde oven op 80-100°C uitdrogen gedurende ca. 3 uur.
                     """)
            afbeelding_2 = Image.open(r"C:\Users\Gebruiker\OneDrive\Privé\Programmeren\Diner Sanne app\Afbeeldingen eten\IMG_0631.jpeg")
            st.image(maak_vierkant(afbeelding_2, 200))
            st.write("""
                    **8.** Wanneer de gelei hard/krokant is, is het voldoende uitgedroogd.
                     \n**9.** Frituur stukken van de tapioca pearls in zonnebloemolie op ca. 150-170°C.
                     \n**10.** Bestrooi de tapioca crisps gelijk met fijn zout.
                     \n**11.** Serveer met gerooktepaprikamayonaise en limoenmayonaise.
                     """)
            
            st.divider()
            st.write("""
                    **De gerooktepaprikamayonaise:**
                     \n**1.** Myoteer de paprikapoeder, knoflook en suiker. Laat afkoelen.
                     \n**2.** Meng de mayonaise met de gemyoteerde kruiden en voeg de citroensap toe.
                     \n**3.** Serveer in een mooi schaaltje.
                     """)
            
            st.divider()
            st.write("""
                    **De limoenmayonaise**
                     \n**1.** Mix de eidooiers, (sushi)azijn, mosterd, limoenrasp, limoensap en knoflookpoeder.
                     \n**2.** Staaf het mengsel op met beetje bij beetje zonnebloemolie.
                     \n**3.** Serveer in een mooi schaaltje
                     """)
 
        with sub_col2:
            afbeelding2 = Image.open("C:/Users/Gebruiker/OneDrive/Privé/Programmeren/Diner Sanne app/Afbeeldingen eten/basil-smash-800x600.png")
            st.image(maak_vierkant(afbeelding2, 300))

            st.write("""
                **1.** Doe de basilicumblaadjes in een cocktailshaker en stamp fijn.
                \n**2.** Voeg de gin, citroensap en suiker toe aan de shaker.
                \n**3.** Vul de shaker met ijsblokjes en schud ca. 15 seconden.
                \n**4.** Giet de cocktail door een fijne zeef in een glas gevuld met ijs.
                     """)



# GANG 5 - Lamsrack
with tab5:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_servings = st.number_input("Aantal servings", value=2)
        initial_servings = 2
        lamskoteletjes = 2
        eekhoortjesbrood = 150
        erwten = 100
        groen_asperges = 100

        ingredienten = [f"{aantal_servings/lamskoteletjes} lamsrack (ca.{lamskoteletjes * aantal_servings} koteletjes)", 
                        "Dijon mosterd",
                        f"{eekhoortjesbrood*(aantal_servings/initial_servings)}g eekhoorntjesbrood",
                        f"{erwten*(aantal_servings/initial_servings)}g erwten",
                        f"{groen_asperges*(aantal_servings/initial_servings)}g groene asperges of broccolini"]
        beschikbaar = [ing for ing in ingredienten if st.checkbox(ing, key=f'key_{ing}_tab5')]

        st.write("**Voor de kruidenkorst:**")
        panko = 30
        daslook = 30
        aantal_bosui_alternatief = 4
        aantal_knoflook_alternatief = 1
        pistachenoten = 20
        olijfolie = 15
        ingredienten_kk = [f"{panko*(aantal_servings/initial_servings)}g panko",
                            f"{daslook*(aantal_servings/initial_servings)}g daslook* (wilde knoflook)",
                            f"{pistachenoten*(aantal_servings/initial_servings)}g pistachenoten",
                            f"{olijfolie*(aantal_servings/initial_servings)}mL olijfolie", 
                            "Zout",]
        beschikbaar_kk = [ing for ing in ingredienten_kk if st.checkbox(ing, key=f"key_{ing}_tab5_kk")]
        st.markdown(f"*<small> Als vervanger kan worden gebruikt: {(aantal_servings/initial_servings)*aantal_bosui_alternatief} bosuitjes "
                    f"en {(aantal_servings/initial_servings)*aantal_knoflook_alternatief} knoflookteentje(s).<small>", unsafe_allow_html=True)

        st.write("**Voor de rodewijnsaus:**")
        rodewijn = 240
        fond = 120
        sjalot = 1
        tl_tijm = 1
        ingredienten_rws = [f"{rodewijn*(aantal_servings/initial_servings)}mL rode wijn (Côtes du Rhône)",
                            f"{fond*(aantal_servings/initial_servings)}mL kalf- of runderfond",
                            f"{sjalot*(aantal_servings/initial_servings)} sjalot, fijngesnippeld",
                            f"{tl_tijm*(aantal_servings/initial_servings)} theelepel verse tijm"]
        beschikbaar_rws = [ing for ing in ingredienten_rws if st.checkbox(ing, key=f"key_{ing}_tab5_rws")]

        st.write("**Voor de groene pesto:**")
        daslook_gp = 40
        aantal_bieslook_alternatief_gp = 1
        aantal_knoflook_alternatief_gp = 1
        pistachenoten_gp = 20
        olijfolie_gp = 60
        el_citroensap = 1
        ingredienten_gp = [f"{daslook_gp*(aantal_servings/initial_servings)}g daslook* (wilde knoflook)",
                           f"{pistachenoten_gp*(aantal_servings/initial_servings)}g pistachenoten",
                           f"{olijfolie_gp*(aantal_servings/initial_servings)}mL olijfolie",
                           f"{el_citroensap*(aantal_servings/initial_servings)} eetlepel citroensap",
                           "Zout"]
        beschikbaar_gp = [ing for ing in ingredienten_gp if st.checkbox(ing, key=f"key_{ing}_tab5_gp")]  
        st.markdown(f"*<small> Als vervanger kan worden gebruikt: {aantal_bieslook_alternatief_gp*(aantal_servings/initial_servings)} bosje bieslook "
                    f"en {aantal_knoflook_alternatief_gp*(aantal_servings/initial_servings)} teentje(s) knoflook en een handje peterselie.<small>", unsafe_allow_html=True)

        st.write("**Voor de afwerking:**")
        ingredienten_afwerking = ["Microgreens", "Eetbare bloemen"]
        beschikbaar_afwerking = [ing for ing in ingredienten_afwerking if st.checkbox(ing, key=f"key_{ing}_tab5_afw")]

    
    with col2:
        st.header("Lamsribbetjes met een korst van wilde look, porcini, knoflookstengels en erwten - Bereiding")
        afbeelding = Image.open("C:/Users/Gebruiker/OneDrive/Privé/Programmeren/Diner Sanne app/Afbeeldingen eten/lam.jpg")
        st.image(maak_vierkant(afbeelding, 300))

        st.write("""
            **Kruidenkorst:**
                 \n**1.** Meng tot een grof kruidenmengsel.
                 \n**2.** Wrijf de gebakken lamsrack in met Dijonmosterd.
                 \n**3.** Druk het kruidenmengels aan op de aangebakken lamsrack.
                 \n
            \n**Lamskoteletten:** 
                 \n**1.** Haal het vlees ongeveer 30 minuten vooraf uit de koelkast.
                 \n**2.** Dep droog en kruid met peper en zout.
                 \n**3.** Bak het lamsrack rondom goudbruin.
                 \n**4.** Bestrijk de vleeskant met Dijonmosterd.
                 \n**5.** Druk de kruidenkorst stevig op het vlees.
                 \n**6.** Laat verder garen in de oven op 200°C tot een kerntemperatuur van ca. 55°C (ongevver 10 minuten).
                 \n**7.** Laat minstens 10 minuten rusten voor aansnijden.
                 \n
            \n**Rodewijnsaus:**
                 \n**1.** Fruit de sjalot kort aan.
                 \n**2.** Voeg de wijn toe en laat inkoken tot ongeveer de helft.
                 \n**3.** Voeg de fond en tijm toe.
                 \n**4.** Laat verder inkoken tot een mooie, stroperige jus.
                 \n**5.** Zeef de saus.
                 \n**6.** Monteer vlak voor het serveren met een klein blokje koude boter voor een extra glans.
                 \n
            \n**Groenten:**
                 \n**1.** Bak de paddenstoelen goudbruin
                 \n**2.** Voeg de groene asperges of broccolini (bimi) toe.
                 \n**3.** Voeg als laatste de doperwten toe zodat ze mooi groen blijven.
                 \n**4.** Breng op smaak met peper en zout.
                 \n
            \n**Groene pesto:**
                 \n**1.** Blend alles tot een gladde pesto. 
                 """)


# GANG 6 - Chocoladekopjes
with tab6:
    col1, col2 = st.columns([1,3], border=True)
    with col1:
        st.header("Ingrediënten")
        aantal_personen = st.number_input("Aantal personen", value = 12, step=2)
        initial_personen = 12
        chocolade = 300
        roomboter = 200
        eieren = 6
        basterdsuiker = 150

        ingredienten = [f"{chocolade*(aantal_personen/initial_personen)}g pure chocolade (70%) van goede kwaliteit", 
                        f"{round(roomboter*(aantal_personen/initial_personen))}g roomboter",
                        f"{eieren*(aantal_personen/initial_personen)} klein/middel eieren",
                        f"{basterdsuiker*(aantal_personen/initial_personen)}g lichtbruine basterdsuiker"]
        
        # round((theelepel_sesamolie*(aantal_porties/initial_porties))*2)/2:g
        beschikbaar = [ing for ing in ingredienten if st.checkbox(ing, key=f'key_{ing}_tab6')]
    with col2:
        st.header("Chocoladekopjes - Bereiding")
        st.write("""
                **1.** Verwarm de over voor op 160°C.
                 \n**2.** Breek de chocolade in stukjes en smelt ze met een snufje zout au bain marie. Laat 15 minuten afkoelen.
                 \n**3.** Klop in een andere kom de eieren en suiker dik en luchtig en giet er al kloppend het chocolademengsel bij.
                 \n**4.** Verdeel het mengsel over ovenbestendige theekopje of ramekins en zet die in een grote, diepe braadslede.
                 \n**5.** Zet de braadslede in de oven en giet er kokend water bij tot de helft van de kopjes.
                 \n**6.** Bak 25 minuten, haal de kopjes uit de slede en laat ze voor het serveren minstens 15 minuten staan.
                 """)











