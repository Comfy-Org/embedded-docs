# Kling 3.0 Omni Da Testo a Video

Questo nodo genera un video da una descrizione testuale utilizzando il modello Kling AI più recente. Invia il prompt a un'API remota e restituisce il video generato. Puoi controllare durata, formato e qualità del video e, facoltativamente, creare storyboard multi-inquadratura.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Il modello Kling specifico da usare per la generazione del video (predefinito: `"kling-v3-omni"`). | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto del video. Può includere sia descrizioni positive sia negative. Ignorato quando gli storyboard sono abilitati. | STRING | Sì | 0 to 2500 characters |
| `aspect_ratio` | La forma o le dimensioni del video da generare. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durata del video in secondi (predefinito: 5). | INT | Sì | 3 to 15 seconds |
| `resolution` | La qualità o risoluzione in pixel del video (predefinito: `"1080p"`). Internamente viene mappata su qualità standard, pro o 4k. | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie di segmenti video con prompt e durate individuali. Ignorato per il modello o1. | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Indica se generare l'audio per il video (predefinito: False). | BOOLEAN | No | True / False |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | No | 0 to 2147483647 |

### Sotto-input dello storyboard

Quando `storyboards` è impostato su un valore diverso da `"disabled"`, i seguenti input compaiono per ogni segmento dello storyboard. Nei nomi dei parametri riportati di seguito, `{i}` è il numero del segmento, da 1 fino al numero di storyboard selezionato.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `storyboard_{i}_prompt` | Prompt per il segmento storyboard {i}. Massimo 512 caratteri. | STRING | Sì | 1 to 512 characters |
| `storyboard_{i}_duration` | Durata per il segmento storyboard {i} in secondi (predefinito: 4). | INT | Sì | 1 to 15 seconds |

### Vincoli e limitazioni dei parametri

- **Limitazioni specifiche del modello:**
  - Il modello `kling-video-o1` supporta solo durate di **5 o 10 secondi**.
  - Il modello `kling-video-o1` **non** supporta la generazione audio.
  - Il modello `kling-video-o1` **non** supporta la risoluzione 4k.
  - Il modello `kling-video-o1` **non** supporta gli storyboard.
- **Vincoli degli storyboard:**
  - Quando gli storyboard sono abilitati, il campo `prompt` viene ignorato.
  - Ogni storyboard richiede un proprio prompt (da 1 a 512 caratteri) e una propria durata.
  - La durata totale di tutti gli storyboard deve essere esattamente uguale al parametro globale `duration`.
- **Requisiti del prompt:**
  - Quando gli storyboard sono **disabilitati**, il campo `prompt` è obbligatorio (minimo 1 carattere).
  - Quando gli storyboard sono **abilitati**, il campo `prompt` può essere vuoto (0 caratteri).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il video generato in base al prompt testuale e alle impostazioni fornite. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
