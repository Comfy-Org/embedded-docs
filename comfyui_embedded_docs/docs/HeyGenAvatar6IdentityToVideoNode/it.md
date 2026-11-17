# HeyGen Avatar 6 Identity to Video

Genera un video parlato di un avatar HeyGen con Avatar 6. Scegli uno degli aspetti predefiniti che supportano Avatar 6 oppure incolla il tuo ID avatar HeyGen, quindi guidalo con un copione testuale o con il tuo audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Selettore del modello. `"heygen-avatar-6-turbo"` è la versione più economica e veloce; entrambi i modelli accettano gli stessi input e risoluzioni. | COMBO | Sì | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `avatar` | Aspetto avatar da presentare. I 19 aspetti predefiniti che supportano Avatar 6 sono elencati direttamente; `custom avatar` mostra `custom_avatar_id` per un aspetto creato in HeyGen. | DYNAMIC_COMBO | Sì | 19 aspetti predefiniti<br>`custom avatar` |
| `speech` | Guida l'avatar con un copione testuale (sintesi vocale di HeyGen) o con il tuo audio. Nome visualizzato: origine del parlato. | DYNAMIC_COMBO | Sì | `"script"`<br>`"audio"` |
| `resolution` | Risoluzione del video di output. Predefinito: `"1080p"`. | COMBO | Sì | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Proporzioni del video di output. `"auto"` segue il filmato originale dell'aspetto avatar. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Indicazioni facoltative per gesti, espressione, postura e movimento della camera. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `motion_expressiveness` | `"less"` produce gesti meno numerosi e più contenuti. Il prompt di movimento ha la precedenza dove i due si sovrappongono. Predefinito: `"default"`. | COMBO | Sì | `"less"`<br>`"default"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di `custom avatar`

Questi input compaiono quando `avatar` è impostato su `custom avatar`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `custom_avatar_id` | ID dell'aspetto avatar HeyGen che supporta Avatar 6, ad esempio uno creato con HeyGen Create Avatar. Predefinito: stringa vuota. | STRING | Sì | - |

### Input del parlato per `script`

Questi input compaiono quando `speech` è impostato su `"script"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text` | Testo che l'avatar deve pronunciare. Predefinito: stringa vuota. | STRING | Sì | Fino a 5000 caratteri |
| `voice` | Voce per il copione. L'opzione predefinita usa la voce assegnata da HeyGen all'avatar; gli avatar creati con HeyGen Create Avatar non ne hanno una, quindi scegli una voce per loro. | COMBO | Sì | `"(avatar's default voice)"` più l'elenco generale delle voci di HeyGen |
| `custom_voice_id` | ID voce HeyGen facoltativo. Se impostato, sostituisce la voce selezionata sopra. Predefinito: stringa vuota. | STRING | No | - |
| `voice_speed` | Moltiplicatore della velocità del parlato. Predefinito: 1.0. | FLOAT | No | 0.5 a 1.5 (passo 0.05) |

### Input del parlato per `audio`

Questi input compaiono quando `speech` è impostato su `"audio"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Parlato per l'avatar. La durata del video segue l'audio. | AUDIO | Sì | 0.5 secondi a 10 minuti |

**Vincoli e comportamento:**

* `custom avatar` richiede un ID avatar non vuoto, altrimenti il nodo genera un errore.
* Un copione è limitato a 5000 caratteri e l'audio a 10 minuti.
* Il prezzo è per secondo di video di output e dipende dal modello e dalla risoluzione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video parlato generato, scaricato da HeyGen al termine del rendering. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`
