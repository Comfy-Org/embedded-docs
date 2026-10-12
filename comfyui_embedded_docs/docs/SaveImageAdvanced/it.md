# Salva Immagine (Avanzato)

Il nodo **Save Image (Advanced)** salva le immagini di input nella directory di output di ComfyUI con controllo avanzato su formato file, profondità di bit e spazio colore. Supporta il salvataggio in file PNG, EXR o AVIF (inclusi AVIF animati) e può incorporare i metadati del workflow nei file salvati.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Le immagini da salvare. | IMAGE | Sì | - |
| `filename_prefix` | Il prefisso per il file da salvare. Può includere token di formattazione come `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`. (predefinito: "ComfyUI") | STRING | Sì | - |
| `format` | Il formato file in cui salvare l'immagine. Selezionando un formato vengono visualizzate opzioni aggiuntive per quel formato. | DYNAMIC_COMBO | Sì | `"png"`<br>`"exr"`<br>`"avif"` |

### Input PNG

Queste opzioni compaiono quando `format` è impostato su `"png"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondità di bit per il file PNG salvato. (predefinito: "8-bit") | COMBO | Sì (condizionale) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Spazio colore del tensore di input. Per il formato PNG è disponibile solo sRGB. (predefinito: "sRGB") | COMBO | Sì (condizionale) | `"sRGB"` |

### Input EXR

Queste opzioni compaiono quando `format` è impostato su `"exr"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondità di bit per il file EXR salvato. (predefinito: "16-bit float") | COMBO | Sì (condizionale) | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | Spazio colore del tensore di input. L'EXR viene sempre scritto come scene-linear nel gamut corrispondente.<br>`"sRGB"` — l'input è Rec.709 codificato sRGB; viene applicata la EOTF sRGB inversa.<br>`"HDR"` — l'input è Rec.2020 (BT.2100) codificato HLG; viene applicata la OETF HLG inversa per ottenere luce scene-linear.<br>`"linear"` — l'input è già scene-linear (primari Rec.709); viene scritto senza modifiche. Usare questa opzione per output di renderer/compositor. (predefinito: "sRGB") | COMBO | Sì (condizionale) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### Input AVIF

Queste opzioni compaiono quando `format` è impostato su `"avif"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondità di bit per il file AVIF salvato. Auto usa YUV420 a 8 bit per sRGB e YUV420 a 10 bit per HDR. (predefinito: "auto") | COMBO | Sì (condizionale) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Spazio colore delle immagini di input. HDR seleziona BT.2020/HLG e HDR PQ seleziona BT.2020/PQ. (predefinito: "sRGB") | COMBO | Sì (condizionale) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Valori più bassi producono una qualità più alta e file più grandi. (predefinito: 18) | INT | Sì (condizionale) | 1 to 63 |
| `save_mode` | La modalità di salvataggio per il file AVIF. `"still images"` salva ogni immagine del batch come file di immagine fissa separato; `"animated"` salva l'intero batch come un singolo file AVIF animato e mostra `fps` e `loop_count`. (predefinito: "still images") | DYNAMIC_COMBO | Sì (condizionale) | `"still images"`<br>`"animated"` |

### Opzioni per AVIF animato

Queste opzioni compaiono quando `save_mode` è impostato su `"animated"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `fps` | La frequenza dei fotogrammi dell'animazione. (predefinito: 6.0) | FLOAT | Sì (condizionale) | 0.01 to 1000.0 |
| `loop_count` | Numero di volte in cui ripetere l'animazione. 0 ripete all'infinito. (predefinito: 0) | INT | Sì (condizionale) | 0 to 1000 |

**Note sulle dipendenze dei parametri:**
- I parametri specifici del formato (`bit_depth`, `input_color_space` e, per AVIF, anche `crf` e `save_mode`) sono disponibili solo quando è selezionato un `format` specifico.
- Per il formato PNG sono disponibili solo le profondità di bit "8-bit" e "16-bit" e solo lo spazio colore "sRGB".
- Per il formato EXR sono disponibili entrambe le profondità di bit "16-bit float" e "32-bit float", con spazi colore "sRGB", "HDR" o "linear". "16-bit float" è l'impostazione predefinita e produce file più piccoli.
- Per il formato AVIF, `fps` e `loop_count` sono disponibili solo quando `save_mode` è impostato su `"animated"`.
- Le immagini PNG ed EXR devono avere 1 (scala di grigi), 3 (RGB) o 4 (RGBA) canali; altri numeri di canali non sono supportati e generano un errore.
- AVIF supporta solo immagini in scala di grigi a 1 canale e RGB a 3 canali; le immagini RGBA (alpha) non sono supportate e generano un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Le immagini di input, passate invariate. L'output UI del nodo fornisce un elenco di risultati delle immagini salvate, ciascuno contenente il nome file, la sottocartella e il tipo ("output"). Per AVIF animato con più di un'immagine, l'output UI include anche un flag `animated`. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `a0f7fccb3b25ffa814bf5d2a970c41fd4114368eb9a9998880b1108a272a41bb`
