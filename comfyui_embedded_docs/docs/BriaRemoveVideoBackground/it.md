# BriaRemoveVideoBackground

Questo nodo rimuove lo sfondo da un video utilizzando il servizio Bria AI. Elabora il video di input e sostituisce lo sfondo originale con un colore solido a tua scelta. L'operazione viene eseguita tramite un'API esterna e il risultato viene restituito come nuovo file video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il file video di input da cui verrà rimosso lo sfondo. | VIDEO | Sì | N/A |
| `background_color` | Colore di sfondo per il video di output. | COMBO | Sì | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | Il parametro `seed` controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal valore del seed. (predefinito: 0) | INT | Sì | 0 a 2147483647 |

**Nota:** Il video di input deve avere una durata pari o inferiore a 60 secondi. I risultati non sono deterministici anche se il valore del seed rimane invariato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video elaborato con lo sfondo rimosso e sostituito dal colore selezionato, codificato come MP4 con codec H.264. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/it.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
