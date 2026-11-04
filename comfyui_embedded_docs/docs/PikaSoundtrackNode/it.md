# Pika Soundtrack

Questo nodo genera una colonna sonora sincronizzata per un video con Pika. L'immagine e la durata vengono mantenute; viene sostituito solo l'audio. Descrivi il suono desiderato oppure lascia vuota l'istruzione per ricavarlo dall'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | La clip per cui creare una colonna sonora. Fino a 10 minuti. | VIDEO | Sì | - |
| `instruction` | Il tipo di audio desiderato: effetti sonori, ambiente, musica o stile. Lasciare vuoto per ricavarlo dall'immagine. Predefinito: "" (stringa vuota). | STRING | Sì | 0 a 10000 caratteri |
| `seed` | Seed per il campionamento. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli:**

* Il video di input deve durare al massimo 10 minuti.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | La clip di input con la colonna sonora generata al posto dell'audio originale. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/it.md)

---
**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`
