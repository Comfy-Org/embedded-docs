# Unisci Latent SeedVR2

Questo nodo ricombina i chunk temporali latent di SeedVR2 campionati in un unico latent a lunghezza completa. Quando viene specificata una sovrapposizione temporale, esegue un crossfade di ogni regione sovrapposta con una finestra di Hann per creare transizioni fluide tra i chunk; quando la sovrapposizione è 0, esegue una concatenazione semplice.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `latents` | I chunk temporali campionati in ordine di sequenza. | LATENT | Sì | Elenco di latent |
| `temporal_overlap` | L'output temporal_overlap di Split SeedVR2 Latent. 0 = concatenazione semplice. (predefinito: 0) | INT | Sì | 0 a 16384 |

**Nota:** Il valore `temporal_overlap` deve essere maggiore o uguale a 0. Tutti i chunk devono essere latent video a 5 dimensioni (B, C, T, H, W) e devono corrispondere in ogni dimensione tranne l'asse temporale (T); solo il chunk finale può essere più corto degli altri. Se viene fornito un solo chunk, viene restituito invariato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `latent` | Il latent ricombinato a lunghezza completa. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/it.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
