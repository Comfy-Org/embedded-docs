# VEED Clean Audio (in Video)

Rimuovi il rumore di fondo dal parlato in un video con VEED. Cambia solo la traccia audio: viene sostituita con il parlato pulito mono a 48 kHz, mentre immagine, risoluzione e frequenza dei fotogrammi restano invariate. È progettato per il parlato in qualsiasi lingua; la musica e gli effetti sonori vengono rimossi anziché preservati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video con una traccia audio contenente parlato, di durata inferiore a 30 minuti. Il video deve avere una traccia audio. | VIDEO | Sì | Fino a 1799 secondi |
| `strength` | Quanto rumore viene rimosso sotto il parlato. Valori più bassi mantengono più rumore ambientale dietro la voce; le pause tra le parole vengono sempre pulite completamente e i valori superiori a quello predefinito cambiano poco. (predefinito: 0.874) | FLOAT | Sì | Da 0.0 a 1.0 (passo 0.001) |
| `loudness` | Indica se normalizzare il volume del parlato. `"normalize"` lo imposta su `target_lufs`; `"keep input level"` lascia invariato il livello. Selezionando un'opzione vengono mostrati i relativi parametri. (predefinito: `"normalize"`) | DYNAMIC_COMBO | Sì | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Loudness integrata del parlato pulito in LUFS. I picchi sono limitati a -1.1 dBTP, quindi i target elevati si fermano prima (circa -15 LUFS per il parlato tipico). Disponibile quando `loudness` è `"normalize"` (predefinito: -19.0). | FLOAT | Sì | Da -40.0 a -8.0 (passo 0.1) |

Il nodo si interrompe con un errore quando la clip supera i 1799 secondi e quando il video non ha una traccia audio.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `VIDEO` | Il video di input con la traccia audio sostituita dal parlato pulito. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/it.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
