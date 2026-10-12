# Scheduler Base

Il nodo `BasicScheduler` è progettato per calcolare una sequenza di valori sigma per modelli di diffusione in base allo scheduler, al modello e ai parametri di denoising forniti. Adatta dinamicamente il numero totale di passaggi in base al fattore denoise per mettere a punto il processo di diffusione, fornendo "ricette" precise per diverse fasi nei processi di campionamento avanzati che richiedono un controllo fine (come il campionamento multi-stadio).

## Input

| Parametro | Descrizione metaforica | Tipo di dati | Tipo di input | Predefinito | Intervallo | Scopo tecnico |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | **Tipo di tela**: materiali di tela diversi richiedono formule di vernice diverse | MODEL | Input | - | - | Oggetto del modello di diffusione, determina la base per il calcolo dei sigma |
| `scheduler` | **Tecnica di miscelazione**: scegli come cambia la concentrazione della vernice | COMBO[STRING] | Widget | - | 9 options | Algoritmo di scheduling, controlla la modalità di decadimento del rumore |
| `steps` | **Numero di miscelazioni**: differenza di precisione tra 20 miscelazioni e 50 miscelazioni | INT | Widget | 20 | 1-10000 | Passaggi di campionamento, influisce sulla qualità e sulla velocità di generazione |
| `denoise` | **Intensità di creazione**: livello di controllo dal fine-tuning alla ridipintura | FLOAT | Widget | 1.0 | 0.0-1.0 | Forza di denoising, supporta scenari di ridipintura parziale |

### Tipi di scheduler

Basato sul codice sorgente `comfy.samplers.SCHEDULER_NAMES`, supporta i seguenti 9 scheduler:

| Nome scheduler       | Caratteristiche      | Casi d'uso                    | Schema di decadimento del rumore |
| -------------------- | -------------------- | ---------------------------- | ---------------------------- |
| **normal**           | Lineare standard     | Scenari generali, bilanciato | Decadimento uniforme         |
| **karras**           | Transizione fluida   | Alta qualità, ricco di dettagli | Decadimento non lineare fluido |
| **exponential**      | Decadimento esponenziale | Generazione rapida, efficienza | Decadimento esponenziale rapido |
| **sgm_uniform**      | Uniforme SGM         | Ottimizzazione per modelli specifici | Decadimento ottimizzato per SGM |
| **simple**           | Scheduling semplice  | Test rapido, uso di base     | Decadimento semplificato     |
| **ddim_uniform**     | Uniforme DDIM        | Ottimizzazione del campionamento DDIM | Decadimento specifico per DDIM |
| **beta**             | Distribuzione beta   | Esigenze di distribuzione speciali | Decadimento con funzione beta |
| **linear_quadratic** | Lineare quadratico   | Ottimizzazione di scenari complessi | Decadimento con funzione quadratica |
| **kl_optimal**       | Ottimale KL          | Ottimizzazione teorica       | Decadimento ottimizzato per divergenza KL |

## Output

| Parametro | Descrizione metaforica | Tipo di dati | Tipo di output | Significato tecnico |
| --- | --- | --- | --- | --- |
| `sigmas` | **Grafico della ricetta della vernice**: elenco dettagliato delle concentrazioni di vernice da usare passo dopo passo | SIGMAS | Output | Sequenza dei livelli di rumore, guida il processo di denoising del modello di diffusione |

## Ruolo del nodo: Assistente dell'artista per la miscelazione dei colori

Immagina di essere un artista che crea un'immagine chiara da una miscela caotica di vernice (rumore). `BasicScheduler` agisce come il tuo **assistente professionale per la miscelazione dei colori**, il cui compito è preparare una serie di ricette precise per la concentrazione della vernice:

### Flusso di lavoro

- **Passaggio 1**: Usa vernice con concentrazione al 90% (livello di rumore alto)
- **Passaggio 2**: Usa vernice con concentrazione all'80%
- **Passaggio 3**: Usa vernice con concentrazione al 70%
- **...**
- **Passaggio finale**: Usa concentrazione allo 0% (tela pulita, senza rumore)

### Competenze speciali dell'assistente per i colori

**Diversi metodi di miscelazione (scheduler)**:

- **Metodo di miscelazione "karras"**: La concentrazione della vernice cambia in modo molto fluido, come la tecnica di gradiente di un artista professionista
- **Metodo di miscelazione "exponential"**: La concentrazione della vernice diminuisce rapidamente, adatto alla creazione rapida
- **Metodo di miscelazione "linear"**: La concentrazione della vernice diminuisce uniformemente, stabile e controllabile

**Controllo preciso (steps)**:

- **20 miscelazioni**: Pittura rapida, priorità all'efficienza
- **50 miscelazioni**: Pittura fine, priorità alla qualità

**Intensità di creazione (denoise)**:

- **1.0 = Creazione completamente nuova**: Inizia completamente da una tela bianca
- **0.5 = Trasformazione a metà**: Mantieni metà del dipinto originale, trasforma l'altra metà
- **0.2 = Regolazione fine**: Apporta solo lievi ritocchi al dipinto originale

### Collaborazione con altri nodi

`BasicScheduler` (Assistente per i colori) → Prepara la ricetta → `SamplerCustom` (Artista) → Pittura effettiva → Opera completata

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/it.md)
