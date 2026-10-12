# Kling 3.0 Omni Da Video a Video

Questo nodo utilizza il modello Kling AI per generare un nuovo video basato su un video di input e immagini di riferimento opzionali. Fornisci un prompt testuale che descrive il contenuto desiderato e il nodo trasforma il video di riferimento di conseguenza. Può anche incorporare fino a quattro immagini di riferimento aggiuntive per guidare lo stile e il contenuto dell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Il modello Kling specifico da utilizzare per la generazione del video (predefinito: "kling-v3-omni"). | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto del video. Può includere sia descrizioni positive che negative. | STRING | Sì | N/A |
| `aspect_ratio` | Il rapporto d'aspetto desiderato per il video generato. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durata del video generato in secondi (predefinito: 3). | INT | Sì | 3 to 10 |
| `reference_video` | Video da utilizzare come riferimento. | VIDEO | Sì | N/A |
| `keep_original_sound` | Determina se l'audio del video di riferimento viene mantenuto nell'output (predefinito: True). | BOOLEAN | Sì | N/A |
| `reference_images` | Fino a 4 immagini di riferimento aggiuntive. | IMAGE | No | N/A |
| `resolution` | La risoluzione per il video generato (predefinito: "1080p"). | COMBO | No | `"1080p"`<br>`"720p"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed (predefinito: 0). | INT | No | 0 to 2147483647 |

**Vincoli sui parametri:**

* Il `prompt` deve essere lungo tra 1 e 2500 caratteri.
* Il `reference_video` deve avere una durata compresa tra 3,0 e 10,05 secondi.
* Il `reference_video` deve avere dimensioni comprese tra 720x720 e 2160x2160 pixel.
* È possibile fornire un massimo di 4 `reference_images`. Ogni immagine deve essere di almeno 300x300 pixel e avere un rapporto d'aspetto compreso tra 1:2.5 e 2.5:1.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il video appena generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `3dc2e3d153ddd9e6da705b764c51b4a859d66464b893fdebb0689d2ad5e870c7`
