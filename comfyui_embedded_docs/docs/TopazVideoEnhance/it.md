# TopazVideoEnhance

Il nodo Topaz Video Enhance dà nuova vita ai video con una potente tecnologia di upscaling e recupero, utilizzando un'API esterna per migliorare la qualità video. Può aumentare la risoluzione del video, incrementare la frequenza dei fotogrammi tramite interpolazione e applicare la compressione. Il nodo elabora un video MP4 in input e restituisce una versione migliorata in base alle impostazioni selezionate. Questo nodo è contrassegnato come deprecato (legacy).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il file video di input da migliorare. | VIDEO | Sì | - |
| `upscaler_enabled` | Abilita o disabilita la funzione di upscaling video (predefinito: True). | BOOLEAN | Sì | - |
| `upscaler_model` | Il modello AI utilizzato per l'upscaling del video. | COMBO | Sì | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | La risoluzione di destinazione per il video con upscaling. | COMBO | Sì | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Livello di creatività (si applica solo a Starlight (Astra) Creative). (predefinito: "low") | COMBO | No | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Abilita o disabilita la funzione di interpolazione dei fotogrammi (predefinito: False). | BOOLEAN | No | - |
| `interpolation_model` | Il modello utilizzato per l'interpolazione dei fotogrammi (predefinito: "apo-8"). | COMBO | No | `"apo-8"` |
| `interpolation_slowmo` | Fattore di slow-motion applicato al video di input. Ad esempio, 2 rende l'output due volte più lento e raddoppia la durata. (predefinito: 1) | INT | No | 1 a 16 |
| `interpolation_frame_rate` | Frequenza dei fotogrammi di output. (predefinito: 60) | INT | No | 15 a 240 |
| `interpolation_duplicate` | Analizza l'input alla ricerca di fotogrammi duplicati e li rimuove. (predefinito: False) | BOOLEAN | No | - |
| `interpolation_duplicate_threshold` | Sensibilità di rilevamento per i fotogrammi duplicati. (predefinito: 0.01) | FLOAT | No | 0.001 a 0.1 |
| `dynamic_compression_level` | Livello CQP. (predefinito: "Low") | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` |

**Nota:** Almeno una funzione di miglioramento deve essere abilitata. Il nodo genererà un errore se sia `upscaler_enabled` sia `interpolation_enabled` sono impostati su False. Il video di input deve essere in formato MP4. L'impostazione `upscaler_creativity` si applica solo quando `upscaler_model` è impostato su "Starlight (Astra) Creative". I file video molto grandi che richiedono caricamenti in più parti non sono supportati.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il file video di output migliorato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/it.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
