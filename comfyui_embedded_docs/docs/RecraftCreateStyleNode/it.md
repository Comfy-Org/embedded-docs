# RecraftCreateStyleNode

Questo nodo crea uno stile personalizzato per la generazione di immagini caricando immagini di riferimento. Puoi caricare da 1 a 5 immagini per definire il nuovo stile e il nodo restituirà un ID stile univoco utilizzabile con altri nodi Recraft. La dimensione totale combinata di tutti i file delle immagini caricate non deve superare i 5 MB.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `style` | Lo stile di base delle immagini generate. | STRING | Sì | `"realistic_image"`<br>`"digital_illustration"` |
| `images` | Un insieme da 1 a 5 immagini di riferimento utilizzate per creare lo stile personalizzato. | IMAGE | Sì | da 1 a 5 immagini |

**Nota:** La dimensione totale dei file di tutte le immagini nell'input `images` deve essere inferiore a 5 MB. Il nodo genererà un errore se questo limite viene superato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `style_id` | L'identificatore univoco per lo stile personalizzato appena creato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/it.md)

---
**Source fingerprint (SHA-256):** `36edcb0b96eed5930d9d7ff00a1812d129b7cd9b7ab0f0d758594a20791826b2`
