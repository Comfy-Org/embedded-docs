# Kling 3.0 Omni Da Immagine a Video

Questo nodo utilizza il modello Kling AI per generare un video basato su un prompt testuale e fino a sette immagini di riferimento. Consente di controllare il rapporto d'aspetto, la durata e la risoluzione del video e, facoltativamente, di usare storyboard o generare audio. Il nodo invia la richiesta a un'API esterna e restituisce il video generato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Il modello Kling specifico da usare per la generazione video (predefinito: `"kling-v3-omni"`). | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto del video. Può includere sia descrizioni positive sia negative. Viene ignorato quando gli storyboard sono abilitati. Segnaposto come `@image` o `@video` (facoltativamente numerati) vengono convertiti automaticamente nel formato compatibile con l'API. Deve contenere tra 1 e 2500 caratteri (può essere vuoto quando gli storyboard sono abilitati). | STRING | Sì | Da 1 a 2500 caratteri (da 0 a 2500 quando gli storyboard sono abilitati) |
| `aspect_ratio` | Il rapporto d'aspetto desiderato per il video generato. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durata del video in secondi, regolata con un cursore (predefinito: 5). | INT | Sì | Da 3 a 15 |
| `reference_images` | Fino a 7 immagini di riferimento. Ogni immagine deve essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1. | IMAGE | Sì | Da 1 a 7 immagini |
| `resolution` | La risoluzione di output del video (predefinito: `"1080p"`). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie di segmenti video con prompt e durate individuali. Supportato solo per `kling-v3-omni`. Quando è abilitato, il `prompt` globale viene ignorato e la durata totale di tutti i segmenti storyboard deve essere uguale alla `duration` globale (predefinito: `"disabled"`). | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Genera l'audio per il video. Supportato solo per `kling-v3-omni` (predefinito: false). | BOOLEAN | No | `true`<br>`false` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | No | Da 0 a 2147483647 |

### Input degli storyboard

Quando `storyboards` è abilitato, per ogni segmento storyboard selezionato compaiono i seguenti input. N va da 1 fino al numero selezionato di storyboard.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `storyboard_N_prompt` | Prompt per il segmento storyboard N. Massimo 512 caratteri. | STRING | Sì | Da 1 a 512 caratteri |
| `storyboard_N_duration` | Durata per il segmento storyboard N in secondi (predefinito: 4). | INT | Sì | Da 1 a 15 |

**Nota:** L'input `reference_images` accetta un massimo di 7 immagini. Se ne vengono fornite di più, il nodo genera un errore. Per ogni immagine vengono validate le dimensioni minime (300x300 pixel) e il rapporto d'aspetto (tra 1:2.5 e 2.5:1).

**Vincoli specifici del modello:**
- `kling-video-o1` non supporta durate superiori a 10 secondi.
- `kling-video-o1` non supporta la generazione audio.
- `kling-video-o1` non supporta la risoluzione 4k.
- `kling-video-o1` non supporta gli storyboard.

**Vincolo storyboard:** La durata totale di tutti i segmenti storyboard deve essere uguale al valore globale di `duration`. Se la somma non corrisponde, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
