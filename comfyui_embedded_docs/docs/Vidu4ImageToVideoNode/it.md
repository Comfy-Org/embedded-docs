# Vidu4ImageToVideoNode

Genera un video da un fotogramma iniziale e un prompt opzionale con un modello Vidu Q4. L'output mantiene le proporzioni dell'immagine di input.

Selezionando un `model` vengono mostrati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Fotogramma iniziale del video generato. Le proporzioni devono essere comprese tra 1:5 e 5:1. | IMAGE | Sì | N/D |
| `model` | Modello da usare per la generazione del video. Selezionando un modello vengono mostrati i parametri specifici: `prompt`, `resolution`, `duration`, `audio` e `seed`. | DYNAMIC_COMBO | Sì | `"Vidu Q4 Preview"` |
| `prompt` | Un prompt testuale opzionale per la generazione del video, fino a 5000 caratteri (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video di output (predefinito: `"720p"`). | COMBO | Sì | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Durata del video di output in secondi (predefinito: 5). | INT | Sì | da 3 a 16 |
| `audio` | Se abilitato, produce un video con audio, inclusi dialoghi ed effetti sonori (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Questo parametro ha la funzionalità «control after generate» (predefinito: 42). | INT | Sì | da 1 a 2147483647 |

**Nota:** Le proporzioni di `image` devono rimanere tra 1:5 e 5:1, e il `prompt` non può superare i 5000 caratteri. Il risultato mantiene le proporzioni dell'immagine di input, quindi la dimensione dell'output segue l'impostazione `resolution` solo all'interno di tali proporzioni.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
