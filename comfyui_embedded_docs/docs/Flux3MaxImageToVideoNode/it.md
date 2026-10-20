# FLUX 3 Max Image to Video

FLUX 3 Max Image to Video anima da 1 a 10 immagini con FLUX 3 Max. Ogni immagine diventa un fotogramma della clip: un'immagine la apre, due diventano il suo primo e ultimo fotogramma, mentre ulteriori immagini vengono distribuite lungo la clip o fissate agli orari scelti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Come la scena deve muoversi e suonare (predefinito: vuoto). | STRING | Sì | Testo multiriga |
| `keyframes` | Slot espandibile: collega da 1 a 10 immagini chiave nell'ordine di riproduzione, ad es. `image_1`, `image_2` e così via. Ogni immagine diventa un fotogramma della clip. | IMAGE | Sì | Da 1 a 10 immagini |
| `placement` | `"spread across the clip"` colloca la prima immagine all'inizio, l'ultima alla fine e le altre in modo uniforme tra le due; `"at times"` fissa ogni immagine a un secondo scelto (predefinito: `"spread across the clip"`). | DYNAMIC_COMBO | Sì | `"spread across the clip"`<br>`"at times"` |
| `aspect_ratio` | Proporzioni di output. `"auto"` segue la prima immagine chiave (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Durata della clip in secondi (predefinito: `"5"`). | COMBO | Sì | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Risoluzione di output (predefinito: `"720p"`). | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Quanto il modello ragiona sul prompt e lo amplia prima di generare. `"high"` richiede più tempo; il prezzo è lo stesso (predefinito: `"high"`). | COMBO | Sì | `"low"`<br>`"high"` |
| `generate_audio` | Genera audio sincronizzato. Disattivato produce un video senza traccia audio (predefinito: true). | BOOLEAN | Sì | `true`<br>`false` |
| `seed` | Seed che controlla se il nodo viene rieseguito. I risultati non sono deterministici indipendentemente da questo valore (predefinito: 42). | INT | Sì | Da 0 a 2147483646 |

### Input di `at times`

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `times` | Un tempo in secondi per immagine, separato da virgole e crescente, ad es. "0, 2.5, 5". Compare solo quando `placement` è `"at times"`. | STRING | No | Secondi separati da virgola |

Nota: `prompt` deve contenere almeno un carattere. `keyframes` deve contenere almeno un'immagine e non può contenerne più di 10; un input in batch conta una volta per immagine.

Con `placement` impostato su `"spread across the clip"`, una o due immagini vengono inviate come immagine iniziale e un'eventuale immagine finale, mentre tre o più vengono posizionate su fotogrammi chiave distribuiti uniformemente lungo la clip a 24 fps.

Con `placement` impostato su `"at times"`, `times` deve fornire un valore per immagine e tali valori devono essere crescenti, non possono essere negativi e l'ultimo valore temporale non può superare la fine della clip.

Il prezzo visualizzato si basa su `resolution` e `duration`: 720p viene addebitato a $0.060775 al secondo e 1080p a $0.103675 al secondo fino al 7 novembre 2026, e a $0.2431 e $0.4147 al secondo dopo tale data. Il costo totale stimato per la clip è mostrato nell'interfaccia utente.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | La clip video generata, costruita dalle immagini chiave con le proporzioni, la durata, la risoluzione e l'impostazione audio scelte. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `fd8bbd627022f86d3ecb3482530a6c8c37d4225e32db36c35185eac318ed4c75`
