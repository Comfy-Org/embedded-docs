# VeoVideoGenerationNode

Genera video da prompt testuali utilizzando l'API Veo di Google. Questo nodo può creare video da descrizioni testuali e input immagine opzionali, con controllo su parametri come proporzioni, durata e altro.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione testuale del video (predefinito: vuoto) | STRING | Sì | - |
| `aspect_ratio` | Proporzioni del video di output (predefinito: "16:9") | COMBO | Sì | "16:9"<br>"9:16" |
| `negative_prompt` | Prompt testuale negativo per guidare ciò che si desidera evitare nel video (predefinito: vuoto) | STRING | No | - |
| `duration_seconds` | Durata del video di output in secondi (predefinito: 5) | INT | No | 5-8 |
| `enhance_prompt` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: True). Questo è un parametro avanzato. | BOOLEAN | No | - |
| `person_generation` | Indica se consentire la generazione di persone nel video (predefinito: "ALLOW"). Questo è un parametro avanzato. | COMBO | No | "ALLOW"<br>"BLOCK" |
| `seed` | Seme per la generazione del video (0 per casuale) (predefinito: 0). Questo è un parametro avanzato. | INT | No | 0-4294967295 |
| `image` | Immagine di riferimento opzionale per guidare la generazione del video | IMAGE | No | - |
| `model` | Modello Veo da utilizzare per la generazione del video (predefinito: "veo-2.0-generate-001") | COMBO | No | "veo-2.0-generate-001"<br>"veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" |

**Nota:** Il parametro `generate_audio` è disponibile solo per i modelli Veo 3.0 e Veo 3.1 ed è gestito automaticamente dal nodo in base al modello selezionato. Quando si utilizzano i modelli Veo 3.0 o Veo 3.1, il parametro `enhance_prompt` viene forzato a True.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/it.md)

---
**Source fingerprint (SHA-256):** `055569f26c7e8f074371239f12f307ca86ce2aa5fd17ca55dd951b34f71fa559`
