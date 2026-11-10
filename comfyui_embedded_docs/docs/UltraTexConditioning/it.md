# UltraTex Conditioning

Condiziona FLUX.2 Klein 9B con la LoRA UltraTex per applicare l'aspetto di un'immagine di riferimento su una mesh, come un'immagine per vista. Esegui il rendering delle viste con Render Mesh in modalità `world normal`, da un Create Camera Orbit di 4, più top e bottom, ed esegui il bake del risultato con Bake Texture From Views.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | Condizionamento testuale. UltraTex è stata addestrata con un prompt vuoto. | CONDITIONING | Sì | - |
| `vae` | VAE utilizzato per codificare le normali, le viste e il riferimento. | VAE | Sì | - |
| `normals` | Immagini `world normal` di Render Mesh: le 6 viste canoniche oppure le 4 viste laterali. | IMAGE | Sì | - |
| `masks` | Maschere di Render Mesh delle stesse viste, una per vista. | MASK | Sì | - |
| `reference` | L'oggetto come dovrebbe apparire, visto dal lato della camera frontale. | IMAGE | Sì | - |
| `reference_mask` | Maschera dell'oggetto del riferimento, bianca per l'oggetto. Predefinito: completamente bianca. | MASK | No | - |
| `extra_views` | Ulteriori riferimenti: l'oggetto visto dalle altre viste, ciascuno associato alla propria vista come il riferimento è associato alla vista frontale. Predefinito: `"off"`. | DYNAMIC_COMBO | Sì | `"off"`<br>`"on"` |

### Input con Extra Views "on"

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `right` | L'oggetto visto dalla vista destra. | IMAGE | No | - |
| `back` | L'oggetto visto dalla vista posteriore. | IMAGE | No | - |
| `left` | L'oggetto visto dalla vista sinistra. | IMAGE | No | - |
| `top` | L'oggetto visto dall'alto. | IMAGE | No | - |
| `bottom` | L'oggetto visto dal basso. | IMAGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | Condizionamento che trasporta la griglia delle viste, i latenti di riferimento e le maschere dei token necessarie a UltraTex. | CONDITIONING |

Nota: `normals` deve contenere le 6 viste canoniche (Create Camera Orbit con `count` 4 e `poles` top e bottom) oppure le 4 viste laterali, e `masks` deve corrispondere al relativo numero di viste.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/it.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
