# Kling 3.0 Omni Da Primo-Ultimo Frame a Video

Questo nodo utilizza il modello Kling AI più recente per generare un video da un fotogramma iniziale, un fotogramma finale opzionale o immagini di riferimento. Può creare un singolo video o uno storyboard multi-inquadratura con prompt e durate individuali per ogni segmento. Il nodo elabora questi input per produrre un video di lunghezza e risoluzione specificate, con generazione audio opzionale.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `model_name` | Il modello Kling AI specifico da utilizzare per la generazione video. | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto del video. Può includere sia descrizioni positive che negative. Ignorato quando gli storyboard sono abilitati. | STRING | Sì | - |
| `duration` | La lunghezza desiderata del video generato in secondi (predefinito: 5). | INT | Sì | 3 to 15 |
| `first_frame` | L'immagine iniziale per la sequenza video. | IMAGE | Sì | - |
| `end_frame` | Un fotogramma finale opzionale per il video. Non può essere utilizzato contemporaneamente a `reference_images`. Non funziona con gli storyboard. | IMAGE | No | - |
| `reference_images` | Fino a 6 immagini di riferimento aggiuntive. | IMAGE | No | - |
| `resolution` | La risoluzione di output per il video generato (predefinito: "1080p"). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie di segmenti video con prompt e durate individuali. Supportato solo per `kling-v3-omni`. | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Genera audio per il video (predefinito: False). Supportato solo per `kling-v3-omni`. | BOOLEAN | No | True / False |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | No | 0 to 2147483647 |

### Input di storyboard

Quando `storyboards` è impostato su un valore diverso da `"disabled"`, i seguenti input vengono aggiunti per ogni segmento selezionato (N varia da 1 al numero selezionato di storyboard):

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `storyboard_N_prompt` | Prompt per il segmento storyboard N. Massimo 512 caratteri. (predefinito: "") | STRING | Sì | - |
| `storyboard_N_duration` | Durata per il segmento storyboard N in secondi (predefinito: 4). | INT | Sì | 1 to 15 |

**Vincoli importanti:**

* L'input `end_frame` non può essere utilizzato contemporaneamente all'input `reference_images`.
* L'input `end_frame` non può essere utilizzato contemporaneamente agli storyboard.
* Il modello `kling-video-o1` non supporta durate superiori a 10 secondi, generazione audio, risoluzione 4k o storyboard.
* Se non fornisci un `end_frame` o delle `reference_images` con il modello `kling-video-o1`, la `duration` può essere impostata solo su 5 o 10 secondi.
* Tutte le immagini di input (`first_frame`, `end_frame` e qualsiasi `reference_images`) devono avere una dimensione minima di 300 pixel sia in larghezza che in altezza.
* Le proporzioni di tutte le immagini di input devono essere comprese tra 1:2.5 e 2.5:1.
* È possibile fornire un massimo di 6 immagini tramite l'input `reference_images`.
* Il testo del `prompt` deve essere lungo tra 1 e 2500 caratteri (0 caratteri consentiti quando gli storyboard sono abilitati).
* Il prompt può fare riferimento alle immagini di input utilizzando i segnaposto `@image`, `@image1`, `@image2`, ecc.; questi vengono automaticamente convertiti nel formato di riferimento immagine compatibile con l'API.
* Quando gli storyboard sono abilitati, la durata totale di tutti i segmenti storyboard deve essere uguale al valore globale di `duration`.
* Ogni prompt storyboard deve essere lungo tra 1 e 512 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
