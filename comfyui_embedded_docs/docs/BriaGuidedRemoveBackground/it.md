# Bria Guided Remove Background

Questo nodo rimuove lo sfondo da un'immagine con Bria, mantenendo ciò che il prompt descrive. I pixel originali vengono restituiti alla piena risoluzione con un nuovo canale alfa anziché essere renderizzati di nuovo, così i dettagli fini e i bordi vengono preservati. Un prompt che non corrisponde a nulla restituisce un'immagine completamente trasparente. Per un semplice ritaglio senza indicazioni, Bria Remove Image Background ha un costo inferiore.

## Input

Il selettore `moderation` mostra ulteriori opzioni di moderazione quando è impostato su `"true"`.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine da ritagliare. | IMAGE | Sì | - |
| `prompt` | Cosa mantenere e, facoltativamente, cosa eliminare o restringere, ad esempio "la persona con il tappetino e la pianta", "la donna alla scrivania senza la lampada" o "solo la sedia". Non deve essere vuoto. Se nulla corrisponde al prompt, il risultato è completamente trasparente. Predefinito: `""` (stringa vuota). | STRING | Sì | 1 carattere o più |
| `moderation` | Impostazioni di moderazione. Se impostato su `"true"`, i flag di moderazione visiva riportati di seguito diventano disponibili. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input con moderazione "true"

Questi parametri compaiono solo quando `moderation` è impostato su `"true"`. L'opzione `"false"` non aggiunge input aggiuntivi.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input. Predefinito: `False`. | BOOLEAN | No | True / False |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine generata. Predefinito: `False`. | BOOLEAN | No | True / False |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine ritagliata: i pixel originali con un nuovo canale alfa. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/it.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`
