# Mescola Elenco Immagini

Il nodo Shuffle Dataset riceve un elenco di immagini e ne modifica casualmente l'ordine. Utilizza un valore seed per controllare la casualità, garantendo che lo stesso ordine di mescolamento possa essere riprodotto. Questo è utile per randomizzare la sequenza di immagini in un dataset prima dell'elaborazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | L'elenco di immagini da mescolare. | IMAGE | Sì | - |
| `seed` | Seme casuale. (predefinito: 0) | INT | No | 0 to 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `images` | Lo stesso elenco di immagini, ma in un nuovo ordine casuale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/it.md)

---
**Source fingerprint (SHA-256):** `6cde5dcf15817ab98f35f7b2e40fe79a5451c86dba93c0e3cd2622d1cec76c36`
