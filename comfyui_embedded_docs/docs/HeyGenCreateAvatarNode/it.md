# Crea Avatar HeyGen

Crea un avatar HeyGen riutilizzabile da una foto di una persona o da un prompt testuale che descrive un personaggio da generare. Il `avatar_id` risultante può essere usato con il nodo HeyGen Avatar Video e dovrebbe essere salvato per riutilizzare l'avatar nei flussi di lavoro futuri.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `source` | Genera un nuovo personaggio da un prompt testuale oppure crea l'avatar da una foto collegata di una persona. | DYNAMIC_COMBO | Sì | `"prompt"`<br>`"photo"` |

### Input per prompt

Disponibile quando `source` è impostato su `"prompt"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione dell'avatar da generare (fino a 1000 caratteri). Deve contenere almeno 1 carattere non di spaziatura. Predefinito: stringa vuota. | STRING | Sì | da 1 a 1000 caratteri |

### Input per foto

Disponibile quando `source` è impostato su `"photo"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `identity_photo` | Foto della persona da trasformare in un avatar. Ridimensionata automaticamente se più grande di 2K. | IMAGE | Sì | Immagine singola |

### Input di riferimento

Disponibile quando `source` è impostato su `"prompt"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega fino a 3 immagini (`ref_image_1`...`ref_image_3`) che guidano l'aspetto generato. Le immagini vengono ridimensionate automaticamente se più grandi di 2K. | IMAGE | No | da 0 a 3 immagini |

**Nota:** Il parametro `source` alterna tra due modalità mutuamente esclusive. In modalità `"prompt"`, `prompt` è obbligatorio e si possono collegare facoltativamente fino a 3 immagini di riferimento. In modalità `"photo"`, `identity_photo` è obbligatorio. Le foto e le immagini di riferimento vengono ridimensionate automaticamente quando sono più grandi di 2K; più di 3 immagini di riferimento non vengono accettate.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `avatar_id` | ID aspetto avatar. Passalo a `custom_avatar_id` di HeyGen Avatar Video; salvalo per riutilizzare l'avatar in seguito. | STRING |
| `preview` | Immagine di anteprima dell'avatar generato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/it.md)

---
**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`
