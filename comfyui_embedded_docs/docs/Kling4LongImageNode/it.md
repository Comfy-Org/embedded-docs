# Kling 4.0 Long Image

Genera un'immagine verticale con Kling 4.0: il design completo di una pagina web oppure una pagina di dettaglio prodotto per e-commerce. Scegli la `skill` che corrisponde al layout desiderato e il nodo mostrerà gli input di quel layout.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `abilità` | Layout da generare. `"webpage"` progetta una pagina completa intorno a un'immagine di stile e a un soggetto opzionali; `"ecommerce"` crea una pagina di dettaglio prodotto a partire da foto del prodotto. | DYNAMIC_COMBO | Sì | `"webpage"`<br>`"ecommerce"` |

### Input di `webpage`

Questi input compaiono quando `skill` è impostato su `"webpage"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `style_image` | Riferimento opzionale per lo stile visivo e il layout. Riferirsi a essa come `@Image1`. | IMAGE | No | Immagine singola |
| `subject_image` | Soggetto opzionale da mantenere e intorno al quale progettare la pagina. Riferirsi a esso come `@Image2`. | IMAGE | No | Immagine singola |
| `prompt` | Descrizione opzionale della pagina. Riferirsi all'immagine di stile come `@Image1` e all'immagine del soggetto come `@Image2`, e specificare la lingua per il testo della pagina, ad esempio «Tutto il testo visibile deve essere solo in inglese». Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione dell'immagine di output. Predefinito: `"1K"`. | COMBO | Sì | `"1K"`<br>`"2K"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di `ecommerce`

Questi input compaiono quando `skill` è impostato su `"ecommerce"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `product_images` | Slot espandibili per le foto del prodotto (`image_1` ... `image_3`). Riferirsi a essi nel prompt come `@Image1`, `@Image2`, `@Image3`. | AUTOGROW | Sì | 1 a 3 immagini |
| `prompt` | Descrizione opzionale della pagina. Riferirsi alle immagini del prodotto come `@Image1`, `@Image2`, `@Image3`. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `length` | Lunghezza della pagina generata. Predefinito: `"medium"`. | COMBO | Sì | `"short"`<br>`"medium"`<br>`"long"` |
| `resolution` | Risoluzione dell'immagine di output. Predefinito: `"1K"`. | COMBO | Sì | `"1K"`<br>`"2K"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli e comportamento:**

* È possibile collegare al massimo 3 immagini del prodotto in `ecommerce`.
* Ogni immagine deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 2:5 e 5:2.
* Con `webpage`, un prompt che menziona `@Image1` o `@Image2` genera un errore quando quell'immagine non è collegata.
* Il prezzo di una chiamata dipende dalla skill, dalla risoluzione e, per `ecommerce`, dalla lunghezza della pagina.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine lunga generata, scaricata da Kling una volta completata l'attività. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4LongImageNode/it.md)

---
**Source fingerprint (SHA-256):** `f1e687bcc8334229c60b318118120b85ddd580d1b62f343164f9803b98a1f987`
