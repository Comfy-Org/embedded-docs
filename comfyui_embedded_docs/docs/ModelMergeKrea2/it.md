# ModelMergeKrea2

Questo nodo unisce due modelli combinando i loro componenti interni a un livello molto dettagliato, consentendoti di controllare quanto le parti specifiche di ciascun modello influenzino il risultato finale. Funziona prendendo due modelli di input e applicando rapporti di fusione separati a diverse sezioni della loro architettura.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `first.` | Rapporto di fusione per il primo blocco layer (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `tmlp.` | Rapporto di fusione per il blocco MLP temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtmlp.` | Rapporto di fusione per il blocco MLP testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `tproj.` | Rapporto di fusione per il blocco di proiezione temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.layerwise_blocks.0.` | Rapporto di fusione per il primo blocco layerwise della fusione testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.layerwise_blocks.1.` | Rapporto di fusione per il secondo blocco layerwise della fusione testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.projector.` | Rapporto di fusione per il blocco proiettore della fusione testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.refiner_blocks.0.` | Rapporto di fusione per il primo blocco di raffinamento della fusione testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.refiner_blocks.1.` | Rapporto di fusione per il secondo blocco di raffinamento della fusione testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `blocks.0.` fino a `blocks.27.` | Rapporto di fusione per ciascuno dei 28 blocchi principali (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `last.` | Rapporto di fusione per l'ultimo blocco (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |

Ogni rapporto di fusione controlla quanto di `model2` viene utilizzato per quello specifico componente: 0.0 significa utilizzare solo `model1`, 1.0 significa utilizzare solo `model2`, mentre i valori intermedi creano una fusione ponderata.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello unito risultante dalla fusione dei due modelli di input in base ai rapporti specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/it.md)

---
**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`
