# Rodin 3D Genera - Generazione da Schizzo

Questo nodo genera asset 3D utilizzando l'API Rodin. Prende in input immagini e le converte in modelli 3D tramite un servizio esterno. Il nodo gestisce l'intero processo, dalla creazione del task al download dei file finali del modello 3D.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `Images` | Immagini di input da convertire in modelli 3D. Puoi fornire da 1 a 5 immagini. | IMAGE | Sì | da 1 a 5 immagini |
| `Seed` | Valore del seed casuale per la generazione (predefinito: 0). Imposta a 0 per un seed casuale. | INT | No | da 0 a 65535 |

**Nota:** Il nodo richiede almeno 1 immagine e supporta un massimo di 5 immagini. Se non viene fornita alcuna immagine, il nodo genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `3D Model Path` | Percorso del file del modello 3D generato (solo per compatibilità con le versioni precedenti) | STRING |
| `GLB` | Il modello 3D generato in formato GLB | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/it.md)

---
**Source fingerprint (SHA-256):** `0b77ce871e267450af63f3e2fe0e36fe81ababc25cbb11498546ad8f487b65e5`
