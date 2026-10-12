# LTX 2.5 Text To Video

LTX 2.5 Text To Video è un nodo API che genera video di qualità professionale da una descrizione testuale utilizzando il modello LTX 2.5. Fornisci un prompt e scegli le impostazioni di generazione come il livello del modello, la durata, la risoluzione, la frequenza dei fotogrammi e se includere l'audio; il nodo invia l'attività all'API LTX e restituisce il video risultante.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il livello del modello LTX 2.5 da utilizzare per la generazione video. | STRING | Sì | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | La durata del video generato. | INT | Sì | Intero |
| `model.resolution` | La risoluzione di output del video. Le opzioni disponibili dipendono dal `model` selezionato. | STRING | Sì | Con "LTX-2.5 (Fast)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>Con "LTX-2.5 (Pro)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `model.fps` | Frequenza dei fotogrammi del video generato (predefinito: 25). | INT | No | Intero |
| `model.generate_audio` | Indica se generare l'audio insieme al video (predefinito: True). | BOOLEAN | No | True<br>False |
| `prompt` | La descrizione testuale del video da generare. È richiesto un prompt non vuoto di massimo 10.000 caratteri (predefinito: ""). | STRING | Sì | Da 1 a 10000 caratteri |
| `seed` | Valore del seed utilizzato per una generazione riproducibile (predefinito: 42). | INT | No | Intero |

Nota: Le opzioni disponibili per `model.resolution` dipendono dal `model` selezionato. "LTX-2.5 (Fast)" supporta risoluzioni fino a 2160x3840, mentre "LTX-2.5 (Pro)" supporta risoluzioni fino a 1920x1080.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il video generato restituito dall'API LTX, pronto per ulteriori utilizzi nel flusso di lavoro. Se la generazione audio è stata abilitata, il video include audio sincronizzato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/it.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
