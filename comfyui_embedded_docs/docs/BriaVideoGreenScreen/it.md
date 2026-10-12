# Bria Video Green Screen

Questo nodo sostituisce lo sfondo di un video con uno schermo chroma-key a tinta unita utilizzando l'API Bria. Elabora il video di input e restituisce un nuovo video in cui lo sfondo originale è stato rimosso e sostituito con un colore a schermo verde o blu uniforme.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il video di input da elaborare | VIDEO | Sì | File video |
| `green_shade` | Tonalità chroma-key a tinta unita applicata dietro il primo piano: `broadcast_green` (#00B140), `chroma_green` (#00FF00) o `blue_screen` (#0000FF). | COMBO | Sì | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | 0 to 2147483647 |

**Nota:** Il video di input non deve superare i 60 secondi di durata.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video elaborato (MP4, H.264) con lo sfondo originale sostituito dalla tonalità chroma-key selezionata | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/it.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
