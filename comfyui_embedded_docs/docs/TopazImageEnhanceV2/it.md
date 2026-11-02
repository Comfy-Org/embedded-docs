# Topaz Image Enhance

Topaz Image Enhance applica upscaling e miglioramento delle immagini secondo gli standard del settore a una singola immagine di input utilizzando i modelli Topaz. Invia l'immagine all'API Topaz, la elabora con il modello selezionato e restituisce il risultato migliorato. È possibile scegliere tra quattro modelli: Reimagine, Bloom 2, Wonder 3.5 e Wonder 4.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input da migliorare. È supportata una sola immagine di input. | IMAGE | Sì | Immagine singola |
| `model` | Il modello di miglioramento Topaz da utilizzare. Il modello selezionato determina quali impostazioni specifiche del modello vengono visualizzate. | DYNAMIC_COMBO | Sì | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"`<br>`"Wonder 4"` |
| `output_width` | Un valore pari a zero indica il calcolo automatico (di solito sarà la dimensione originale o verrà scalata proporzionalmente a `output_height` se specificato). Wonder 3.5 e Wonder 4 supportano fattori di upscaling da 1x a 6x, Bloom 2 da 1x a 12x. Bloom 2, Wonder 3.5 e Wonder 4 mantengono sempre le proporzioni dell'input: se entrambe le dimensioni sono impostate e il loro rapporto è diverso, prevale l'upscaling maggiore e l'output (e il prezzo) è più grande della dimensione richiesta. (predefinito: 0) | INT | No | 0 a 32000 |
| `output_height` | Un valore pari a zero indica di restituire la stessa altezza dell'originale o una scala proporzionale a `output_width` se specificato. Wonder 3.5 e Wonder 4 supportano fattori di upscaling da 1x a 6x, Bloom 2 da 1x a 12x. Bloom 2, Wonder 3.5 e Wonder 4 mantengono sempre le proporzioni dell'input: se entrambe le dimensioni sono impostate e il loro rapporto è diverso, prevale l'upscaling maggiore e l'output (e il prezzo) è più grande della dimensione richiesta. (predefinito: 0) | INT | No | 0 a 32000 |

### Input di Reimagine

Queste impostazioni si applicano quando `model` è impostato su `"Reimagine"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale opzionale per guidare l'upscaling creativo. (predefinito: "") | STRING | Sì | Qualsiasi testo |
| `creativity` | Livello di creatività per il miglioramento. (predefinito: 3) | INT | Sì | 1 a 9 |
| `subject_detection` | Modalità di rilevamento del soggetto (avanzata). | COMBO | Sì | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Migliora i volti (se presenti) durante l'elaborazione. (predefinito: True) | BOOLEAN | Sì | true<br>false |
| `face_enhancement_creativity` | Imposta il livello di creatività per il miglioramento dei volti. (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1.0 |
| `face_enhancement_strength` | Controlla quanto sono nitidi i volti migliorati rispetto allo sfondo. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `face_preservation` | Preserva l'identità facciale dei soggetti. (predefinito: True) | BOOLEAN | Sì | true<br>false |
| `color_preservation` | Preserva i colori originali. (predefinito: True) | BOOLEAN | Sì | true<br>false |
| `crop_to_fill` | Per impostazione predefinita, l'immagine viene adattata con bande nere quando le proporzioni dell'output differiscono. Abilita per ritagliare l'immagine in modo che riempia le dimensioni dell'output. (predefinito: False) | BOOLEAN | Sì | true<br>false |

### Input di Bloom 2

Queste impostazioni si applicano quando `model` è impostato su `"Bloom 2"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale opzionale per la generazione. Lasciare vuoto per generare automaticamente un prompt dall'immagine di input. (predefinito: "") | STRING | Sì | Qualsiasi testo |
| `creativity` | 1 è un miglioramento contenuto, 9 è una reinterpretazione marcata con dettagli generati ex novo. (predefinito: 3) | INT | Sì | 1 a 9 |
| `seed` | Seme per una generazione riproducibile. (predefinito: 2) | INT | Sì | 1 a 2000 |
| `color_preservation` | Preserva i colori originali. (predefinito: True) | BOOLEAN | Sì | true<br>false |
| `grain` | Aggiunge grana all'immagine di output. (predefinito: False) | BOOLEAN | Sì | true<br>false |
| `grain_model` | Modello di grana da utilizzare. Viene ignorato se la grana è disabilitata. | COMBO | Sì | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Forza dell'effetto grana. Viene ignorato se la grana è disabilitata. (predefinito: 0.5) | FLOAT | Sì | 0.0 a 1.0 |
| `grain_size` | Dimensione delle particelle di grana. Viene ignorato se la grana è disabilitata. (predefinito: 1.0) | FLOAT | Sì | 1.0 a 5.0 |
| `grain_density` | Intensità dell'effetto grana. Viene ignorato se la grana è disabilitata. (predefinito: 0.5) | FLOAT | Sì | 0.0 a 1.0 |

### Input di Wonder 3.5

Queste impostazioni si applicano quando `model` è impostato su `"Wonder 3.5"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Livello di miglioramento per diverse condizioni di input. (predefinito: "high") | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Aggiunge grana all'immagine di output. (predefinito: False) | BOOLEAN | Sì | true<br>false |
| `grain_model` | Modello di grana da utilizzare. Viene ignorato se la grana è disabilitata. | COMBO | Sì | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Forza dell'effetto grana. Viene ignorato se la grana è disabilitata. (predefinito: 0.5) | FLOAT | Sì | 0.0 a 1.0 |
| `grain_size` | Dimensione delle particelle di grana. Viene ignorato se la grana è disabilitata. (predefinito: 1.0) | FLOAT | Sì | 1.0 a 5.0 |
| `grain_density` | Intensità dell'effetto grana. Viene ignorato se la grana è disabilitata. (predefinito: 0.5) | FLOAT | Sì | 0.0 a 1.0 |

**Nota:** È supportata una sola immagine di input; il nodo genera un errore se il batch di input contiene più di un'immagine. Le impostazioni della grana (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) vengono ignorate a meno che `grain` non sia abilitato. Per Bloom 2, lasciare `prompt` vuoto genera automaticamente un prompt dall'immagine di input. Wonder 4 espone solo gli input comuni. L'output è limitato a 179 megapixel e a 32000 pixel per lato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine migliorata e ingrandita restituita dall'API Topaz. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/it.md)

---
**Source fingerprint (SHA-256):** `dd109d31ea4ab7928058414c3a62ae3829f879354ebdce329b599aacb9804d1b`
