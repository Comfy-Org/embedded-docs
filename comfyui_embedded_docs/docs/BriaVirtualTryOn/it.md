# Bria Virtual Try-On

Questo nodo veste una persona con indumenti o accessori tramite Bria. L'identità, la posa e lo sfondo della persona vengono mantenuti mentre la scena viene renderizzata nuovamente a circa 1 megapixel, quindi il risultato non è allineato a livello di pixel con la foto di input. Ogni immagine di indumento sostituisce l'elemento corrispondente che la persona già indossa.

## Input

Il selettore `moderation` mostra un'opzione di moderazione aggiuntiva quando impostato su `"true"`.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `person_image` | La foto della persona che prova gli indumenti. Il canale alfa viene rimosso prima del caricamento dell'immagine. | IMAGE | Sì | - |
| `garment_images` | Da 1 a 3 indumenti o accessori indossati insieme, ognuno dei quali sostituisce l'elemento corrispondente indossato dalla persona. Un input in batch viene conteggiato una volta per immagine e le aree trasparenti vengono trattate come bianche. | AUTOGROW | Sì | 1 a 3 immagini |
| `instruction` | Indicazione aggiuntiva facoltativa aggiunta all'istruzione integrata di Bria, ad esempio quale indumento sovrapporre. Predefinito: `""` (stringa vuota). | STRING | Sì | - |
| `aspect_ratio` | `"auto"` mantiene l'inquadratura della foto della persona a circa 1 megapixel. Un rapporto fisso restituisce da 0,6 a 1 megapixel, ad esempio 768x1024 per `"3:4"`. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Seed inviato a Bria con la richiesta. Predefinito: 42. | INT | Sì | 1 a 2147483647 |
| `moderation` | Impostazioni di moderazione. Quando impostato su `"true"`, il flag di moderazione riportato di seguito diventa disponibile. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione "true"

Questo parametro compare solo quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine generata. Predefinito: `False`. | BOOLEAN | No | True / False |

**Vincoli:**

* `garment_images` accetta un massimo di 3 immagini, conteggiate per immagine quando l'input è in batch.
* I pixel trasparenti nelle immagini degli indumenti vengono sovrapposti a uno sfondo bianco prima del caricamento.
* Il canale alfa di `person_image` viene rimosso prima del caricamento.

## Output

| Nome dell'output | Descrizione | Tipo di dati |
|------------------|-------------|--------------|
| `image` | La foto modificata con la persona che indossa gli indumenti forniti. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVirtualTryOn/it.md)

---
**Source fingerprint (SHA-256):** `32f89c8685d8624bdef2c17ba5ba916b030d1dc88718b83c79aadb9a5fa378de`
