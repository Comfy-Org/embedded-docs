# ByteDanceVideoEnhanceNode

Questo nodo esegue l'upscaling e il ripristino dei video utilizzando ByteDance vCube. Può aumentare la risoluzione fino a 8K, rimuovere artefatti di compressione e rumore, migliorare colore e nitidezza e, facoltativamente, interpolare i fotogrammi per una frequenza dei fotogrammi più elevata. Il video viene caricato sul servizio vCube, elaborato con il preset di miglioramento selezionato e restituito come file video migliorato.

## Input

### Input comuni

Questi input sono sempre visibili.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video da migliorare. La risoluzione di origine deve essere al massimo 2560x1440 (2K); la dimensione di output è impostata dall'input `resolution`. | VIDEO | Sì | Al massimo 2560x1440 (2K) |
| `tool_version` | 'standard' bilancia velocità e qualità con oltre 10 algoritmi di miglioramento. 'professional' utilizza oltre 30 algoritmi per un ripristino di livello cinematografico, richiede circa 3 volte più tempo e costa 10 volte di più. | DYNAMIC_COMBO | Sì | "standard"<br>"professional" |
| `resolution` | Risoluzione di output. Il lato corto viene impostato al livello scelto e il lato lungo segue le proporzioni della sorgente. 'source' mantiene la dimensione della sorgente, 'custom' imposta il lato corto in pixel. Le sorgenti più larghe o più alte di circa 2,2:1 vengono fatturate a un livello di risoluzione superiore. | DYNAMIC_COMBO | Sì | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Frequenza dei fotogrammi di output. Una frequenza superiore a quella della sorgente abilita l'interpolazione dei fotogrammi tramite IA; una inferiore determina la perdita di fotogrammi. 'source' mantiene la frequenza della sorgente, fino a 120 fps. Frequenze superiori a 30 fps costano 2x, superiori a 60 fps 4x. (predefinito: "source") | COMBO | Sì | "source" (predefinito)<br>Frequenze dei fotogrammi numeriche fino a 120 fps |
| `bitrate_level` | Bitrate target del file consegnato, scalato in base alla risoluzione e alla frequenza dei fotogrammi di output. (predefinito: "medium") | COMBO | Sì | "low"<br>"medium"<br>"high" |

### Input standard

Visualizzati quando `tool_version` è impostato su "standard".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `scene` | Preset ottimizzato per il contenuto: 'aigc' per filmati generati dall'IA, 'common' per video generici, 'ugc' per clip compresse da smartphone, 'short_series' per drammi con volti, 'old_film' per filmati d'archivio graffiati o tremolanti. (predefinito: "aigc") | COMBO | Sì | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' applica un miglioramento più nitido; 'natural' riduce l'intensità per un aspetto più morbido e meno nitido. (predefinito: "hd") | COMBO | Sì | "hd"<br>"natural" |

### Input professionali

Visualizzati quando `tool_version` è impostato su "professional".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' applica un miglioramento più nitido; 'natural' riduce l'intensità per un aspetto più morbido e meno nitido. (predefinito: "hd") | COMBO | Sì | "hd"<br>"natural" |

### Input per risoluzione personalizzata

Visualizzati quando `resolution` è impostato su "custom".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `short_side` | Lato corto dell'output in pixel; il lato lungo segue le proporzioni della sorgente. (predefinito: 1080) | INT | Sì | Predefinito 1080; limitato dai valori minimo e massimo del lato corto supportati da vCube |

### Note

- Il video di origine deve essere al massimo 2560x1440 (2K). I video più grandi vengono rifiutati e devono essere ridimensionati prima del miglioramento.
- La durata del video di origine è limitata alla durata massima supportata dal servizio vCube.
- Quando `tool_version` è "standard", sono disponibili sia `scene` sia `enhance_style`. Quando è "professional", è disponibile solo `enhance_style`.
- Quando `resolution` è "custom", il valore `short_side` è obbligatorio. I preset di risoluzione e "source" non usano `short_side`.
- Quando `resolution` è "source" e il lato corto della sorgente è almeno il limite minimo del lato corto, l'output mantiene la risoluzione della sorgente.
- Quando `fps` è "source", la frequenza dei fotogrammi di output corrisponde a quella della sorgente, fino a 120 fps.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-----------|-----------|
| `video` | Il video migliorato, sottoposto a upscaling e ripristinato alla risoluzione e alla frequenza dei fotogrammi richieste. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/it.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
