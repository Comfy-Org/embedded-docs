# Luma Ray 3.2 Modifica Video

## Panoramica

Questo nodo esegue nuovamente il rendering di un video esistente con un nuovo prompt usando Luma Ray 3.2, consentendo di modificarne lo stile, l'illuminazione, aggiungere o rimuovere elementi mantenendo il movimento originale. Il video sorgente può durare fino a 18 secondi e il video modificato mantiene la durata originale della sorgente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video sorgente da modificare. Fino a 18 secondi. | VIDEO | Sì | - |
| `prompt` | Descrive la modifica desiderata. | STRING | Sì | - |
| `resolution` | La risoluzione di output per il video modificato. (predefinito: "720p") | COMBO | Sì | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Quanto preservare rispetto a reinterpretare la sorgente. "auto" lascia scegliere a Ray 3.2; `adhere_*` preserva il più possibile, `flex_*` è bilanciato, `reimagine_*` modifica il più possibile. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Seed per la riproducibilità. | INT | Sì | - |

**Nota:** `prompt` deve essere compreso tra 1 e 6000 caratteri. Il video sorgente non deve superare i 18 secondi di durata.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | Il video modificato in output. | VIDEO |
| `generation_id` | L'identificatore univoco per la richiesta di generazione. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/it.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
