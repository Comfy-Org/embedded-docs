# KlingDualCharacterVideoEffectNode

Il nodo Kling Dual Character Video Effect crea video con effetti speciali in base alla scena selezionata. Riceve due immagini e posiziona la prima immagine sul lato sinistro e la seconda immagine sul lato destro del video composito. Effetti visivi diversi vengono applicati in base alla scena effetto scelta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image_left` | Immagine sul lato sinistro | IMAGE | Sì | - |
| `image_right` | Immagine sul lato destro | IMAGE | Sì | - |
| `effect_scene` | Il tipo di scena con effetto speciale da applicare alla generazione video | COMBO | Sì | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | Il modello da utilizzare per gli effetti dei personaggi (predefinito: "kling-v1") | COMBO | No | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | La modalità di generazione video (predefinito: "std") | COMBO | No | `"std"`<br>`"pro"` |
| `duration` | La durata del video generato in secondi | COMBO | Sì | `"5"`<br>`"10"` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato con effetti per due personaggi | VIDEO |
| `duration` | Le informazioni sulla durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/it.md)

---
**Source fingerprint (SHA-256):** `314fc23940225eb4559ecc74f333bb23e9a4939bbb884c93341f4d6f6e7b64df`
