# ModelMergeSD1

Il nodo ModelMergeSD1 fonde insieme due modelli Stable Diffusion 1.x regolando quanto ciascun componente del modello contribuisce al risultato. Offre un controllo individuale su time embedding, label embedding e ogni blocco di input, intermedio e output, consentendo una fusione dei modelli ottimizzata per casi d'uso specifici.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `time_embed.` | Peso di fusione del livello di time embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `label_emb.` | Peso di fusione del livello di label embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.0.` | Peso di fusione del blocco di input 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.1.` | Peso di fusione del blocco di input 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.2.` | Peso di fusione del blocco di input 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.3.` | Peso di fusione del blocco di input 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.4.` | Peso di fusione del blocco di input 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.5.` | Peso di fusione del blocco di input 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.6.` | Peso di fusione del blocco di input 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.7.` | Peso di fusione del blocco di input 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.8.` | Peso di fusione del blocco di input 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.9.` | Peso di fusione del blocco di input 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.10.` | Peso di fusione del blocco di input 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `input_blocks.11.` | Peso di fusione del blocco di input 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `middle_block.0.` | Peso di fusione del blocco intermedio 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `middle_block.1.` | Peso di fusione del blocco intermedio 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `middle_block.2.` | Peso di fusione del blocco intermedio 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.0.` | Peso di fusione del blocco di output 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.1.` | Peso di fusione del blocco di output 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.2.` | Peso di fusione del blocco di output 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.3.` | Peso di fusione del blocco di output 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.4.` | Peso di fusione del blocco di output 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.5.` | Peso di fusione del blocco di output 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.6.` | Peso di fusione del blocco di output 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.7.` | Peso di fusione del blocco di output 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.8.` | Peso di fusione del blocco di output 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.9.` | Peso di fusione del blocco di output 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.10.` | Peso di fusione del blocco di output 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `output_blocks.11.` | Peso di fusione del blocco di output 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `out.` | Peso di fusione del livello di output (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |

Tutti i pesi di fusione accettano valori da 0.0 a 1.0 e sono impostati su 1.0 per impostazione predefinita; ciò significa che ogni componente del primo modello viene utilizzato completamente, salvo modifiche.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/it.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
