# Kling Motion Control

Il nodo Kling Motion Control genera un video applicando il movimento, le espressioni e i movimenti di camera da un video di riferimento a un personaggio definito da un'immagine di riferimento e da un prompt testuale. Consente di controllare se l'orientamento finale del personaggio proviene dal video di riferimento o dall'immagine di riferimento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt` | Una descrizione testuale del video desiderato. La lunghezza massima è di 2500 caratteri. | STRING | Sì | N/A |
| `reference_image` | Un'immagine del personaggio da animare. Le dimensioni minime sono 340x340 pixel. Le proporzioni devono essere comprese tra 1:2,5 e 2,5:1. | IMAGE | Sì | N/A |
| `reference_video` | Video di riferimento del movimento usato per guidare movimento/espressione. I limiti di durata dipendono dall'impostazione `character_orientation`. Le dimensioni minime sono 340x340 pixel, le dimensioni massime sono 3850x3850 pixel. | VIDEO | Sì | N/A |
| `keep_original_sound` | Determina se l'audio originale del video di riferimento viene mantenuto nell'output. Il valore predefinito è `True`. | BOOLEAN | No | N/A |
| `character_orientation` | Controlla da dove provengono l'orientamento e la direzione del personaggio. `"video"`: i movimenti, le espressioni, i movimenti di camera e l'orientamento seguono il video di riferimento del movimento (altri dettagli tramite prompt). `"image"`: i movimenti e le espressioni seguono comunque il video di riferimento del movimento, ma l'orientamento del personaggio corrisponde all'immagine di riferimento (camera/altri dettagli tramite prompt). | COMBO | No | `"video"`<br>`"image"` |
| `mode` | La modalità di generazione da usare. | COMBO | No | `"pro"`<br>`"std"` |
| `model` | La versione del modello Kling da usare. Il valore predefinito è `"kling-v2-6"`. | COMBO | No | `"kling-v3"`<br>`"kling-v2-6"` |

**Vincoli:**

- La durata di `reference_video` deve essere compresa tra 3 e 30 secondi quando `character_orientation` è impostato su `"video"`.
- La durata di `reference_video` deve essere compresa tra 3 e 10 secondi quando `character_orientation` è impostato su `"image"`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato con il personaggio che esegue il movimento dal video di riferimento. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/it.md)

---
**Source fingerprint (SHA-256):** `a61e55fabe53f4e13fa993c3d891db40024709ea4fb6b16b5716d893b2bd23b5`
