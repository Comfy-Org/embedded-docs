# LTXVFreezeLatent

Il nodo LTXV Freeze Latent imposta a zero la maschera di rumore di un latent, il che mantiene quel latent pulito e invariato durante l'esecuzione del campionamento. Funziona sia su latent video che audio, quindi un latent può essere congelato prima che venga concatenato con altri o quando non dovrebbe essere denoizzato affatto.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `latent` | Latent video o audio da congelare. L'audio è 4D; il video è 5D. | LATENT | Sì | N/A |

### Vincoli

- Il latent deve contenere un tensore semplice. Un latent audio-video concatenato non è accettato; deve essere prima separato con il nodo Separate AV Latent.
- Sono supportati solo latent 4D (audio) e 5D (video). Qualsiasi altra forma causa un errore.
- La maschera di rumore generata viene creata con zeri utilizzando lo stesso dispositivo del tensore di input. Per i latent video la maschera ha forma (batch, 1, frames, 1, 1); per i latent audio ha forma (batch, 1, frames, 1).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `latent` | Il latent di input con una maschera di rumore di zeri aggiunta, in modo che rimanga pulito durante il campionamento. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/it.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
