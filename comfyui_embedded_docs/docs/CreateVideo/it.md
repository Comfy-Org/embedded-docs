# Crea Video

Il nodo Create Video combina una sequenza di immagini in un video. È possibile impostare la velocità di riproduzione in fotogrammi al secondo, aggiungere facoltativamente l'audio e scegliere il formato di compressione, la profondità di bit e lo spazio colore del video risultante.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | Le immagini da cui creare un video. | IMAGE | Sì | - |
| `fps` | I fotogrammi al secondo per la velocità di riproduzione del video (predefinito: 30.0). | FLOAT | Sì | 1.0 - 120.0 |
| `audio` | L'audio da aggiungere al video. | AUDIO | No | - |
| `bit_depth` | Auto usa 8 bit per sRGB e 10 bit per HDR e HDR PQ. Le scelte esplicite 8 bit e 10 bit sono indipendenti dallo spazio colore. (predefinito: "auto") | COMBO | No | `"auto"`<br>8<br>10 |
| `color_space` | Spazio colore delle immagini di input. HDR seleziona BT.2020/HLG e HDR PQ seleziona BT.2020/PQ. (predefinito: "sRGB") | COMBO | No | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `codec` | Codifica facoltativamente il video immediatamente. None mantiene le immagini in forma di tensore; Auto usa H.264. (predefinito: "none") | COMBO | No | `"none"`<br>Opzioni di codec video disponibili dall'elenco dei codec video (ad es. `"auto"` e altri codec supportati) |

Nota: quando `bit_depth` è impostato su `"auto"`, il nodo usa automaticamente 10 bit per gli spazi colore HDR e HDR PQ, e 8 bit per sRGB.

Nota: il parametro `codec` è un'opzione avanzata. Quando viene lasciato su `"none"`, l'output rimane in forma di tensore; selezionando qualsiasi altro codec, il video viene codificato immediatamente.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il video generato contenente le immagini di input e l'audio facoltativo. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/it.md)

---
**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`
