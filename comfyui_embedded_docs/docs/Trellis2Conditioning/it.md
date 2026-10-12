# Condizionamento Trellis2

Trellis2Conditioning converte un'immagine di input in dati di condizionamento per il modello TRELLIS.2. Utilizza un modello CLIP vision per codificare l'immagine in due insiemi di feature (alle scale 512 e 1024) e li impacchetta come coppia di condizionamento positiva, creando anche una coppia di condizionamento negativa riempita di zeri, corrispondente, che funge da riferimento vuoto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_vision_model` | Il modello CLIP vision utilizzato per codificare l'immagine in feature di condizionamento. | CLIP_VISION | Sì | Qualsiasi modello CLIP vision disponibile |
| `image` | Immagine preprocessata da ImageCropToMask (pad_factor=1.0 per TRELLIS.2). | IMAGE | Sì | Qualsiasi immagine |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Condizionamento contenente le feature dell'immagine codificate alle scale 512 e 1024, utilizzato come condizionamento positivo per il modello TRELLIS.2. | CONDITIONING |
| `negative` | Condizionamento riempito di zeri con la stessa forma del condizionamento positivo, utilizzato come riferimento negativo vuoto. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
