# EmptyAudio

Il nodo EmptyAudio genera un clip audio silenzioso con durata, frequenza di campionamento e configurazione dei canali specificate. Crea una forma d'onda contenente tutti zeri, producendo silenzio completo per la durata indicata. Questo nodo è utile per creare audio segnaposto o generare segmenti silenziosi nei flussi di lavoro audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `duration` | Durata del clip audio vuoto in secondi (impostazione predefinita: 60.0) | FLOAT | Sì | 0.0 a 1.8446744073709552e+19 |
| `sample_rate` | Frequenza di campionamento del clip audio vuoto (impostazione predefinita: 44100) | INT | Sì | 1 a 192000 |
| `channels` | Numero di canali audio (1 per mono, 2 per stereo) (impostazione predefinita: 2) | INT | Sì | 1 a 2 |

## Output
| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `AUDIO` | Il clip audio silenzioso generato, contenente i dati della forma d'onda e le informazioni sulla frequenza di campionamento | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/it.md)

---
**Source fingerprint (SHA-256):** `687bfe02cb0192add9128ae9040fa5773be0d7a0a5df17618cf56050901c6dc5`
