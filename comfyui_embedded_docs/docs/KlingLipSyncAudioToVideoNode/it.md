# KlingLipSyncAudioToVideoNode

Il nodo Kling Lip Sync Audio to Video sincronizza i movimenti della bocca in un file video per farli corrispondere al contenuto audio di un file audio. Questo nodo analizza i pattern vocali nell'audio e regola i movimenti facciali nel video per creare un lip-sync realistico. Il processo richiede sia un video contenente un volto distinto sia un file audio con parti vocali chiaramente distinguibili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Il file video contenente un volto da sincronizzare labialmente | VIDEO | Sì | - |
| `audio` | Il file audio contenente la voce da sincronizzare con il video | AUDIO | Sì | - |
| `voice_language` | La lingua della voce nel file audio (predefinito: "en") | COMBO | Sì | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Vincoli importanti:**

- Il file audio non deve essere più grande di 5 MB
- Il file video non deve essere più grande di 100 MB
- Le dimensioni del video devono essere comprese tra 720px e 1920px in altezza/larghezza
- La durata del video deve essere compresa tra 2 e 10 secondi
- L'audio deve contenere parti vocali chiaramente distinguibili
- Il video deve contenere un volto distinto

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il video elaborato con i movimenti della bocca sincronizzati | VIDEO |
| `video_id` | L'identificatore univoco del video elaborato | STRING |
| `duration` | La durata del video elaborato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
