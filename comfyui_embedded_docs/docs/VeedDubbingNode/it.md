# VEED Dubbing

VEED Dubbing traduce il parlato di un video in un'altra lingua con VEED, clonando la voce di ogni parlante e sincronizzando il movimento delle labbra con la traduzione. La clip viene caricata, il job VEED viene interrogato periodicamente e il video doppiato viene restituito a 25 fps, con una durata pari a quella della nuova traccia audio. Usalo per localizzare una clip già pronta senza rigirare scene né registrare nuovamente la voce.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello di doppiaggio. `"standard"` è più economico e restituisce audio mono, con spagnolo latinoamericano e portoghese brasiliano; `"pro"` aggiunge accenti regionali e audio stereo. La selezione di un modello mostra `video`, `target_language`, `source_language` e `seed`. | DYNAMIC_COMBO | Sì | `"standard"`<br>`"pro"` |

### Input di standard

Questi input compaiono quando `model` è impostato su `"standard"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video con un volto visibile e parlato, fino a 599 secondi. L'output ha la stessa durata della sua traccia audio e viene riprodotto a 25 fps. | VIDEO | Sì | Fino a 599 secondi |
| `target_language` | Lingua in cui eseguire il doppiaggio, una delle 85 lingue. (predefinito: `"English"`) | COMBO | Sì | 85 lingue |
| `source_language` | Lingua parlata nel video, oppure `"auto"` per rilevarla. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>85 lingue |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

### Input di pro

Questi input compaiono quando `model` è impostato su `"pro"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video con un volto visibile e parlato, fino a 599 secondi. L'output ha la stessa durata della sua traccia audio e viene riprodotto a 25 fps. | VIDEO | Sì | Fino a 599 secondi |
| `target_language` | Lingua o accento regionale in cui eseguire il doppiaggio: 87 lingue più 14 accenti come `"English (UK)"`, `"Spanish (Mexico)"` e `"Portuguese (Brazil)"`. (predefinito: `"English (US)"`) | COMBO | Sì | 101 opzioni |
| `source_language` | Lingua parlata nel video, oppure `"auto"` per rilevarla. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>91 lingue |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

Il nodo si arresta con un errore quando il video non ha una traccia audio, quando la clip dura più di 599 secondi o quando il job VEED fallisce.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | Il video doppiato: il filmato originale con il parlato tradotto e il movimento delle labbra sincronizzato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/it.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`
