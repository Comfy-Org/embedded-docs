# Krea 2 Image

## Panoramica

Il nodo Krea 2 Image genera immagini utilizzando il modello AI Krea 2. Supporta due varianti del modello: Medium per illustrazioni espressive e Large per fotorealismo espressivo, con un'ulteriore opzione Medium Turbo per una generazione più rapida. Puoi facoltativamente includere un moodboard e fino a 10 riferimenti di stile per immagini per influenzare l'immagine generata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per l'immagine. | STRING | Sì | N/A |
| `model` | Krea 2 Medium è ideale per illustrazioni espressive; Krea 2 Large è ideale per fotorealismo espressivo. | DICT | Sì | Vedi sotto |
| `seed` | Seme casuale per la riproducibilità (predefinito: 0). | INT | Sì | da 0 a 2147483647 |

Il parametro `model` è un dizionario con i seguenti sotto-parametri:

| Sotto-parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------------|-------------|--------------|--------------|------------|
| `model` | Seleziona la variante del modello Krea 2. | STRING | Sì | `"krea 2 medium turbo"`<br>`"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | Le proporzioni per l'immagine generata. | STRING | Sì | N/A |
| `resolution` | La risoluzione per l'immagine generata. | STRING | Sì | N/A |
| `creativity` | Controlla il livello di creatività della generazione. | FLOAT | Sì | N/A |
| `moodboard_id` | L'UUID di un moodboard Krea per influenzare l'immagine. Deve essere un UUID valido. | STRING | No | N/A |
| `moodboard_strength` | La forza dell'influenza del moodboard (predefinito: 0.35). | FLOAT | No | N/A |
| `style_reference` | Un elenco di riferimenti di stile per immagini. Ogni riferimento deve avere un `url` (STRING) e `strength` (FLOAT). | LIST | No | da 0 a 10 elementi |

**Vincoli:**
- `moodboard_id` deve essere un UUID valido (ad es. `"123e4567-e89b-12d3-a456-426614174000"`). Copialo dal sito web Krea.
- `style_reference` accetta un massimo di 10 riferimenti di stile per immagini.
- Il `prompt` deve contenere almeno 1 carattere.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine generata come tensore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `645b404fe2c7653662803f1630125bdef912429c95d7b3a1268b0e0d7f533277`
