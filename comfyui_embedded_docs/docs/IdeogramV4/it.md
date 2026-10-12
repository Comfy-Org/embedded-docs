# IdeogramV4

Genera immagini utilizzando il modello Ideogram 4.0 da un prompt testuale. Questo nodo invia la descrizione testuale all'API di Ideogram e restituisce l'immagine generata come tensore di output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione dell'immagine. | STRING | Sì | Nessuna restrizione |
| `resolution` | La risoluzione dell'immagine generata. Predefinito: "Auto" che consente al modello di scegliere la risoluzione migliore. | COMBO | Sì | `"Auto"`<br>`"2048x2048 (1:1)"`<br>`"1440x2880 (1:2)"`<br>`"2880x1440 (2:1)"`<br>`"1664x2496 (2:3)"`<br>`"2496x1664 (3:2)"`<br>`"1792x2240 (4:5)"`<br>`"2240x1792 (5:4)"`<br>`"1440x2560 (9:16)"`<br>`"2560x1440 (16:9)"`<br>`"1600x2560 (5:8)"`<br>`"2560x1600 (8:5)"`<br>`"1728x2304 (3:4)"`<br>`"2304x1728 (4:3)"`<br>`"1296x3168 (9:22)"`<br>`"3168x1296 (22:9)"`<br>`"1152x2944 (9:23)"`<br>`"2944x1152 (23:9)"`<br>`"1248x3328 (3:8)"`<br>`"3328x1248 (8:3)"`<br>`"1280x3072 (5:12)"`<br>`"3072x1280 (12:5)"` |
| `rendering_speed` | Controlla il compromesso tra velocità di generazione e qualità. Predefinito: "DEFAULT". | COMBO | Sì | `"DEFAULT"`<br>`"TURBO"`<br>`"QUALITY"` |
| `seed` | Seed per la generazione riproducibile. Predefinito: 0. | INT | Sì | Min: 0<br>Max: 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata come tensore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/it.md)

---
**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`
