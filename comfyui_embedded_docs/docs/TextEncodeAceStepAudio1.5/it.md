# TextEncodeAceStepAudio1.5

Il nodo TextEncodeAceStepAudio1.5 prepara metadati testuali e relativi all'audio per l'uso con il modello AceStepAudio 1.5. Riceve tag descrittivi, testo del brano e parametri musicali, quindi utilizza un modello CLIP per convertirli in un formato di condizionamento adatto alla generazione audio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per tokenizzare e codificare il testo di input. | CLIP | Sì | N/A |
| `tags` | Tag descrittivi per l'audio, come genere, atmosfera o strumenti. Supporta input multilinea e prompt dinamici. | STRING | Sì | N/A |
| `lyrics` | Il testo del brano per la traccia audio. Supporta input multilinea e prompt dinamici. | STRING | Sì | N/A |
| `seed` | Un valore di seed casuale per una generazione riproducibile. Ha un widget control_after_generate. Predefinito: 0. | INT | No | 0 to 18446744073709551615 |
| `bpm` | I battiti per minuto (BPM) per l'audio generato. Predefinito: 120. | INT | No | 10 to 300 |
| `duration` | La durata desiderata dell'audio in secondi. Predefinito: 120.0. | FLOAT | No | 0.0 to 2000.0 |
| `timesignature` | L'indicazione di tempo musicale. | COMBO | No | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | La lingua del testo di input. Predefinito: "en". | COMBO | No | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | La tonalità e la scala musicale (maggiore o minore). | COMBO | No | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | Abilita il LLM che genera i codici audio. Può essere lento, ma aumenterà la qualità dell'audio generato. Disattivalo se stai fornendo al modello un riferimento audio. Predefinito: True. | BOOLEAN | No | N/A |
| `cfg_scale` | La scala di guida senza classificatore. Valori più alti fanno sì che l'output segua più fedelmente il prompt. Predefinito: 2.0. | FLOAT | No | 0.0 to 100.0 |
| `temperature` | Una temperatura di campionamento. Valori più bassi rendono l'output più deterministico. Predefinito: 0.85. | FLOAT | No | 0.0 to 2.0 |
| `top_p` | La probabilità di campionamento nucleus (top-p). Predefinito: 0.9. | FLOAT | No | 0.0 to 2000.0 |
| `top_k` | Il numero di token con probabilità più alta da considerare (top-k). Predefinito: 0. | INT | No | 0 to 100 |
| `min_p` | La soglia di probabilità minima per il campionamento dei token (min-p). Predefinito: 0.000. | FLOAT | No | 0.0 to 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento, che contengono il testo codificato e i parametri audio per il modello AceStepAudio 1.5. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/it.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
