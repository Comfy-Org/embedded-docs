# Recraft Stile - Logo Raster

Questo nodo seleziona lo stile raster del logo e un sottostile specifico per la generazione di immagini di logo. È specializzato nella creazione di design di logo con trattamenti visivi di tipo raster. Lo stile scelto viene restituito come impostazione di stile Recraft che può essere passata ad altri nodi Recraft.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `substyle` | Il sottostile raster specifico del logo da applicare per la generazione del logo | COMBO | Sì | `"bold"`<br>`"minimal"`<br>`"vibrant"`<br>`"handdrawn"`<br>`"geometric"`<br>`"vintage"`<br>`"neon"`<br>`"gradient"`<br>`"flat"`<br>`"outline"`<br>`"mascot"`<br>`"badge"`<br>`"abstract"`<br>`"retro"`<br>`"modern"`<br>`"playful"`<br>`"luxury"`<br>`"tech"`<br>`"nature"`<br>`"food"`<br>`"sport"`<br>`"fashion"`<br>`"music"`<br>`"travel"`<br>`"education"`<br>`"health"`<br>`"finance"`<br>`"realestate"`<br>`"nonprofit"` |

Nota: è necessario selezionare sempre un sottostile; non esiste un'opzione "none".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `recraft_style` | La configurazione dello stile Recraft selezionata, che include lo stile raster del logo e il sottostile scelto | CUSTOM |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3LogoRaster/it.md)

---
**Source fingerprint (SHA-256):** `59c3af980261d2b20b6d401980639c6bbc3a8b7c4e2370ca048ccb07535b10e7`
