# ShuffleVideoDataset

Questo nodo prende un elenco di video e li riordina casualmente. Utilizza un seed casuale per rendere il mescolamento riproducibile, così lo stesso seed produce sempre lo stesso ordine di output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `videos` | Elenco di video da mescolare. | VIDEO | Sì | Elenco di input video |
| `seed` | Seed casuale per il mescolamento (predefinito: 0). | INT | No | da 0 a 18446744073709551615 |

Nota: il valore del seed viene ridotto modulo 4294967295 (2^32 - 1) prima di essere utilizzato. Di conseguenza, i seed che differiscono per un multiplo di 4294967295 producono lo stesso ordine di output.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `videos` | Elenco di video mescolato in ordine casuale. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/it.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
