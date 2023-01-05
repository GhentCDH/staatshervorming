# readme

## bestanden

| bestand              | Inhoud                                                                                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| naamdatatabel.txt    | Basis persoonsgegevens, link naar reftabel.txt: cijfers die tussen haakjes staan                                                                                                 |
| kwnatificeerbaar.txt | Persoonsfuncties, link naar anderefunc.txt (Functieandere1, Functieandere2); geogrfisch.txt (Origine); sociaal.txt (Sociaal); leekcler.txt (LeekClericus); studies.txt (Studies) |
| Titeltabel.txt       | Persoonstitels, link naar reftabel.txt: cijfers die tussen haakjes staan                                                                                                         |
| Afkortingen.txt      | Afkortingen van bronnen, ... (kunnen eventueel als html title attribuut worden toegevoegd) die voorkomen in basis persoonsgegevens en in de reftabel                           |
| bronnen.txt          | Beschrijvende tekst over de keuze van de bronnen                                                                                                                               |
| help.txt             | Beschrijvende tekst + tabellen                                                                                                                                                 |

*   Processing van CSVs met Ptyhon en [Jinja](https://github.com/pallets/jinja)
    *   Overzichtstabel van personen opbouwen met [jQuery DataTables](https://github.com/DataTables/DataTables), zodat eenvoudige filteroperaties mogelijk zijn
    *   Detailpagina&#39;s van personen met daarin
        *   de volledige tekst (in secties met inpage navigatie: sociaal, coltureel, bezit, carriere)
            *   referenties in de tekst weergeven als afkortingen die linken naar de corresponderende entry in de overzichtslijst onderaan de pagina
        *   titels in een zijkolom
        *   de kwantificeerbare data in een zijkolom
        *   een overzicht van de referenties met zowel de afkorting als de volledige titel van de referentie
    *   (Detailpagina&#39;s van referenties met de volledige titel van de referentie en een lijst met alle personen die gebruik maken van deze referentie)
