# Pruna P-Video-2 Testo in video

Genera un video da un prompt testuale con il modello P-Video-2 di Pruna. Il prompt descrive la scena, il suo movimento e il suo suono, e il nodo genera una propria colonna sonora oppure prende una clip audio che guida il movimento e diventa la colonna sonora.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello video Pruna da usare. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"p-video-2"` |

### Input di P-Video-2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Descrive il video, il suo movimento e il suo suono. Deve contenere almeno un carattere non di spaziatura, fino a 5000 caratteri (predefinito: vuoto). | STRING | Sì | Fino a 5000 caratteri |
| `model.aspect_ratio` | Rapporto d'aspetto del video di output (predefinito: `"16:9"`). | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.duration` | Durata del video in secondi. `"auto"` lascia che il modello scelga la durata dal prompt. Ignorato quando `model.audio` è connesso: il video segue quindi la durata dell'audio, arrotondata per eccesso al secondo intero, fino a 20 secondi (predefinito: `"5"`). | COMBO | Sì | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `model.resolution` | Risoluzione di output. 720p produce circa 0,9 megapixel (1280x704 in 16:9), 1080p circa 2 megapixel (1920x1088 in 16:9) (predefinito: `"720p"`). | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `model.fps` | Fotogrammi al secondo. 48 fps non è disponibile con la modalità draft a 1080p (predefinito: `"24"`). | COMBO | Sì | `"24"`<br>`"48"` |
| `model.draft` | Rendering più veloce e meno dettagliato, fatturato a una tariffa inferiore rispetto a un rendering standard (predefinito: False). | BOOLEAN | Sì | True/False |
| `model.generate_audio` | Genera una colonna sonora per il video. Ignorato quando `model.audio` è connesso, che diventa invece la colonna sonora (predefinito: True). | BOOLEAN | Sì | True/False |
| `model.enhance_prompt` | Riscrive il prompt con maggiori dettagli prima della generazione; i prompt brevi ne hanno bisogno. Disattivalo per riprodurre esattamente un risultato con lo stesso seed (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.audio` | Audio che guida il movimento e diventa la colonna sonora. Durata minima di 1 secondo; l'audio più lungo di 20 secondi viene troncato. Imposta la durata del video anziché `model.duration`. | AUDIO | No | - |
| `model.seed` | Seed per la generazione. Lo stesso seed riproduce esattamente un risultato solo quando `model.enhance_prompt` è disattivato (predefinito: 42). | INT | Sì | 0 to 2147483647 |

**Note:**

- `model.prompt` è obbligatorio e limitato a 5000 caratteri.
- La modalità draft a 1080p non può essere combinata con 48 fps: il nodo genera un errore, quindi disattiva la modalità draft oppure usa 24 fps.
- L'audio connesso deve durare almeno 1 secondo; tutto ciò che supera i 20 secondi viene ignorato.
- Con `model.audio` connesso, l'audio imposta la durata del video, quindi `model.duration` e `model.generate_audio` non hanno effetto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video generato con la sua colonna sonora. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `bb7bacf2591618220c72525c1e32382174abe3a55069720adbc84fc1d8081718`
