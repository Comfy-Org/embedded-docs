# sync.so Lip Sync

Questo nodo risincronizza il movimento della bocca in un video con un nuovo audio del parlato utilizzando l'API sync.so. Gestisce automaticamente primi piani, profili e ostruzioni preservando l'espressione del parlante. Il costo è proporzionale alla durata dell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Filmati del parlante da risincronizzare. Fino a 4K (4096x2160); una frequenza di fotogrammi costante di 24/25/30 fps funziona meglio. | VIDEO | Sì | - |
| `audio` | Audio del parlato con cui sincronizzare la bocca. | AUDIO | Sì | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | 0 a 2147483647 |
| `model` | Modello di generazione sync.so. | COMBO | Sì | "sync-3" |

Il parametro `model` è un combo dinamico che include i seguenti sotto-parametri:

| Sotto-parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------------|-------------|--------------|--------------|------------|
| `sync_mode` | Come gestire una discrepanza di durata tra video e audio; questo imposta anche la lunghezza dell'output. bounce: il video viene riprodotto in avanti e poi all'indietro finché l'audio non termina (output = durata audio). loop: il video ricomincia finché l'audio non termina (output = durata audio). remap: il video viene dilatato temporalmente per corrispondere all'audio (output = durata audio). cut_off: la traccia più lunga viene tagliata (output = durata più breve). silence: nulla viene tagliato; la traccia più breve viene riempita (output = durata più lunga). (predefinito: "bounce") | COMBO | Sì | "bounce"<br>"cut_off"<br>"loop"<br>"silence"<br>"remap" |
| `speaker_selection` | Quale volto sincronizzare labialmente quando sono visibili più persone. default: lascia decidere al modello. auto-detect: rileva e segue il parlante attivo. coordinates: punta al volto alle coordinate pixel (speaker_x, speaker_y) nel fotogramma scelto da speaker_frame. (predefinito: "default") | COMBO | Sì | "default"<br>"auto-detect"<br>"coordinates" |
| `speaker_frame` | Fotogramma video usato per localizzare il parlante. Usato solo quando `speaker_selection` è 'coordinates'. (predefinito: 0) | INT | No | 0 a 1.000.000 |
| `speaker_x` | Coordinata X in pixel del volto del parlante. Usato solo quando `speaker_selection` è 'coordinates'. (predefinito: 0) | INT | No | 0 a 4096 |
| `speaker_y` | Coordinata Y in pixel del volto del parlante. Usato solo quando `speaker_selection` è 'coordinates'. (predefinito: 0) | INT | No | 0 a 4096 |

**Vincoli:**
- La risoluzione video non deve superare 4K (4096x2160). I video al di sopra di questo limite genereranno un errore.
- Le durate di video e audio non devono superare 600 secondi (10 minuti).
- I parametri `speaker_frame`, `speaker_x` e `speaker_y` vengono usati solo quando `speaker_selection` è impostato su "coordinates".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video risincronizzato con il movimento della bocca allineato all'audio fornito. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/it.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`
