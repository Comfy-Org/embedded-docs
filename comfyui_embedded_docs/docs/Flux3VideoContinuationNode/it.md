# Flux 3 Continuazione Video

Questo nodo continua una clip video esistente con FLUX 3: la nuova clip prosegue dai fotogrammi finali del video fornito. Carica la clip di origine, invia il prompt e le impostazioni al servizio di generazione e restituisce il video di continuazione risultante quando è pronto.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | La clip da continuare. Le clip con area superiore a 3840x2160 pixel vengono ridimensionate verso il basso per adattarsi. | VIDEO | Sì | Singola clip video |
| `prompt` | Cosa deve mostrare la continuazione; il prompt viene interpretato ed espanso prima della generazione. (predefinito: "") | STRING | Sì | Testo non vuoto (minimo 1 carattere) |
| `aspect_ratio` | Rapporto d'aspetto dell'output. 'auto' ne seleziona uno dal prompt e dagli input. (predefinito: "auto") | COMBO | Sì | "auto" (predefinito)<br>Più opzioni predefinite |
| `duration` | Durata della clip in secondi. 'auto' adatta la durata al contenuto. (predefinito: "auto") | COMBO | Sì | "auto" (predefinito)<br>Valori numerici in secondi |
| `resolution` | Risoluzione dell'output. (predefinito: "720p") | COMBO | Sì | "720p" (predefinito)<br>"1080p"<br>"1440p"<br>"2160p" |
| `generate_audio` | Genera audio sincronizzato (ambiente, parlato, effetti). Disattivato produce un video senza traccia audio. (predefinito: true) | BOOLEAN | Sì | true<br>false |
| `safety_tolerance` | Tolleranza di moderazione, 0 è la più rigorosa. Le richieste che inviano immagini o video sono limitate a 2 indipendentemente da quanto impostato qui. (parametro avanzato, predefinito: 2) | INT | Sì | 0 - 4 (massimo effettivo: 2 per richieste video) |
| `seed` | Seed per determinare se il nodo deve rieseguirsi; FLUX 3 sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. (predefinito: 42) | INT | Sì | 0 - 4294967295 (0xFFFFFFFF) |

### Note

- `prompt` deve contenere almeno un carattere, altrimenti la generazione fallisce. Sebbene il campo abbia come valore predefinito una stringa vuota, per eseguire il nodo è necessario un prompt non vuoto.
- `safety_tolerance` accetta qualsiasi valore da 0 a 4, ma poiché questo nodo invia un video all'API, la tolleranza effettiva è limitata a 2 indipendentemente dal valore selezionato.
- Quando `duration` è impostato su un numero, viene convertito in un numero intero di secondi. Il valore speciale "auto" consente al servizio di adattare la durata al contenuto.
- Gli elenchi esatti delle opzioni per `aspect_ratio`, `duration` e `resolution` sono definiti internamente dal nodo. `resolution` offre "720p" (predefinito), "1080p", "1440p" e "2160p". Il prezzo viene calcolato in base a `resolution` e `duration` selezionati: "720p" viene addebitato a $0.5863 al secondo, "1080p" a $0.7579, "1440p" a $0.9295 e "2160p" a $1.3585.
- `seed` controlla solo se il nodo viene rieseguito; non viene inviato al servizio di generazione.
- I campi di autenticazione e identificazione del nodo (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) sono nascosti e gestiti automaticamente dalla piattaforma.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | La clip di continuazione generata da FLUX 3, che prosegue dalla fine del video di origine. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/it.md)

---
**Source fingerprint (SHA-256):** `112004aa664617ce23adba425705327898a1f7632c8d3e8fa4f9ae3e7620776b`
