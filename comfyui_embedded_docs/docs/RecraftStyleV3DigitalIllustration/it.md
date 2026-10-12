# RecraftStyleV3DigitalIllustration

Questo nodo configura uno stile da utilizzare con l'API Recraft, selezionando specificamente lo stile "digital_illustration". Consente di scegliere un sottostile opzionale per affinare ulteriormente la direzione artistica dell'immagine generata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `substyle` | Un sottostile opzionale per specificare un particolare tipo di illustrazione digitale. Se non selezionato, viene utilizzato lo stile di base "digital_illustration". | STRING | No | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `recraft_style` | Un oggetto stile configurato contenente lo stile "digital_illustration" selezionato e il sottostile opzionale, pronto per essere passato ad altri nodi dell'API Recraft. | STYLEV3 |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/it.md)

---
**Source fingerprint (SHA-256):** `b6901d81bc11c3226d847ed61386b9bcf4ece90f6a95b6ad9888f102ef355594`
