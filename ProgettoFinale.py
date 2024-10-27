#Introduzione

'''
All'interno di questo codice andrò ad analizzare l'evoluzione e le tendenze principali emerse sulla piattaforma culinaria nel corso degli ultimi tre anni. Attraverso una panoramica dettagliata delle categorie 
alimentari, del coinvolgimento degli utenti e del numero crescente di ricette, esplorererò come la comunità gastronomica ha risposto e si è adattata alle nuove preferenze culinarie. Esaminererò anche il contributo 
di diversi paesi, la varietà delle ricette postate, e come queste riflettano le nuove abitudini alimentari e gli stili di vita sostenibili. 
'''

import pandas as pd                     # Importazione della libreria pandas, utilizzata per la manipolazione e l'analisi dei dati strutturati.
import matplotlib.pyplot as plt         # Importazione di pyplot dal modulo matplotlib, che fornisce una serie di funzioni per creare grafici 2D.
import matplotlib as mpl                # Importazione del modulo matplotlib, utile per gestire aspetti avanzati dei grafici, come le colormap.
import numpy as np                      # Importazione della libreria numpy, utilizzata per il calcolo numerico efficiente su array multidimensionali.
import matplotlib                       # Importazione di matplotlib per l'uso di funzionalità avanzate legate ai colori e alla personalizzazione dei grafici.

# Definire una funzione per aggiungere etichette ai grafici con valori in formato float 
def etichetta_float():
    '''
    Aggiunge etichette alle barre di un grafico a barre, mostrando i valori delle altezze delle barre con due cifre decimali.

    Args:
        None

    Returns: 
        None

    Note:
        Questa funzione presuppone che il grafico a barre sia stato precedentemente creato e che le barre siano contenute in `bars.patches`.
    '''
    for bar in bars.patches:                            # Inizia un ciclo per ogni barra presente nel grafico
        plt.text(bar.get_x() + bar.get_width() / 2,     # Calcola la posizione X al centro della barra
             bar.get_height(),                          # Imposta la posizione Y all'altezza della barra
             f'{bar.get_height():.2f}',                 # Format del valore della barra con 2 decimali
             ha='center',                               # Allinea orizzontalmente il testo al centro della barra
             va='bottom',                               # Allinea verticalmente il testo alla parte superiore della barra
             fontsize=10,                               # Imposta la dimensione del font dell'etichetta a 10
             fontweight='bold')                         # Imposta il peso del font dell'etichetta a grassetto

# Definire una funzione per aggiungere etichette ai grafici con valori interi 
def etichetta_int():
    '''
    Aggiunge etichette alle barre di un grafico a barre, mostrando i valori delle altezze delle barre come numeri interi.

    Args:
        None

    Returns: 
        None

    Note:
        Questa funzione presuppone che il grafico a barre sia stato precedentemente creato e che le barre siano contenute in `bars.patches`.
    '''
    for bar in bars.patches:                            # Inizia un ciclo per ogni barra presente nel grafico
        plt.text(bar.get_x() + bar.get_width() / 2,     # Calcola la posizione X al centro della barra
             bar.get_height(),                          # Imposta la posizione Y all'altezza della barra
             f'{int(bar.get_height())}',                # Format del valore della barra con un intero
             ha='center',                               # Allinea orizzontalmente il testo al centro della barra
             va='bottom',                               # Allinea verticalmente il testo alla parte superiore della barra
             fontsize=10,                               # Imposta la dimensione del font dell'etichetta a 10
             fontweight='bold')                         # Imposta il peso del font dell'etichetta a grassetto

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Caricamento Dataset (Excel)
df = pd.read_excel(r'C:\Users\alessandro\Desktop\file famiglia\Alessandro\Corso Start2Impact\09 - Progetto Finale\Food_data Final Project.xlsx') # Inserisce il dataset Excel nella variabile df

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Calcola il numero di utenti, chef e ricette.
unique_users = df['user_uuid'].nunique()            # Numero di utenti unici
unique_chefs = df['chef_id'].nunique()              # Numero di chef unici
unique_recipes = df['recipe_id'].nunique()          # Numero di ricette uniche

# Storytelling sul numero di utenti, chef e ricette.
story = (
        "All'interno del file .xlsx vi sono "
        f"{unique_users} utenti unici che esplorano le meraviglie della cucina, "
        f"di cui {unique_chefs} chef talentuosi che offrono il loro tocco unico a ogni ricetta, "
        f"per un totale di {unique_recipes} ricette uniche, ognuna pronta a ispirare "
        "gli utenti a intraprendere un viaggio culinario indimenticabile."
    )
    
print(story)                                            # Stampa dello Storytelling 

# Stampa il numero di utenti, chef e ricette unici 
print("\n")                                             # Stampa una riga vuota per avere lo spazio necessario tra una visualizzazione ed un'altra.
print(f"Riepilogo:")                                    # Stampa "Riepilogo"
print(f"Numero di utenti unici: {unique_users}")        # Stampa il numero di utenti unici
print(f"Numero di chef unici: {unique_chefs}")          # Stampa il numero di chef unici
print(f"Numero di ricette uniche: {unique_recipes}")    # Stampa il numero di ricette uniche
print("-" * 40)                                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il numero di ricette per anno 
df['cooking_date'] = pd.to_datetime(df['cooking_date'])         # Converte la colonna 'cooking_date' in formato datetime
cases_per_year = df.groupby(df['cooking_date'].dt.year).size()  # Raggruppa i dati per anno basato sulla colonna 'cooking_date'

# Storytelling sul numero di ricette per anno
story = (
        "Negli ultimi tre anni, la nostra piattaforma ha vissuto una crescita esponenziale nel numero di ricette condivise. "
        f"Nel 2021, abbiamo visto l'emergere di {cases_per_year[2021]} ricette, mentre nel 2022 questo numero è aumentato "
        f"fino a raggiungere {cases_per_year[2022]} ricette. "
        f"Ma la vera esplosione è avvenuta nel 2023, con un impressionante totale di {cases_per_year[2023]} ricette! "
        "Questo trend evidenzia un crescente interesse nella cucina e nella condivisione di esperienze culinarie, "
        "portando a una comunità sempre più attiva e coinvolta."
    )
    
print(story) # Stampa dello Storytelling 

print("\n")                                             # Stampa una riga vuota per avere lo spazio necessario tra una visualizzazione ed un'altra.
print(f"Riepilogo:")                                    # Stampa "Riepilogo"
print("Numero di casi per anno:")                       # Stampa "Numero di casi per anno"
print(cases_per_year)                                   # Stampa il numero di ricette per anno
print("-" * 40)                                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il numero di ricette per anno 
df['year'] = df['cooking_date'].dt.year                                                     # Aggiunge una colonna che contiene l'anno estratto dalla variabile "cooking_date"
category_counts_per_year = df.groupby(['year', 'category']).size().unstack(fill_value=0)    # Raggruppa i dati per anno e categoria, contando le ricette di ciascuna categoria

# Storytelling sul numero di ricette per categorie e per anno
story = (
    "Negli ultimi tre anni, abbiamo assistito a un notevole cambiamento nel panorama culinario della nostra piattaforma.\n"
    
    # Analisi per l'anno 2021
    "Nel 2021, le seguenti categorie hanno avuto un impatto significativo:\n"
    f"- 'breakfast' ha contribuito con 16 ricette, dimostrando un crescente interesse per la colazione.\n"
    f"- 'dinner', sebbene meno popolare, ha avuto 14 ricette, evidenziando la continua ricerca di pasti serali.\n"
    f"- La categoria 'ethnic' si è distinta con 47 ricette, riflettendo l'interesse della comunità per la cucina internazionale.\n"
    f"- 'lunch' ha registrato 9 ricette, suggerendo che il pranzo non era ancora una priorità per molti.\n"
    f"- 'smoothie' ha raccolto 12 ricette, mostrando un'influenza crescente delle tendenze salutistiche.\n"
    f"- 'snack', con 4 ricette, ha avuto una presenza limitata, mentre i piccoli pasti non erano ancora in voga.\n"
    f"- Infine, la categoria 'vegan' ha visto 6 ricette, segnalando un inizio di interesse per l'alimentazione vegetale.\n"
    
    # Analisi per l'anno 2022
    "Nel 2022, le seguenti categorie hanno avuto un notevole impatto:\n"
    f"- 'breakfast' ha visto una crescita straordinaria, con 54 ricette, che indicano un aumento dell'attenzione per la colazione.\n"
    f"- La categoria 'dinner' ha raggiunto 33 ricette, mostrando una maggiore varietà di opzioni per la cena.\n"
    f"- 'ethnic' è esplosa con 88 ricette, rivelando un forte interesse per la gastronomia globale.\n"
    f"- 'lunch' ha guadagnato terreno con 31 ricette, segnalando che il pranzo è diventato più importante nella routine culinaria.\n"
    f"- 'smoothie' ha continuato a crescere, con 20 ricette, in linea con le tendenze salutistiche.\n"
    f"- 'snack' è aumentata a 21 ricette, evidenziando un cambiamento nel consumo di pasti leggeri.\n"
    f"- La categoria 'vegan' ha visto anch'essa un incremento con 21 ricette, indicando un crescente interesse per stili di vita più sostenibili.\n"
    
    # Analisi per l'anno 2023
    "Nel 2023, le seguenti categorie hanno avuto un impatto significativo:\n"
    f"- 'breakfast' ha trionfato con 101 ricette, confermando la colazione come pasto fondamentale per gli utenti della nostra piattaforma.\n"
    f"- 'dinner' ha contribuito con 62 ricette, mostrando una varietà ancora maggiore nella scelta dei pasti serali.\n"
    f"- La categoria 'ethnic' ha raggiunto un incredibile 214 ricette, dimostrando un'affermazione chiara della cucina internazionale.\n"
    f"- 'lunch' ha continuato la sua ascesa con 106 ricette, consolidando la sua posizione tra le preferenze alimentari.\n"
    f"- 'smoothie' ha mantenuto il suo slancio con 40 ricette, suggerendo che le opzioni salutari sono sempre più ricercate.\n"
    f"- 'snack' ha visto 52 ricette, indicando un significativo aumento nell'attenzione per i pasti leggeri e i piccoli spuntini.\n"
    f"- Infine, 'vegan' ha avuto 48 ricette, segnalando una continua crescita dell'interesse per le opzioni vegetali.\n"
    
    # Analisi finale sul cambiamento degli anni
    "Analisi finale:\n"
    "Osservando i dati degli ultimi tre anni, emerge un chiaro trend di crescita nel numero complessivo di ricette e nella diversità delle categorie. "
    "Dal 2021 al 2023, il numero di ricette nella categoria 'breakfast' è aumentato da 16 a 101, evidenziando un forte cambiamento nelle abitudini alimentari.\n"
    "La categoria 'dinner' ha visto un incremento moderato, ma costante, mentre 'ethnic' ha registrato un'impennata straordinaria, passando da 47 a 214 ricette, "
    "sottolineando l'apertura culturale e la voglia di esplorare sapori diversi.\n"
    "La categoria 'lunch' ha registrato una crescita significativa, passando da 9 a 106 ricette, indicativa di un cambiamento nelle routine quotidiane degli utenti.\n"
    "Le categorie 'smoothie', 'snack' e 'vegan' hanno mostrato un incremento continuo, riflettendo l'interesse crescente per un'alimentazione sana e sostenibile.\n"
    "In sintesi, la nostra piattaforma sta diventando un riflesso delle tendenze culinarie contemporanee, con un'utenza sempre più consapevole e desiderosa di diversificare la propria esperienza gastronomica."
)

print(story) # Stampa dello Storytelling

print("\n")                                             # Stampa una riga vuota per avere lo spazio necessario tra una visualizzazione ed un'altra.
print(f"Riepilogo:")                                    # Stampa "Riepilogo"
print("Numero di ricette per categorie e per anno:")    # Stampa "Numero di ricette per categorie e per anno"
print(category_counts_per_year)                         # Stampa il numero di ricette per categorie e per anno
print("-" * 40)                                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra lo chef più attivo e il conteggio delle sue ricette per anno e categoria 
chef_counts = df['chef_id'].value_counts()                      # Conta quante volte si ripete ciascuno chef nella colonna 'chef_id'
most_frequent_chef = chef_counts.idxmax()                       # Identifica lo chef_id con il maggior numero di ricette
most_frequent_chef_count = chef_counts.max()                    # Numero totale di ricette per lo chef più attivo
df['year'] = df['cooking_date'].dt.year                         # Aggiunge una colonna per l'anno estratto dalla data 
df_most_frequent_chef = df[df['chef_id'] == most_frequent_chef] # Filtra il dataset per ottenere solo i dati relativi allo chef più attivo

# Raggruppa i dati dello chef per anno e categoria, contando le ricette per ogni anno
chef_counts_per_year_category = df_most_frequent_chef.groupby(['year', 'category']).size().unstack(fill_value=0)

print(f"Lo chef_id che si ripete più volte è: {most_frequent_chef} con {most_frequent_chef_count} ricette totali.")  # Stampa lo chef più attivo e il conteggio  totale delle sue ricette
print("Numero di ricette dello chef_id per anno e categoria:")                                                       # Stampa "Numero di ricette dello chef_id per anno e categoria:"
print(chef_counts_per_year_category)                                                                                 # Stampa lo chef più attivo e il conteggio delle sue ricette per anno e categoria

# Storytelling che mostra lo chef più attivo e il conteggio delle sue ricette per anno e categoria
story = (
    "Nel mondo della nostra piattaforma culinaria, uno chef ha catturato l'attenzione di tutti per il suo eccezionale numero di ricette.\n"
    f"Lo chef con l'ID {most_frequent_chef} si è dimostrato il più prolifico, con un totale di {most_frequent_chef_count} ricette pubblicate nel corso degli anni.\n"

    "Analizzando le sue ricette per anno e categoria, emergono tendenze interessanti:\n"

    # Dettagli per l'anno 2021
    "Nel 2021, lo chef ha pubblicato:\n"
    f"- {chef_counts_per_year_category.loc[2021, 'breakfast']} ricette nella categoria 'breakfast', dimostrando una passione per la prima colazione.\n"
    f"- {chef_counts_per_year_category.loc[2021, 'dinner']} ricette nella categoria 'dinner', indicando un impegno anche nei pasti serali.\n"
    f"- {chef_counts_per_year_category.loc[2021, 'ethnic']} ricette 'ethnic', evidenziando l'interesse per la cucina internazionale con 4 piatti.\n"
    f"- Non ci sono state ricette per la categoria 'lunch', mentre ha contribuito con {chef_counts_per_year_category.loc[2021, 'smoothie']} ricette di 'smoothie', 1 di 'vegan' e nessuna di 'snack'.\n"

    # Dettagli per l'anno 2022
    "Nel 2022, il suo repertorio ha continuato a crescere:\n"
    f"- La categoria 'breakfast' non ha avuto ricette, ma ha creato {chef_counts_per_year_category.loc[2022, 'dinner']} ricette per la cena.\n"
    f"- Ha preparato {chef_counts_per_year_category.loc[2022, 'ethnic']} piatti 'ethnic', con un aumento rispetto all'anno precedente.\n"
    f"- Nella categoria 'lunch', ha prodotto {chef_counts_per_year_category.loc[2022, 'lunch']} ricette, suggerendo una maggiore attenzione per il pranzo.\n"
    f"- Ha creato {chef_counts_per_year_category.loc[2022, 'smoothie']} ricette di 'smoothie', {chef_counts_per_year_category.loc[2022, 'snack']} di 'snack' e nessuna di 'vegan'.\n"

    # Dettagli per l'anno 2023
    "Nel 2023, lo chef ha raggiunto nuovi traguardi:\n"
    f"- La categoria 'breakfast' è esplosa con {chef_counts_per_year_category.loc[2023, 'breakfast']} ricette, consolidando il suo status come esperto nella prima colazione.\n"
    f"- Per quanto riguarda la categoria 'dinner', ha creato {chef_counts_per_year_category.loc[2023, 'dinner']} piatti, evidenziando un'ampia varietà di opzioni serali.\n"
    f"- La cucina 'ethnic' è stata un grande successo, con ben {chef_counts_per_year_category.loc[2023, 'ethnic']} ricette.\n"
    f"- Ha anche pubblicato {chef_counts_per_year_category.loc[2023, 'lunch']} ricette 'lunch', mostrando una chiara crescita nel numero di piatti per il pranzo.\n"
    f"- Nella categoria 'smoothie', ci sono state {chef_counts_per_year_category.loc[2023, 'smoothie']} ricette, segnalando un'interesse continuo per le bevande salutari.\n"
    f"- Inoltre, ha creato {chef_counts_per_year_category.loc[2023, 'snack']} ricette di 'snack' e {chef_counts_per_year_category.loc[2023, 'vegan']} di 'vegan'.\n"

    f"Questa evoluzione nella produzione di ricette dello chef con id {most_frequent_chef} sottolinea non solo la sua versatilità, ma anche il crescente interesse della nostra comunità per una varietà di stili culinari.\n"
    
    "Osservando i dati nel tempo, è evidente che la cucina sta diventando sempre più diversificata. "
    "L'incremento significativo nella categoria 'ethnic' e l'attenzione crescente per 'lunch' e 'dinner' mostrano che gli utenti della nostra piattaforma non solo amano cucinare, "
    "ma sono anche pronti ad esplorare sapori e ricette da tutto il mondo. "
    "Questo trend non solo celebra il talento dello chef più attivo, ma rappresenta anche un viaggio culinario condiviso da tutta la comunità."
)

print(story)                                            # Stampa dello Storytelling
print("-" * 40)                                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il numero di ricette mensili per ogni anno
activity_trend = df.groupby(df['cooking_date'].dt.to_period('M')).size()                # Raggruppa i dati nella colonna 'cooking_date' per mese e conta il numero di ricette postate ogni mese
activity_trend_df = activity_trend.reset_index()                                        # Crea un DataFrame a partire dal conteggio delle ricette mensili
activity_trend_df.columns = ['cooking_date', 'recipe_count']                            # Le colonne del DataFrame vengono rinominate per una maggiore chiarezza
activity_trend_df['year'] = activity_trend_df['cooking_date'].dt.year.astype(int)       # Viene aggiunta una colonna al DataFrame che estrae l'anno dalla data di cottura e lo converte in un intero
years = activity_trend_df['year'].unique()                                              # Viene estratto un array di anni unici presenti nel DataFrame
colors = mpl.colormaps['tab10']                                                         # Viene creata una mappa di colori utilizzando la colormap 'tab10' per distinguere gli anni
bar_colors = [colors(years.tolist().index(year)) for year in activity_trend_df['year']] # I colori vengono mappati in base all'anno, creando una lista di colori per ogni anno presente nel DataFrame

plt.figure(figsize=(12, 6))                                                                                 # La dimensione del grafico viene impostata (Larghezza e Altezza)
plt.bar(activity_trend_df['cooking_date'].astype(str), activity_trend_df['recipe_count'], color=bar_colors) # Viene creato un grafico a barre, utilizzando la data come asse X e il conteggio delle ricette come asse Y, applicando i colori
plt.title('Trend di Attività Mensile per Anno', fontweight='bold')                                          # Viene aggiunto un titolo al grafico
plt.ylabel('Numero di Ricette', fontweight='bold')                                                          # Etichetta l'asse Y del grafico con il numero di ricette
plt.xlabel('Mese', fontweight='bold')                                                                       # Etichetta l'asse X del grafico con i mesi

for x, y in zip(range(len(activity_trend_df)), activity_trend_df['recipe_count']):                          # Viene aggiunta un'etichetta ai punti dati del grafico, posizionando il valore della ricetta sopra ogni barra
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.xticks(rotation=90)         # Le etichette dell'asse X vengono ruotate di 90 gradi per migliorare la leggibilità
plt.grid(axis='y')              # Viene aggiunta una griglia all'asse Y del grafico per migliorare la leggibilità
plt.show()                      # Il grafico finale viene mostrato

# Storytelling che mostra il numero di ricette mensili per ogni anno
story = (

    "Nel mondo della piattaforma culinaria, il numero di ricette postate mensilmente ha subito una crescita notevole dal 2021 al 2023.\n"
    "Nel 2021, l'anno è iniziato con un'attività modesta. Già a gennaio sono state postate solo 6 ricette, con un calo a febbraio con appena 3 ricette.\n"
    "Tuttavia, l'attività è ripresa in estate, raggiungendo il picco ad agosto con 17 ricette, per poi stabilizzarsi tra 9 e 12 ricette al mese fino a dicembre.\n\n"
    
    "Il 2022 ha segnato un punto di svolta. L'anno è iniziato con una forte crescita: già a gennaio sono state postate 23 ricette, mantenendosi costante fino a marzo.\n"
    "Nonostante una lieve flessione durante i mesi estivi (con un minimo di 18 ricette a giugno e luglio), l'attività è ripresa nell'ultimo trimestre del 2022, raggiungendo il massimo dell'anno a novembre con 31 ricette.\n\n"
    
    "Il 2023 è stato l'anno dell'esplosione di attività. Gennaio ha visto 50 ricette, un numero significativamente più alto rispetto agli anni precedenti.\n"
    "L'attività ha continuato a crescere, raggiungendo il picco massimo di 57 ricette ad aprile, e mantenendosi stabile e su livelli elevati per tutto l'anno.\n"
    "Il picco assoluto è stato registrato a settembre 2023, con 59 ricette. Anche negli ultimi mesi dell'anno, i numeri sono rimasti elevati, con 56 ricette a ottobre e 54 a novembre.\n\n"
    
    "In conclusione, la piattaforma ha vissuto una notevole evoluzione in questi tre anni. Il 2021 rappresenta l'anno di avvio, con numeri ancora in crescita.\n"
    "Il 2022 ha visto una stabilizzazione e un'accelerazione nell'attività, mentre il 2023 ha consolidato il successo della piattaforma con un numero costante e alto di ricette postate mensilmente.\n"
)

print(story)                                                # Stampa dello Storytelling
print("-" * 40)                                             # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Mostra il numero di partecipazioni a ciascuna challenge:
challenge_participation = df['challenge_id'].value_counts() # Conta il numero di partecipazioni a ogni 'challenge'.

print("Partecipazione alle challenge:")                     # Stampa "Partecipazione alle challenge"
print(challenge_participation.head())                       # Stampa i livelli delle ricette con il totale

# Storytelling che mostra il numero di partecipazioni a ciascuna challenge
story =(
        "Ho analizzato il numero di partecipazioni a ciascuna challenge:\n"
        "- **Challenge 3**: 270 partecipazioni\n"
        "- **Challenge 2**: 253 partecipazioni\n"
        "- **Challenge 1**: 248 partecipazioni\n"
        "- **Challenge 0**: 228 partecipazioni\n\n"
        "La **Challenge 3** si è dimostrata la più popolare, con ben 270 partecipazioni, seguita da vicino "
        "dalla **Challenge 2** con 253 partecipazioni. Anche le altre challenge hanno visto un buon numero di partecipazioni, "
        "dimostrando che gli utenti sono entusiasti di mettersi alla prova in cucina.\n\n"
        "In conclusione, la partecipazione alle challenge evidenzia un forte coinvolgimento della nostra comunità culinaria. "
        "Ogni partecipazione è un passo verso l'esplorazione di nuove ricette e la condivisione di esperienze. "
)

print(story)                                                # Stampa dello Storytelling
print("-" * 40)                                             # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Mostra i livelli delle ricette con il totale.
level = df['level'].value_counts()      # Conteggio delle ricette per ciascun livello di difficoltà ('level')

print("Livelli:")                       # Stampa "Livelli"
print(level.head())                     # Stampa i livelli delle ricette con il totale.

# Storytelling che mostra i livelli delle ricette con il totale.
story = (
    "Nel mondo della cucina su questa piattaforma, le ricette si distribuiscono su vari livelli di difficoltà, ma è interessante notare alcune tendenze particolari.\n"
    "Le ricette di livello **advanced**, destinate agli chef più esperti e competenti, sono state postate in maniera significativa: ben 450 ricette sono state catalogate come avanzate.\n"
    "Questo dimostra che c'è un'ampia partecipazione da parte di utenti che cercano di mettere alla prova le loro abilità culinarie più avanzate.\n\n"
    
    "D'altro canto, anche il livello **basic**, rivolto agli utenti meno esperti o a chi vuole realizzare ricette semplici e veloci, ha avuto una buona risposta.\n"
    "Sono state postate 348 ricette di livello base, il che indica una solida richiesta di contenuti più accessibili e facili da seguire.\n\n"
    
    "Questo equilibrio tra ricette avanzate e di base dimostra che la piattaforma riesce a soddisfare le esigenze di una vasta gamma di utenti, dai principianti agli esperti.\n"
    "La distribuzione di queste ricette offre a tutti la possibilità di migliorare le proprie competenze, indipendentemente dal livello di partenza.\n"
    "Inoltre, questa varietà di difficoltà arricchisce la comunità culinaria, offrendo sfide per gli chef esperti, ma anche soluzioni pratiche per chi è appena agli inizi.\n"
)

print(story)                            # Stampa dello Storytelling
print("-" * 40)                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra i dati per anno e paese
country_year_counts = df.groupby(['year', 'country']).size().reset_index(name='recipe_count')   # Raggruppa i dati per anno e paese ('country'), contando il numero di ricette
print(country_year_counts)                                                                      # Stampa i risultati del conteggio per paese(nazione) e anno

# Mostra una tabella pivot per i dati di ricette per paese e anno
pivot_table = country_year_counts.pivot(index='year', columns='country', values='recipe_count').fillna(0)   # Crea una tabella pivot con gli anni come indice, i paesi come colonne e il numero di ricette come valori e riempire i valori mancanti (NaN) con 0
ax = pivot_table.plot(kind='bar', figsize=(14, 8), stacked=False)                                           # Crea un grafico a barre (non sovrapposto) con i dati della tabella pivot, impostando la dimensione della figura

plt.title('Distribuzione delle Ricette per Paese e Anno', fontweight='bold')                                # Aggiunge un titolo al grafico con testo in grassetto
plt.ylabel('Numero di Ricette', fontweight='bold')                                                          # Aggiunge un'etichetta per l'asse Y (Numero di Ricette), con testo in grassetto
plt.xlabel('Anno', fontweight='bold')                                                                       # Aggiunge un'etichetta per l'asse X (Anno), con testo in grassetto
plt.legend(title='Paese', bbox_to_anchor=(1.05, 1), loc='upper left')                                       # Aggiunge una legenda con il titolo 'Paese' e posizionarla fuori dal grafico (a destra)

for container in ax.containers:                                                                             # Aggiunge etichette numeriche su ciascuna barra, con testo in grassetto e un leggero padding
    ax.bar_label(container, label_type='edge', fontsize=12, fontweight='bold', padding=3)

plt.xticks(rotation=45)                                                                                     # Ruota le etichette dell'asse X di 45 gradi per migliorare la leggibilità
plt.grid(axis='y')                                                                                          # Aggiunge una griglia orizzontale lungo l'asse Y
plt.tight_layout()                                                                                          # Migliora il layout del grafico per evitare sovrapposizioni tra elementi
plt.show()                                                                                                  # Mostra il grafico

# Storytelling che mostra i dati  di ricette per paese e anno
story = (
    "Nel corso di tre anni, la piattaforma ha assistito a un aumento impressionante del numero di ricette postate, con un coinvolgimento crescente da parte di tre nazioni chiave: Francia, Italia e Regno Unito.\n\n"
    
    "Nel 2021, l'attività culinaria era ancora in una fase iniziale, con numeri relativamente modesti. La Francia ha contribuito con 26 ricette, mentre l'Italia ha registrato 39 ricette, evidenziando una partecipazione un po' più forte.\n"
    "Tuttavia, il Regno Unito ha superato entrambi, diventando il paese con il maggior numero di ricette postate nel 2021, con 43 ricette. Questo dimostra una certa vivacità culinaria in UK già dal primo anno.\n\n"
    
    "Nel 2022, si è osservato un chiaro segnale di crescita. La Francia ha quasi triplicato il numero delle ricette postate, raggiungendo 62 ricette.\n"
    "L'Italia ha mostrato una crescita ancora più marcata, passando a 120 ricette, diventando il paese con il maggior aumento rispetto all'anno precedente.\n"
    "Anche il Regno Unito ha visto una crescita significativa, con 86 ricette pubblicate, rafforzando la sua presenza attiva sulla piattaforma.\n\n"
    
    "Il 2023 ha segnato un vero e proprio boom nell'attività culinaria. La Francia ha continuato la sua crescita costante, con 132 ricette pubblicate, mentre l'Italia ha fatto un balzo spettacolare, registrando un totale di 282 ricette, consolidandosi come il paese con il maggior contributo.\n"
    "Nel frattempo, il Regno Unito ha anche avuto un notevole incremento, arrivando a 209 ricette. Questo segnala un forte coinvolgimento internazionale, con l'Italia che ha dominato il 2023 e la Francia e il Regno Unito che seguono da vicino.\n\n"
    
    "Questa crescita negli ultimi anni non solo riflette il crescente interesse degli utenti verso la piattaforma, ma mostra anche come la comunità internazionale culinaria stia diventando sempre più attiva.\n"
    "La leadership dell'Italia nel 2023, con il maggior numero di ricette, è un segnale del suo crescente peso nella comunità, ma è interessante vedere come anche Francia e Regno Unito abbiano consolidato la loro posizione.\n"
)

print(story)                                                 # Stampa dello Storytelling
print("-" * 40)                                              # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Mostra la valutazione media per ciascuna categoria
average_ratings_by_category = df.groupby('category')['stars'].mean().round(2)                   # Calcola la valutazione media ('stars') per ciascuna categoria, arrotondata a due cifre decimali
print(average_ratings_by_category)                                                              # Stampa la valutazione media per ciascuna categoria

plt.figure(figsize=(10, 6))                                                                     # Crea una figura con dimensioni 10x6 pollici
bars = average_ratings_by_category.plot(kind='bar',                                             # Genera un grafico a barre per le valutazioni medie per categoria
                                        color=colors(range(len(average_ratings_by_category))),  # 'colors' è usato per assegnare un colore diverso a ciascuna barra
                                        title='Valutazioni Medie per Categoria',                # Titolo del grafico
                                        ylabel='Stelle Medie',                                  # Etichetta Asse Y
                                        xlabel='Categoria')                                     # Etichetta Asse X

plt.title('Valutazioni Medie per Categoria', fontweight='bold')                                 # Aggiunge un titolo al grafico con testo in grassetto
plt.ylabel('Stelle Medie', fontweight='bold')                                                   # Aggiunge un'etichetta per l'asse Y (Stelle Medie) con testo in grassetto
plt.xlabel('Categoria', fontweight='bold')                                                      # Aggiunge un'etichetta per l'asse X (Categoria) con testo in grassetto
etichetta_float()                                                                               # La funzione aggiunge etichette per ciascuna barra nel grafico con numeri di tipo "float"
plt.xticks(rotation=45)                                                                         # Ruota le etichette dell'asse X di 45 gradi per migliorare la leggibilità
plt.grid(axis='y')                                                                              # Aggiunge una griglia orizzontale sull'asse Y
plt.tight_layout()                                                                              # Migliora il layout per evitare sovrapposizioni tra gli elementi grafici
plt.show()                                                                                      # Mostra il grafico generato

# Storytelling che mostra la valutazione media per ciascuna categoria
story = (
    "L'analisi delle valutazioni medie per le diverse categorie di cibo rivela alcuni trend interessanti nelle preferenze alimentari.\n\n"
    "Le categorie con le valutazioni più alte sono 'Smoothie' e 'Vegan', con punteggi rispettivamente di 3.31 e 3.27. Questo suggerisce un'elevata preferenza per opzioni salutari e a base vegetale tra i consumatori.\n\n"
    "D'altra parte, la categoria 'Dinner' ha la valutazione media più bassa, con un punteggio di 2.96. Ciò potrebbe indicare un margine di miglioramento per i piatti consumati durante la cena.\n\n"
    "Le altre categorie, come 'Lunch' e 'Ethnic', presentano valutazioni medie rispettivamente di 3.25 e 3.12, dimostrando una buona accoglienza per pranzi leggeri o cucine internazionali.\n\n"
    "Infine, le categorie 'Breakfast' e 'Snack', con valutazioni di circa 3.0, riflettono un gradimento moderato. Questo evidenzia un equilibrio tra preferenze più classiche e nuove tendenze alimentari.\n\n"
    "In sintesi, l'analisi mette in luce una forte inclinazione verso cibi salutari, con un particolare interesse per smoothie e opzioni vegane, mentre i pasti serali sembrano avere un potenziale di miglioramento."
)

print(story)                                                          # Stampa dello Storytelling
print("-" * 40)                                                       # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra la valutazione media ('stars') per livello di difficoltà ('level')
average_ratings_by_level = df.groupby('level')['stars'].mean().round(2)         # Calcola la valutazione media ('stars') per ciascun livello di difficoltà ('level'), arrotondando a due cifre decimali
print(average_ratings_by_level)                                                 # Stampa le valutazioni medie per ciascun livello di difficoltà

colors = plt.colormaps['tab10'](range(len(average_ratings_by_level)))           # Crea una lista di colori basata sulla mappa dei colori 'tab10' di matplotlib e il numero di colori è determinato dal numero di livelli di difficoltà
plt.figure(figsize=(10, 6))                                                     # Crea una figura con dimensioni 10x6 pollici per il grafico

bars = average_ratings_by_level.plot(kind='bar',                                # Genera un grafico a barre con i colori assegnati a ciascun livello di difficoltà
                                     color=colors,                              # 'colors' è usato per assegnare un colore diverso a ciascuna barra
                                     title='Valutazioni Medie per Difficoltà',  # Titolo del grafico
                                     ylabel='Stelle Medie',                     # Etichetta Asse Y
                                     xlabel='Livello di Difficoltà')            # Etichetta Asse X


plt.title('Valutazioni Medie per Difficoltà', fontweight='bold')                # Aggiunge un titolo al grafico con testo in grassetto
plt.ylabel('Stelle Medie', fontweight='bold')                                   # Aggiunge un'etichetta per l'asse Y (Stelle Medie) con testo in grassetto
plt.xlabel('Livello di Difficoltà', fontweight='bold')                          # Aggiunge un'etichetta per l'asse X (Livello di Difficoltà) con testo in grassetto
etichetta_float()                                                               # La funzione aggiunge etichette per ciascuna barra nel grafico con numeri di tipo "float"
plt.xticks(rotation=45)                                                         # Ruota le etichette dell'asse X di 45 gradi per migliorarne la leggibilità
plt.grid(axis='y')                                                              # Aggiunge una griglia orizzontale lungo l'asse Y per aiutare a visualizzare meglio le altezze delle barre
plt.tight_layout()                                                              # Ottimizza il layout del grafico per evitare sovrapposizioni e migliorare la visualizzazione degli elementi
plt.show()                                                                      # Mostra il grafico generato

# Storytelling che mostra la valutazione media ('stars') per livello di difficoltà ('level')
story = (
    "L'analisi delle valutazioni medie suddivise per livello di difficoltà mette in evidenza alcune differenze nelle preferenze degli utenti.\n\n"
    "I piatti di livello 'Intermediate' ottengono la valutazione media più alta, con un punteggio di 3.16. Questo suggerisce che i consumatori apprezzano particolarmente le ricette di complessità intermedia, probabilmente perché offrono un equilibrio ideale tra sfida e accessibilità.\n\n"
    "Le ricette di livello 'Advanced' seguono da vicino, con una valutazione media di 3.13. Nonostante la maggiore difficoltà, molti utenti sembrano gradire le sfide culinarie più complesse.\n\n"
    "Infine, le ricette di livello 'Basic' ottengono una valutazione media di 3.07, leggermente inferiore rispetto agli altri livelli. Questo potrebbe indicare che le ricette più semplici, sebbene apprezzate, non suscitano lo stesso entusiasmo delle alternative più elaborate.\n\n"
    "In sintesi, i risultati suggeriscono che gli utenti tendono a preferire ricette di complessità media o avanzata, riconoscendone il valore sia in termini di gusto che di sfida culinaria."
)

print(story)                                                # Stampa dello Storytelling
print("-" * 40)                                             # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra per categoria e per nazioni quali ricette hanno  <= 2 stelle
low_rated_recipes = df[df['stars'] <= 2]                                                    # Filtra le ricette con valutazioni basse (<= 2 stelle)
low_rated_per_category_country = low_rated_recipes.groupby(['category', 'country']).size()  # Conta il numero di ricette con valutazioni basse per categoria e paese
print(low_rated_per_category_country)                                                       # Stampa i risultati

# Storytelling che mostra  per categoria e per nazioni quali ricette hanno  <= 2 stelle
story = (
    "L'analisi delle ricette con valutazioni basse, ossia pari o inferiori a 2 stelle, offre uno spaccato interessante delle preferenze culinarie per categoria e paese.\n\n"
    "Per la categoria 'Breakfast', vediamo che le ricette francesi, italiane e britanniche ottengono un numero abbastanza equilibrato di valutazioni basse, rispettivamente con 19, 28 e 21 ricette. Ciò suggerisce che, in questa categoria, c'è un margine di miglioramento per aumentare la soddisfazione in tutti e tre i paesi.\n\n"
    "La situazione è leggermente diversa per 'Dinner', dove le ricette italiane sembrano riscuotere minori consensi rispetto a quelle francesi e britanniche, con 17 ricette a bassa valutazione in Italia, contro 9 in Francia e 19 nel Regno Unito. Questo indica una possibile area di miglioramento per le cene in Italia.\n\n"
    "La categoria 'Ethnic' mostra un quadro in cui l'Italia (58 ricette) ha molte più valutazioni basse rispetto alla Francia (26) e al Regno Unito (43). Questo potrebbe indicare una minore accettazione delle ricette etniche in Italia o una differente aspettativa nei confronti di queste proposte.\n\n"
    "'Lunch' riflette una tendenza simile, con l'Italia che guida con 23 ricette a bassa valutazione, seguita dal Regno Unito (14) e dalla Francia (10). Questo suggerisce che le proposte per il pranzo potrebbero necessitare di un'attenzione particolare, soprattutto in Italia.\n\n"
    "Per quanto riguarda i 'Smoothie', notiamo un numero relativamente basso di valutazioni basse, con 8 ricette in Francia, 9 in Italia e 5 nel Regno Unito, evidenziando un maggiore apprezzamento complessivo per questa categoria.\n\n"
    "La categoria 'Snack' mostra invece una distribuzione più uniforme, con Francia, Italia e Regno Unito che contano ciascuno circa 10-13 ricette con valutazioni basse, suggerendo una risposta generalmente tiepida verso le proposte snack.\n\n"
    "Infine, nella categoria 'Vegan', vediamo un trend simile con l'Italia che registra 13 ricette a bassa valutazione, seguita dal Regno Unito con 12 e dalla Francia con 5. Questo potrebbe indicare una certa resistenza verso i piatti vegani in Italia e nel Regno Unito rispetto alla Francia.\n\n"
    "In sintesi, questa analisi suggerisce che esistono delle differenze culturali nelle preferenze alimentari, con alcune categorie che richiedono maggiori miglioramenti, soprattutto in Italia per le ricette etniche, pranzi e vegane. Migliorare queste aree potrebbe portare a un aumento della soddisfazione dei consumatori."
)

print(story)                                                # Stampa dello Storytelling
print("-" * 40)                                             # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il valore e la % delle piattaforme utilizzate per visulizzare le ricette
platform_distribution = df['platform'].value_counts()   # Mostra la distribuzione delle piattaforme utilizzate ('platform')
print(platform_distribution)                            # Stampa la distribuzione delle piattaforme

# Creare una nuova figura per il grafico a torta, con dimensioni 8x8 pollici
plt.figure(figsize=(8, 8))
platform_distribution.plot(kind='pie', autopct='%1.2f%%', textprops={'fontweight': 'bold'}) # Crea un grafico a torta per visualizzare la distribuzione delle piattaforme; 'platform_distribution' è una serie contenente i dati sulle piattaforme; 'autopct' serve per mostrare le percentuali con due cifre decimali ('%1.2f%%');'textprops' specifica lo stile del testo per le etichette (grassetto)
plt.title('Distribuzione delle Piattaforme', fontweight='bold')                             # Aggiunge il titolo nel grafico a torta, con testo in grassetto
plt.ylabel('')                                                                              # Rimuove l'etichetta predefinita dell'asse Y (per evitare che appaia nel grafico)
plt.show()                                                                                  # Mostra il grafico a torta

# Storytelling che mostra il valore e la % delle piattaforme utilizzate per visulizzare le ricette
story = (
    "L'analisi della distribuzione delle piattaforme utilizzate per accedere alle ricette rivela alcuni interessanti insight sul comportamento degli utenti.\n\n"
    "La televisione ('TV') emerge come la piattaforma più popolare, rappresentando una parte significativa degli accessi, con il 45.05% del totale. Questo suggerisce che molti utenti preferiscono consultare le ricette comodamente dal proprio salotto, sfruttando schermi più grandi e un'interfaccia visiva che potrebbe risultare più comoda e immersiva per seguire le istruzioni culinarie.\n\n"
    "La seconda piattaforma più utilizzata è il 'PC', con una quota del 30.93%. L'uso del PC riflette probabilmente la preferenza per una maggiore flessibilità e controllo nell'accesso ai contenuti, in particolare per chi preferisce la stabilità di un computer durante la ricerca e la preparazione delle ricette.\n\n"
    "Infine, il 'Mobile' si attesta al 24.02%. Nonostante la sua diffusione e la comodità d'uso, gli smartphone sembrano essere meno popolari per questo tipo di attività rispetto alla TV e al PC. Questo potrebbe essere dovuto alla dimensione ridotta dello schermo, che rende meno pratico seguire istruzioni dettagliate o visualizzare ingredienti e passaggi.\n\n"
    "In sintesi, l'analisi mostra che, sebbene tutte e tre le piattaforme siano utilizzate, la televisione rimane il dispositivo preferito per consultare ricette, seguita dal PC, mentre il mobile è meno scelto per questa attività specifica."
)

print(story)                                            # Stampa dello Storytelling
print("-" * 40)                                         # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il numero di ricette per paese (nazione)
activity_by_country = df['country'].value_counts()                                          # Conta il numero di ricette postate per paese ('country')
print(activity_by_country)                                                                  # Stampa il conteggio delle ricette per paese
colors = matplotlib.colormaps.get_cmap('tab20')                                             # Ottiene la mappa dei colori 'tab20' da matplotlib, che fornisce una palette con 20 colori distinti
plt.figure(figsize=(10, 6))                                                                 # Crea una nuova figura per il grafico a barre, con dimensioni 10x6 pollici

# Crea il grafico a barre che visualizza il conteggio delle ricette per per paese; 'activity_by_country' è un DataFrame o Serie che contiene il numero di ricette per paese; i colori delle barre vengono assegnati dinamicamente dalla palette 'tab20' per ciascun paese
bars = activity_by_country.plot(kind='bar', 
                                color=[colors(i) for i in range(len(activity_by_country))],  # Assegna un colore per ogni barra
                                title='Numero di Ricette per Paese/Nazione',                 # Titolo del grafico
                                ylabel='Numero di Ricette',                                  # Etichetta per l'asse Y
                                xlabel='Paese/Nazione')                                      # Etichetta per l'asse X

plt.title('Numero di Ricette per Paese/Nazione', fontweight='bold')                         # Aggiunge un titolo al grafico con testo in grassetto
plt.ylabel('Numero di Ricette', fontweight='bold')                                          # Aggiunge un'etichetta per l'asse Y (Numero di Ricette), con testo in grassetto
plt.xlabel('Paese/Nazione', fontweight='bold')                                              # Aggiunge un'etichetta per l'asse X (per Paese/Nazione), con testo in grassetto
etichetta_int()                                                                             # La funzione aggiunge etichette per ciascuna barra nel grafico con numeri interi
plt.xticks(rotation=45)                                                                     # Ruota le etichette dell'asse X di 45 gradi per migliorarne la leggibilità
plt.tight_layout()                                                                          # Ottimizza il layout per evitare sovrapposizioni tra gli elementi grafici
plt.show()                                                                                  # Mostra il grafico

# Storytelling che mostra il numero di ricette per paese (nazione)
story = (
    "L'analisi dell'attività di pubblicazione delle ricette per paese rivela interessanti differenze nella partecipazione tra Italia, Regno Unito e Francia.\n\n"
    "L'Italia emerge come il paese più attivo, con un totale di 441 ricette pubblicate. Questo dato riflette la forte tradizione culinaria italiana e l'interesse costante del pubblico per la condivisione di ricette, che spaziano probabilmente dalla cucina tradizionale alle nuove tendenze alimentari.\n\n"
    "Il Regno Unito segue con 338 ricette pubblicate. Anche se leggermente meno attivo rispetto all'Italia, il Regno Unito dimostra un notevole interesse per la creazione e la condivisione di contenuti culinari, forse con una maggiore enfasi su piatti internazionali e fusion.\n\n"
    "La Francia si posiziona al terzo posto con 220 ricette. Nonostante la ricca tradizione gastronomica francese, il numero inferiore di ricette rispetto all'Italia e al Regno Unito potrebbe riflettere una preferenza per la conservazione di tecniche culinarie più tradizionali, con meno attenzione verso la condivisione digitale.\n\n"
    "In conclusione, l'Italia domina la scena in termini di pubblicazione di ricette, seguita dal Regno Unito e dalla Francia. Questa tendenza potrebbe indicare l'importanza della cultura culinaria in ciascun paese e il loro approccio alla condivisione digitale del sapere gastronomico."
)

print(story)                                                        # Stampa dello Storytelling
print("-" * 40)                                                     # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Mostra il numero di ricette per ogni singolo mese
df['subscription_date'] = pd.to_datetime(df['subscription_date'])                               # Conversione della colonna 'subscription_date' in formato datetime
activity_by_subscription_date = df.groupby(df['subscription_date'].dt.to_period('M')).size()    # Conta il numero di ricette postate rispetto alla data di iscrizione
print(activity_by_subscription_date)                                                            # Stampa il conteggio delle ricette rispetto alla data di iscrizione

plt.figure(figsize=(10, 6))                                                                     # Crea una nuova figura per il grafico a linee, con dimensioni 10x6 pollici
# Crea un grafico a linee per visualizzare la relazione tra la data di iscrizione degli utenti e il numero di ricette postate; 'activity_by_subscription_date' è DataFrame o Serie che contiene il numero di ricette per ogni data di iscrizione
activity_by_subscription_date.plot(kind='line', 
                                   title='Attività Utenti per Data di Iscrizione',  # Titolo del grafico
                                   ylabel='Numero di Ricette',                      # Etichetta per l'asse Y
                                   xlabel='Data di Iscrizione')                     # Etichetta per l'asse X

plt.xticks(rotation=45)     # Ruota le etichette dell'asse X di 45 gradi per migliorare la leggibilità
plt.show()                  # Mostra il grafico a linee

# Storytelling che mostra il numero di ricette per ogni singolo mese
story = (
    "L'analisi dell'attività di pubblicazione delle ricette in relazione alla data di iscrizione degli utenti mostra trend interessanti che si sviluppano nel corso di tre anni.\n\n"
    "All'inizio del 2020, vediamo una crescita costante nel numero di ricette postate, con un picco di 36 ricette sia a marzo che a gennaio 2021. Questo periodo coincide con l'inizio della pandemia, un momento in cui molte persone hanno trascorso più tempo in casa e si sono dedicate maggiormente alla cucina.\n\n"
    "Nel corso del 2021, l'attività raggiunge un altro picco a ottobre, con 48 ricette postate, probabilmente dovuto all'adattamento alla nuova normalità e a un rinnovato interesse per la condivisione di ricette. Anche i mesi estivi del 2021, come maggio e luglio, registrano una forte attività, con 47 e 41 ricette rispettivamente.\n\n"
    "Tuttavia, l'inizio del 2022 vede un leggero calo dell'attività, con numeri più moderati durante i primi mesi dell'anno. Nonostante ciò, ci sono alcuni momenti di ripresa, come a maggio e giugno, con 44 e 36 ricette pubblicate rispettivamente. Questo potrebbe indicare che, anche se l'attività complessiva ha rallentato, l'interesse per la cucina e la condivisione delle ricette non è scomparso del tutto.\n\n"
    "Nel complesso, l'analisi rivela che l'attività di pubblicazione delle ricette è strettamente legata agli eventi globali e ai cambiamenti stagionali, con i picchi più alti durante i periodi di maggiore permanenza a casa, e una leggera fluttuazione durante il 2022."
)

print(story)                                                        # Stampa dello Storytelling
print("-" * 40)                                                     # Stampa una linea orizzontale di 40 caratteri

#-----------------------------------------------------------------------------------------------------------------------------------------------------

################################################################___________CONCLUSIONE______________###################################################################################################################

'''
Negli ultimi tre anni, la nostra piattaforma culinaria ha vissuto una trasformazione significativa, affermandosi come uno spazio privilegiato per gli appassionati di cucina e per chef di talento provenienti 
da tutto il mondo. La straordinaria crescita nel numero di ricette, nella varietà delle categorie e nella partecipazione degli utenti è una testimonianza di come la gastronomia stia diventando sempre più centrale 
nella vita quotidiana e nella cultura globale.
Il percorso iniziato nel 2021 ha visto un modesto ma promettente debutto, con appena 108 ricette pubblicate. Tuttavia, nel corso del 2022 e, in particolare, nel 2023, abbiamo assistito a una vera e propria 
esplosione di creatività culinaria: il numero di ricette è salito rispettivamente a 268 e poi a ben 623, consolidando la piattaforma come una delle più vivaci nel panorama digitale. Questo incremento non è 
solo quantitativo ma anche qualitativo, poiché la varietà delle categorie esplorate dagli utenti si è ampliata notevolmente, riflettendo i cambiamenti nelle preferenze alimentari e negli stili di vita.
Tra i dati più interessanti emerge l'ascesa della colazione come uno dei momenti centrali della giornata per gli utenti. Dal 2021 al 2023, il numero di ricette nella categoria "breakfast" è passato da 16 a 101, 
evidenziando un cambiamento significativo nelle abitudini alimentari, con un'attenzione maggiore alla qualità e alla varietà del primo pasto della giornata. Anche il pranzo e la cena hanno visto una crescita 
consistente, con un numero crescente di utenti che sperimentano nuove ricette e si avvicinano alla cucina in modo più consapevole e creativo. La categoria "lunch", ad esempio, ha visto un aumento da 9 a 106 
ricette in tre anni, segno che il pranzo sta diventando sempre più un momento di espressione gastronomica, non solo un pasto veloce.
Un aspetto particolarmente rilevante è l'interesse esplosivo per la cucina internazionale, riflesso nella categoria "ethnic", che ha visto un incremento straordinario da 47 ricette nel 2021 a 214 nel 2023. 
Questo trend non solo dimostra una crescente curiosità verso le tradizioni culinarie globali, ma riflette anche un'apertura culturale e un desiderio di esplorare sapori e tecniche da tutto il mondo. La cucina 
etnica, infatti, rappresenta una parte fondamentale della nostra piattaforma, contribuendo a creare una comunità globale e multiculturale che celebra la diversità attraverso il cibo.
Parallelamente, abbiamo assistito a un'evoluzione nell'interesse per l'alimentazione sana e sostenibile. Le categorie "smoothie" e "vegan" sono cresciute notevolmente, con un aumento continuo di ricette anno 
dopo anno. Nel 2023, la categoria "smoothie" ha visto la pubblicazione di 40 ricette, mentre la categoria "vegan" ha raggiunto le 48 ricette, segnalando un chiaro cambiamento nelle preferenze degli utenti verso 
opzioni più salutari e basate su alimenti vegetali. Questo interesse per l'alimentazione sostenibile è un riflesso di un movimento più ampio che abbraccia non solo una cucina gustosa, ma anche eticamente 
consapevole e rispettosa dell'ambiente.
La nostra piattaforma non è solo uno spazio per la sperimentazione culinaria, ma anche per lo sviluppo delle competenze degli utenti. Le ricette sono distribuite su vari livelli di difficoltà, con una forte 
presenza di ricette "advanced", che testimoniano la voglia degli utenti di mettersi alla prova e migliorare continuamente le proprie abilità in cucina. Nel 2023, ben 450 ricette sono state classificate come 
"advanced", dimostrando che molti utenti cercano sfide culinarie più complesse. Al tempo stesso, con 348 ricette "basic", la piattaforma riesce anche a soddisfare le esigenze di coloro che preferiscono soluzioni 
più semplici e veloci, rendendo l'esperienza accessibile a una vasta gamma di utenti.
Un altro punto di forza della piattaforma è la varietà dei contributi provenienti da diverse regioni del mondo. L'Italia, il Regno Unito e la Francia sono stati i paesi più attivi, con una crescita impressionante 
di contributi. L'Italia, in particolare, ha visto una straordinaria espansione, passando da 39 ricette nel 2021 a 282 nel 2023, diventando così il paese con il maggior numero di ricette pubblicate. Anche la 
Francia e il Regno Unito hanno mostrato un forte impegno, con rispettivamente 132 e 209 ricette nel 2023. Questo riflette non solo la ricchezza delle tradizioni culinarie di questi paesi, ma anche un crescente 
entusiasmo per la condivisione di idee e ricette a livello internazionale.
Dal punto di vista delle valutazioni, le categorie "smoothie" e "vegan" hanno ottenuto i punteggi medi più alti, segnalando una forte preferenza per le opzioni salutari e a base vegetale. Questo suggerisce 
che, oltre alla crescente popolarità di queste categorie, vi è anche una maggiore soddisfazione tra gli utenti che le scelgono. Al contrario, la categoria "dinner" ha registrato la valutazione media più bassa, 
con un punteggio di 2.96, suggerendo che esiste ancora spazio per migliorare l'offerta di piatti serali sulla piattaforma.
Le piattaforme utilizzate dagli utenti per accedere alle ricette offrono un ulteriore spunto di riflessione. La televisione si è rivelata la piattaforma preferita, con il 45% degli accessi totali, seguita dal 
PC con il 30.9% e dal mobile con il 24%. Questo suggerisce che, sebbene gli smartphone siano sempre più diffusi, per la consultazione di ricette gli utenti preferiscono dispositivi con schermi più grandi e 
interfacce visive più dettagliate, come la TV o il PC, probabilmente per una migliore fruizione delle istruzioni culinarie.
In conclusione, la nostra piattaforma ha dimostrato di essere molto più di un semplice archivio di ricette: è diventata un punto di incontro per appassionati di cucina di tutto il mondo, uno spazio di 
esplorazione culturale e di apprendimento continuo. La straordinaria crescita degli ultimi tre anni, in termini di partecipazione, varietà e qualità delle ricette, testimonia non solo il successo della 
piattaforma, ma anche l'evoluzione delle abitudini alimentari globali. La comunità che si è creata intorno a questa piattaforma è vivace, dinamica e desiderosa di sperimentare nuove tendenze e di condividere 
le proprie esperienze culinarie. Guardando al futuro, ci aspettiamo che questa crescita continui, con nuovi contributi, nuove idee e un ulteriore arricchimento del panorama gastronomico digitale.

'''
