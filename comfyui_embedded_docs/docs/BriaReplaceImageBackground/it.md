# Bria Sostituisci sfondo immagine

Questo nodo sostituisce lo sfondo di un'immagine con uno nuovo generato da Bria. Il nuovo sfondo può essere descritto con un prompt testuale oppure guidato da immagini di riferimento. I pixel del soggetto vengono preservati mentre lo sfondo viene generato attorno ad essi.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input il cui sfondo verrà sostituito. | IMAGE | Sì | |
| `background` | Descrivi il nuovo sfondo con un prompt oppure guidalo con immagini di riferimento. | DYNAMIC_COMBO | Sì | `"prompt"`<br>`"reference images"` |
| `original_quality` | Restituisce la dimensione in pixel esatta dell'input invece di ridimensionare il risultato a circa 1 megapixel. Un input di grandi dimensioni restituirà quindi un'immagine di grandi dimensioni. (predefinito: false) | BOOLEAN | No | `true`<br>`false` |
| `seed` | Lo stesso seed di solito restituisce lo stesso sfondo; il perfezionamento automatico del prompt può comunque variarlo. (predefinito: 42) | INT | No | da 0 a 2147483647 |
| `moderation` | Impostazioni di moderazione. (predefinito: "false") | DYNAMIC_COMBO | No | `"false"`<br>`"true"` |

### Input del prompt

Visualizzato quando `background` è impostato su `"prompt"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione del nuovo sfondo. Un codice colore esadecimale come #FF5733 produce uno sfondo a tinta unita. Deve contenere almeno 1 carattere. | STRING | Sì | |
| `mode` | `high_control` segue il prompt nel modo più fedele, `base` è un'impostazione predefinita equilibrata e `fast` sacrifica il dettaglio in favore della velocità. | COMBO | Sì | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | Riscrive il prompt per ottenere risultati migliori, traducendo anche i prompt non in inglese. Disattivalo per inviare il prompt esattamente come scritto. (predefinito: true) | BOOLEAN | No | `true`<br>`false` |

### Input di immagini di riferimento

Visualizzato quando `background` è impostato su `"reference images"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `ref_images` | Slot espandibile: collega da 1 a 10 immagini che guidano il nuovo sfondo; non devono avere necessariamente la stessa dimensione. Ogni riferimento modifica il risultato, quindi pochi riferimenti coerenti sono meglio di molti riferimenti contrastanti. Un input in batch viene conteggiato una volta per immagine. | IMAGE | Sì | da 1 a 10 immagini |
| `enhance_ref_images` | Elaborazione aggiuntiva delle immagini di riferimento per ottenere risultati migliori. (predefinito: true) | BOOLEAN | No | `true`<br>`false` |

### Input di moderazione

Visualizzato quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Abilita la moderazione per il contenuto del prompt. (predefinito: false) | BOOLEAN | No | `true`<br>`false` |
| `visual_input_moderation` | Abilita la moderazione per l'input visivo. (predefinito: false) | BOOLEAN | No | `true`<br>`false` |
| `visual_output_moderation` | Abilita la moderazione per l'output visivo. (predefinito: false) | BOOLEAN | No | `true`<br>`false` |

**Nota:** L'input `ref_images` accetta un massimo di 10 immagini; fornirne più di 10 restituisce un errore. Il campo `prompt` deve contenere almeno 1 carattere. Quando `original_quality` è false, l'immagine di input viene ridimensionata a circa 1 megapixel prima dell'elaborazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine con il nuovo sfondo. | IMAGE |
| `refined_prompt` | Il prompt utilizzato da Bria per la generazione, vuoto nel percorso con immagini di riferimento. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/it.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
