# EmptyMiniMaxMusic3LatentAudio

Questo nodo crea un latente audio vuoto (riempito di zeri) per il modello MiniMax Music3. Converte la durata richiesta in secondi nel numero corrispondente di frame audio e produce un tensore latente vuoto della dimensione corretta, pronto per essere usato come punto di partenza per la generazione musicale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `seconds` | La durata del latente audio in secondi (predefinito: 120.0). Il valore viene convertito in frame audio e limitato ai limiti di durata supportati dal modello. | FLOAT | Sì | da 0.04 a (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), passo 0.04 |
| `batch_size` | Il numero di latenti audio da generare in un batch (predefinito: 1). | INT | Sì | da 1 a 4096 |

Nota: il valore `seconds` viene arrotondato al frame audio più vicino e limitato a un minimo di 1 frame e a un massimo di `MAX_AUDIO_FRAMES` frame, quindi la lunghezza effettiva del latente può differire leggermente dal valore esatto inserito.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `LATENT` | Un tensore latente audio riempito di zeri con forma (batch_size, 128, latent_length). Include metadati che contrassegnano il campione come dati audio con un rapporto di ridimensionamento temporale di 512. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
