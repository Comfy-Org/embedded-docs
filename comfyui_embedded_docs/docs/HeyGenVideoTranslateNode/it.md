# HeyGen Video Translate

Traduce un video parlato in un'altra lingua con clonazione vocale e sincronizzazione labiale. Questo nodo clona la voce dell'oratore originale e rianima la bocca per adattarla al parlato tradotto, producendo un risultato dall'aspetto naturale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video con parlato da tradurre. | VIDEO | Sì | - |
| `output_language` | Lingua di destinazione per il video tradotto. | COMBO | Sì | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' è più veloce; 'precision' produce una sincronizzazione labiale di qualità superiore a un prezzo più alto. (predefinito: "speed") | COMBO | Sì | "speed"<br>"precision" |
| `translate_audio_only` | Sostituisce solo la traccia audio, mantenendo i movimenti originali della bocca (nessuna sincronizzazione labiale). (predefinito: False) | BOOLEAN | No | True<br>False |
| `speaker_count` | Numero di parlanti nel video. 0 = rileva automaticamente. I valori superiori a 0 vengono inviati all'API come numero di parlanti. (predefinito: 0) | INT | No | 0 a 10 |
| `seed` | Non viene inviato a HeyGen; modificalo per forzare una nuova esecuzione. (predefinito: 42) | INT | No | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video tradotto con clonazione vocale e sincronizzazione labiale applicate. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/it.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
