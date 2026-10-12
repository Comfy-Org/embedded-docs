# Generazione Video da Riferimenti Vidu

Il nodo Vidu Reference Video genera video da più immagini di riferimento e un prompt testuale. Utilizza modelli di IA per creare contenuti video coerenti in base alle immagini e alla descrizione fornite. Il nodo supporta varie impostazioni video, tra cui durata, rapporto d'aspetto, risoluzione e controllo del movimento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Nome del modello per la generazione video (predefinito: "viduq1") | COMBO | Sì | `"viduq1"` |
| `images` | Immagini da usare come riferimenti per generare un video con soggetti coerenti (massimo 7 immagini) | IMAGE | Sì | - |
| `prompt` | Una descrizione testuale per la generazione video | STRING | Sì | - |
| `duration` | Durata del video di output in secondi (predefinito: 5) | INT | No | 5-5 |
| `seed` | Seed per la generazione video (0 per casuale) (predefinito: 0) | INT | No | 0-2147483647 |
| `aspect_ratio` | Il rapporto d'aspetto del video di output | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `resolution` | I valori supportati possono variare in base al modello e alla durata (predefinito: "1080p") | COMBO | No | `"1080p"` |
| `movement_amplitude` | L'ampiezza di movimento degli oggetti nell'inquadratura (predefinito: "auto") | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Vincoli e limitazioni:**

- Il campo `prompt` è obbligatorio e non può essere vuoto
- Massimo 7 immagini consentite come riferimento
- Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1
- Ogni immagine deve avere dimensioni minime di 128x128 pixel
- La durata è fissa a 5 secondi

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato in base alle immagini di riferimento e al prompt | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `087ce07dbf0bdad9dcb1f1487dd95cf1b50d627cc8b1f8a17ff26d74016c2c3e`
