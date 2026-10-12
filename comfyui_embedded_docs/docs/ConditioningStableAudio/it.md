# Condizionamento Stable Audio

Il nodo ConditioningStableAudio aggiunge informazioni di temporizzazione sia agli input di conditioning `positive` sia a quelli `negative` per la generazione audio. Imposta i parametri di tempo iniziale e durata totale che aiutano a controllare quando e per quanto tempo deve essere generato il contenuto audio. Questo nodo modifica i dati di conditioning esistenti aggiungendo metadati di temporizzazione specifici per l'audio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di conditioning `positive` da modificare con le informazioni di temporizzazione audio | CONDITIONING | Sì | - |
| `negative` | L'input di conditioning `negative` da modificare con le informazioni di temporizzazione audio | CONDITIONING | Sì | - |
| `seconds_start` | Il tempo iniziale in secondi per la generazione audio (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1000.0 (passo 0.1) |
| `seconds_total` | La durata totale in secondi per la generazione audio (predefinito: 47.0) | FLOAT | Sì | 0.0 a 1000.0 (passo 0.1) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il conditioning `positive` modificato a cui sono state applicate le informazioni di temporizzazione audio | CONDITIONING |
| `negative` | Il conditioning `negative` modificato a cui sono state applicate le informazioni di temporizzazione audio | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/it.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
