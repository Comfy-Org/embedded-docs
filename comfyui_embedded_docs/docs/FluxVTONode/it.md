# FluxVTONode

Questo nodo esegue un virtual try-on vestendo una persona con un'immagine del capo fornita. Invia le immagini della persona e del capo al servizio BFL Flux VTO, che genera un'immagine realistica della persona che indossa il capo. Un'istruzione testuale opzionale può descrivere come il capo dovrebbe calzare o apparire.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `person` | Immagine della persona da vestire. | IMAGE | Sì | - |
| `garment` | Immagine del capo da applicare. | IMAGE | Sì | - |
| `prompt` | Istruzione di styling opzionale in linguaggio naturale (ad es. come il capo dovrebbe calzare). Il valore predefinito è una stringa vuota. | STRING | No | - |
| `seed` | Il seed casuale utilizzato per creare il rumore. Predefinito: 0. | INT | No | 0 to 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine risultante che mostra la persona che indossa il capo fornito. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/it.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
