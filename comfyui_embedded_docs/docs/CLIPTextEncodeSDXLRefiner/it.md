# ClipTextEncodeSdxlRefiner

Questo nodo è progettato specificamente per il modello SDXL Refiner per convertire i prompt testuali in informazioni di condizionamento, incorporando punteggi estetici e informazioni dimensionali per migliorare le condizioni dei task di generazione, migliorando così l'effetto di rifinitura finale. Agisce come un direttore artistico professionista: non solo trasmette la tua intenzione creativa, ma infonde anche nel lavoro precisi standard estetici e requisiti di specifica.

## Informazioni su SDXL Refiner

SDXL Refiner è un modello di rifinitura specializzato che si concentra sul miglioramento dei dettagli e della qualità delle immagini a partire dal modello base SDXL. Questo processo è come avere un ritoccatore d'arte:

1. Innanzitutto, riceve immagini preliminari o descrizioni testuali generate dal modello base
2. Poi, guida il processo di rifinitura attraverso punteggi estetici precisi e parametri dimensionali
3. Infine, si concentra sull'elaborazione dei dettagli ad alta frequenza delle immagini per migliorare la qualità complessiva

Refiner può essere utilizzato in due modi:

- Come passaggio di rifinitura autonomo per la post-elaborazione delle immagini generate dal modello base
- Come parte di un sistema esperto di integrazione, assumendo l'elaborazione durante la fase a basso rumore della generazione

## Input

| Nome parametro | Descrizione | Tipo di dati | Tipo di input | Valore predefinito | Intervallo di valori |
| --- | --- | --- | --- | --- | --- |
| `clip` | Istanza del modello CLIP utilizzata per la tokenizzazione e la codifica del testo, il componente principale per convertire il testo in un formato comprensibile al modello | CLIP | Obbligatorio | - | - |
| `ascore` | Controlla la qualità visiva e l'estetica delle immagini generate, in modo simile a impostare standard di qualità per un'opera d'arte:<br/>- Punteggi alti (7.5-8.5): persegue effetti più rifiniti e ricchi di dettagli<br/>- Punteggi medi (6.0-7.0): controllo della qualità bilanciato<br/>- Punteggi bassi (2.0-3.0): adatto per prompt negativi | FLOAT | Opzionale | 6.0 | 0.0-1000.0 |
| `width` | Specifica la larghezza dell'immagine di output (in pixel), deve essere un multiplo di 8. SDXL offre le prestazioni migliori quando il numero totale di pixel è vicino a 1024×1024 (circa 1M pixel) | INT | Obbligatorio | 1024 | 64-16384 |
| `height` | Specifica l'altezza dell'immagine di output (in pixel), deve essere un multiplo di 8. SDXL offre le prestazioni migliori quando il numero totale di pixel è vicino a 1024×1024 (circa 1M pixel) | INT | Obbligatorio | 1024 | 64-16384 |
| `text` | Descrizione del prompt testuale, supporta input multilinea e sintassi dei prompt dinamici. In Refiner, i prompt testuali dovrebbero concentrarsi maggiormente sulla descrizione della qualità visiva e delle caratteristiche di dettaglio desiderate | STRING | Obbligatorio | - | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | Output condizionale rifinito contenente la codifica integrata di semantica del testo, standard estetici e informazioni dimensionali, specificamente per guidare il modello SDXL Refiner in una precisa rifinitura dell'immagine | CONDITIONING |

## Note

1. Questo nodo è ottimizzato specificamente per il modello SDXL Refiner e differisce dai normali nodi CLIPTextEncode
2. Si consiglia un punteggio estetico di 7.5 come linea di base, che è l'impostazione standard utilizzata nell'addestramento di SDXL
3. Tutti i parametri dimensionali devono essere multipli di 8, ed è consigliato un numero totale di pixel vicino a 1024×1024 (circa 1M pixel)
4. Il modello Refiner si concentra sul miglioramento dei dettagli e della qualità delle immagini, quindi i prompt testuali dovrebbero enfatizzare gli effetti visivi desiderati piuttosto che il contenuto della scena
5. Nell'uso pratico, Refiner viene in genere utilizzato nelle fasi finali della generazione (approssimativamente l'ultimo 20% dei passi), concentrandosi sull'ottimizzazione dei dettagli

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/it.md)
