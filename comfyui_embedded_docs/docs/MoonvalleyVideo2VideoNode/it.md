# MoonvalleyVideo2VideoNode

Il nodo Moonvalley Marey Video to Video trasforma un video di input in un nuovo video basato su una descrizione testuale. Utilizza l'API Moonvalley per generare video che corrispondono al tuo prompt preservando le caratteristiche di movimento o posa del video originale. Puoi controllare lo stile e il contenuto del video di output tramite prompt testuali e vari parametri di generazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrive il video da generare (input multilinea) | STRING | Sì | - |
| `negative_prompt` | Testo del prompt negativo (predefinito: elenco esteso di descrittori negativi) | STRING | No | - |
| `seed` | Valore del seed casuale (predefinito: 9) | INT | Sì | 0 to 4294967295 |
| `video` | Il video di riferimento utilizzato per generare il video di output. Deve durare almeno 5 secondi. I video più lunghi di 5 s verranno tagliati automaticamente. È supportato solo il formato MP4. | VIDEO | Sì | - |
| `control_type` | Selezione del tipo di controllo (predefinito: "Motion Transfer") | COMBO | No | "Motion Transfer"<br>"Pose Transfer" |
| `motion_intensity` | Usato solo se `control_type` è "Motion Transfer" (predefinito: 100) | INT | No | 0 to 100 |
| `steps` | Numero di passaggi di inferenza (predefinito: 33) | INT | Sì | 1 to 100 |

**Nota:** Il parametro `motion_intensity` viene applicato solo quando `control_type` è impostato su "Motion Transfer". Quando si utilizza "Pose Transfer", questo parametro viene ignorato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il video generato in output | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/it.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
