# Quiver Immagine in SVG

Questo nodo converte un'immagine raster in una grafica vettoriale scalabile (SVG) utilizzando i modelli di vettorizzazione di Quiver AI. Invia l'immagine a un'API esterna che la elabora e restituisce il risultato vettorizzato.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `immagine` | Immagine di input da vettorizzare. | IMAGE | Sì | N/A |
| `ritaglio automatico` | Ritaglia automaticamente sul soggetto dominante (predefinito: False). | BOOLEAN | Sì | True<br>False |
| `modello` | Modello da usare per la vettorizzazione SVG. Selezionando un modello vengono rivelati parametri aggiuntivi specifici di quel modello: `target_size` (dimensione target quadrata del ridimensionamento in pixel; 0 mantiene la dimensione dell'immagine di origine, altrimenti da 128 a 4096), `temperature`, `top_p` e `presence_penalty`. | DYNAMIC_COMBO | Sì | `"arrow-2"`<br>`"arrow-2-telos"` |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal valore del seed. Questo parametro ha la funzionalità "control after generate" (predefinito: 0). | INT | Sì | 0 to 2147483647 |
| `reasoning_effort` | Quanto ragionamento impiega il modello prima di disegnare. Livelli più alti migliorano il dettaglio e costano più token. Usato solo dai modelli Arrow 2 (predefinito: "high"). | COMBO | No | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `SVG` | L'output SVG vettorizzato. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/it.md)

---
**Source fingerprint (SHA-256):** `196b0693328478bff21b11da87c52608e8bb57abb9bf482052782231f6d81c30`
