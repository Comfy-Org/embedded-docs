# Sonilo Video in Musica

Genera musica da un video utilizzando il modello AI di Sonilo. Questo nodo analizza il contenuto di un video in input e crea un brano musicale corrispondente. Utilizza un servizio AI esterno per elaborare il video e generare l'audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video di input da cui generare la musica. Durata massima: 6 minuti. | VIDEO | Sì | - |
| `prompt` | Prompt testuale opzionale per guidare la generazione della musica. Lascia vuoto per la migliore qualità: il modello analizzerà completamente il contenuto del video. (predefinito: stringa vuota) | STRING | No | - |
| `seed` | Seed per la riproducibilità. Attualmente ignorato dal servizio Sonilo ma mantenuto per la coerenza del grafo. (predefinito: 0) | INT | No | da 0 a 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | La musica generata come file audio. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/it.md)

---
**Source fingerprint (SHA-256):** `ed118d346add099f41a99635638ecb9aa4026b2210b17628c34cdad6bb919767`
