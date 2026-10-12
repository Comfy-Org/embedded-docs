# PikaScenesV2_2

Il nodo PikaScenes v2.2 combina più immagini per creare un video che incorpora oggetti da tutte le immagini di input. Puoi caricare fino a cinque immagini diverse come ingredienti e generare un video di alta qualità che le fonde insieme senza interruzioni.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt_text` | Descrizione testuale di ciò che si desidera generare | STRING | Sì | - |
| `negative_prompt` | Descrizione testuale di ciò che si desidera evitare nella generazione | STRING | Sì | - |
| `seed` | Valore seed casuale per la generazione | INT | Sì | - |
| `resolution` | Risoluzione di output per il video | STRING | Sì | - |
| `duration` | Durata del video generato | INT | Sì | - |
| `ingredients_mode` | Modalità per combinare gli ingredienti (predefinita: "creative") | STRING | No | "creative"<br>"precise" |
| `aspect_ratio` | Rapporto d'aspetto (larghezza / altezza) (predefinito: 1.778) | FLOAT | No | 0.4 - 2.5 |
| `image_ingredient_1` | Immagine che verrà utilizzata come ingrediente per creare un video | IMAGE | No | - |
| `image_ingredient_2` | Immagine che verrà utilizzata come ingrediente per creare un video | IMAGE | No | - |
| `image_ingredient_3` | Immagine che verrà utilizzata come ingrediente per creare un video | IMAGE | No | - |
| `image_ingredient_4` | Immagine che verrà utilizzata come ingrediente per creare un video | IMAGE | No | - |
| `image_ingredient_5` | Immagine che verrà utilizzata come ingrediente per creare un video | IMAGE | No | - |

**Nota:** Puoi fornire fino a 5 immagini come ingredienti, ma è richiesta almeno un'immagine per generare un video. Il nodo utilizzerà tutte le immagini fornite per creare la composizione video finale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il video generato che combina tutte le immagini di input | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/it.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
