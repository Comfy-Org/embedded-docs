# VEED Clean Audio

Rimuovi il rumore di fondo dal parlato con VEED. È progettato per il parlato in qualsiasi lingua: il rumore sotto la voce viene eliminato, le pause vengono ripulite completamente e la musica e gli effetti sonori vengono rimossi anziché conservati. L'output è audio mono a 48 kHz.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | Registrazione vocale, inferiore a 30 minuti. | AUDIO | Sì | Fino a 1799 secondi |
| `strength` | Quanto rumore viene rimosso sotto il parlato. Valori più bassi mantengono più rumore ambientale dietro la voce; le pause tra le parole vengono sempre ripulite completamente, e i valori superiori a quello predefinito apportano scarsi cambiamenti. (predefinito: 0.874) | FLOAT | Sì | 0.0 a 1.0 (passo 0.001) |
| `loudness` | Indica se normalizzare la loudness dell'output. `"normalize"` imposta l'output su `target_lufs`; `"keep input level"` lascia il livello invariato. Selezionando un'opzione vengono mostrati i relativi parametri. (predefinito: `"normalize"`) | DYNAMIC_COMBO | Sì | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Loudness integrata dell'output in LUFS. I picchi sono limitati a -1.1 dBTP, quindi i target più elevati si fermano prima (circa -15 LUFS per il parlato tipico). Disponibile quando `loudness` è `"normalize"` (predefinito: -19.0). | FLOAT | Sì | -40.0 a -8.0 (passo 0.1) |

Il nodo si arresta con un errore quando la registrazione dura più di 1799 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `AUDIO` | Il parlato ripulito come audio mono a 48 kHz. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/it.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
