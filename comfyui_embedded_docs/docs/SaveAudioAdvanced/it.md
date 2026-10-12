# SaveAudioAdvanced

Salva l'audio di input nella directory di output di ComfyUI. Questo nodo consente di esportare l'audio in vari formati, tra cui FLAC, MP3 e Opus, con impostazioni di qualità configurabili.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | L'audio da salvare. | AUDIO | Sì | - |
| `filename_prefix` | Il prefisso del file da salvare. Può includere token di formattazione come %date:yyyy-MM-dd%. (predefinito: "audio/ComfyUI") | STRING | Sì | - |
| `format` | Il formato file in cui salvare l'audio. | DYNAMIC_COMBO | Sì | "flac"<br>"mp3"<br>"opus" |

### Input di MP3

Quando viene selezionato "mp3" come formato, diventa disponibile la seguente impostazione.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `quality` | La qualità di codifica del file MP3 di output. (predefinito: "V0") | COMBO | No | "V0"<br>"128k"<br>"320k" |

### Input di Opus

Quando viene selezionato "opus" come formato, diventa disponibile la seguente impostazione.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `quality` | La qualità di codifica del file Opus di output. (predefinito: "128k") | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

Nota: l'impostazione `quality` è disponibile solo quando è selezionato il formato corrispondente. Quando è selezionato "flac", non è disponibile alcuna impostazione di qualità aggiuntiva.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `audio` | L'audio di input, passato invariato dopo il salvataggio. | AUDIO |

Il nodo restituisce anche informazioni UI contenenti le informazioni sul file audio salvato.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
