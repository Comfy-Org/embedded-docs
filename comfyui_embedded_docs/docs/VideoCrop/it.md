# Ritaglia video

Questo nodo ritaglia un video in una regione rettangolare definita in pixel, mantenendo solo l'area all'interno di quel rettangolo. Salva un'anteprima MP4 temporanea del risultato ritagliato e restituisce in output il video ritagliato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video di origine che verrà ritagliato. | VIDEO | Sì | Qualsiasi video |
| `crop` | Regione di ritaglio in pixel. Larghezza/altezza pari a zero mantiene il fotogramma intero. Il rettangolo di ritaglio fornisce i valori `x`, `y`, `width` e `height`, tutti con valore predefinito 0. | VIDEO_EDIT | Sì | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Tutti i valori predefiniti a 0 |

Nota: La regione di ritaglio è descritta in coordinate pixel. Quando larghezza e altezza sono 0, non viene applicato alcun ritaglio e il nodo restituisce in output l'intero video di input.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video ritagliato nella regione rettangolare selezionata. Quando larghezza e altezza del ritaglio sono 0, l'output è l'intero video di input. Il risultato ritagliato viene anche salvato come file MP4 temporaneo e mostrato come anteprima video. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/it.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
