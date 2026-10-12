# ModelMergeWAN2_1

Il nodo ModelMergeWAN2_1 unisce due modelli WAN2.1 fondendo i loro componenti tramite medie ponderate. Supporta diverse dimensioni di modello, inclusi i modelli 1.3B con 30 blocchi e i modelli 14B con 40 blocchi, con una gestione speciale per i modelli image-to-video che includono un componente aggiuntivo di embedding dell'immagine. Ogni componente può essere pesato individualmente per controllare il rapporto di fusione tra i due modelli di input.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Primo modello da unire | MODEL | Sì | - |
| `model2` | Secondo modello da unire | MODEL | Sì | - |
| `patch_embedding.` | Peso per il componente patch embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `time_embedding.` | Peso per il componente time embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `time_projection.` | Peso per il componente time projection (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `text_embedding.` | Peso per il componente text embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `img_emb.` | Peso per il componente image embedding, utilizzato nei modelli image-to-video (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.0.` | Peso per il blocco 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.1.` | Peso per il blocco 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.2.` | Peso per il blocco 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.3.` | Peso per il blocco 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.4.` | Peso per il blocco 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.5.` | Peso per il blocco 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.6.` | Peso per il blocco 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.7.` | Peso per il blocco 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.8.` | Peso per il blocco 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.9.` | Peso per il blocco 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.10.` | Peso per il blocco 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.11.` | Peso per il blocco 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.12.` | Peso per il blocco 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.13.` | Peso per il blocco 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.14.` | Peso per il blocco 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.15.` | Peso per il blocco 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.16.` | Peso per il blocco 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.17.` | Peso per il blocco 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.18.` | Peso per il blocco 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.19.` | Peso per il blocco 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.20.` | Peso per il blocco 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.21.` | Peso per il blocco 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.22.` | Peso per il blocco 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.23.` | Peso per il blocco 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.24.` | Peso per il blocco 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.25.` | Peso per il blocco 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.26.` | Peso per il blocco 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.27.` | Peso per il blocco 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.28.` | Peso per il blocco 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.29.` | Peso per il blocco 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.30.` | Peso per il blocco 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.31.` | Peso per il blocco 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.32.` | Peso per il blocco 32 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.33.` | Peso per il blocco 33 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.34.` | Peso per il blocco 34 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.35.` | Peso per il blocco 35 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.36.` | Peso per il blocco 36 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.37.` | Peso per il blocco 37 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.38.` | Peso per il blocco 38 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.39.` | Peso per il blocco 39 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `head.` | Peso per il componente head (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

**Nota:** Tutti i parametri di peso utilizzano un intervallo da 0.0 a 1.0 con incrementi di 0.01. Il nodo fornisce fino a 40 input di peso per i blocchi per adattarsi alle diverse dimensioni dei modelli: i modelli 1.3B usano 30 blocchi (`blocks.0.` fino a `blocks.29.`), mentre i modelli 14B usano 40 blocchi (`blocks.0.` fino a `blocks.39.`). Il parametro `img_emb.` è utilizzato dai modelli image-to-video.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello unito che combina i componenti di entrambi i modelli di input in base ai pesi specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/it.md)

---
**Source fingerprint (SHA-256):** `6a17defa25b1ef045b85af4a73e00d3a64c1948c0c47f355d1d488a75b09f224`
