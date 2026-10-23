# Bria Product Holding

Questo nodo mette un prodotto nelle mani di una persona con Bria. L'identità, la posa e lo sfondo della persona vengono mantenuti mentre la scena viene renderizzata nuovamente a circa 1 megapixel, quindi il risultato non è allineato a livello di pixel con la foto di input. Tutte le immagini del prodotto descrivono un unico prodotto da angolazioni o fasi diverse.

## Input

Il selettore `moderation` rivela un'opzione di moderazione aggiuntiva quando è impostato su `"true"`.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `person_image` | La foto della persona che tiene il prodotto. Il canale alpha viene rimosso prima del caricamento dell'immagine. | IMAGE | Sì | - |
| `product_images` | Da 1 a 3 immagini di un unico prodotto: il prodotto stesso, il suo imballaggio, un'altra angolazione o un articolo complementare. Un input in batch conta una volta per immagine e le aree trasparenti vengono trattate come bianche. | AUTOGROW | Sì | Da 1 a 3 immagini |
| `instruction` | Indicazione aggiuntiva facoltativa aggiunta all'istruzione integrata di Bria, ad esempio quale mano usare o verso quale direzione rivolgere l'etichetta. Predefinito: `""` (stringa vuota). | STRING | Sì | - |
| `aspect_ratio` | `"auto"` mantiene l'inquadratura della foto della persona a circa 1 megapixel. Un rapporto fisso restituisce da 0.6 a 1 megapixel, ad esempio 768x1024 per `"3:4"`. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Seed inviato a Bria con la richiesta. Predefinito: 42. | INT | Sì | Da 1 a 2147483647 |
| `moderation` | Impostazioni di moderazione. Quando impostato su `"true"`, il flag di moderazione riportato di seguito diventa disponibile. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione con "true"

Questo parametro compare solo quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine generata. Predefinito: `False`. | BOOLEAN | No | True / False |

**Vincoli:**

* `product_images` accetta un massimo di 3 immagini, conteggiate per immagine quando l'input è in batch.
* I pixel trasparenti nelle immagini del prodotto vengono composti su uno sfondo bianco prima del caricamento.
* Il canale alpha di `person_image` viene rimosso prima del caricamento.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | La foto modificata con il prodotto posizionato nelle mani della persona. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/it.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`
