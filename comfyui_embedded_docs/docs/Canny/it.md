# Canny

Estrae tutte le linee di contorno dalle foto, come usare una penna per delineare una foto, tracciando i contorni e i confini dei dettagli degli oggetti.

## Principio di funzionamento

Immagina di essere un artista che deve usare una penna per delineare una foto. Il nodo Canny agisce come un assistente intelligente, aiutandoti a decidere dove tracciare le linee (bordi) e dove no.

Questo processo è come un lavoro di selezione:

- **Soglia alta** è il "criterio delle linee da tracciare obbligatoriamente": verranno tracciate solo linee di contorno molto evidenti e chiare, come i contorni del viso delle persone e le strutture degli edifici
- **Soglia bassa** è il "criterio delle linee da non tracciare assolutamente": i bordi troppo deboli verranno ignorati per evitare di disegnare rumore e linee prive di significato
- **Area intermedia**: i bordi compresi tra i due criteri verranno tracciati insieme se sono collegati alle "linee da tracciare obbligatoriamente", ma non verranno tracciati se sono isolati

L'output finale è un'immagine in bianco e nero, in cui le parti bianche sono le linee di contorno rilevate e le parti nere sono le aree senza bordi.

## Input

| Nome parametro | Descrizione funzione | Tipo di dati | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `image` | Foto originale da cui estrarre i bordi | IMAGE | Input | - | - |
| `low_threshold` | Soglia bassa, determina quanto debbano essere deboli i bordi da ignorare. Valori più bassi preservano più dettagli ma possono produrre rumore | FLOAT | Widget | 0.4 | 0.01-0.99 |
| `high_threshold` | Soglia alta, determina quanto debbano essere forti i bordi da preservare. Valori più alti mantengono solo le linee di contorno più evidenti | FLOAT | Widget | 0.8 | 0.01-0.99 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Immagine in bianco e nero dei bordi, le linee bianche sono i bordi rilevati, le aree nere sono le parti senza bordi | IMAGE |

## Confronto parametri

![Immagine originale](./asset/input.webp)

![Confronto parametri](./asset/compare.webp)

**Problemi comuni:**

- Bordi interrotti: prova ad abbassare la soglia alta
- Troppo rumore: alza la soglia bassa
- Dettagli importanti mancanti: abbassa la soglia bassa
- Bordi troppo grezzi: controlla la qualità e la risoluzione dell'immagine di input

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/it.md)
