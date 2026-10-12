# Pruna P-Video-2 da immagine a video

Anima un'immagine trasformandola in un video con il modello P-Video-2 di Pruna. Il primo fotogramma è obbligatorio e fissa le proporzioni dell'output; un ultimo fotogramma opzionale fornisce al video un punto finale verso cui interpolare. Il prompt descrive come si muove la scena, e il nodo genera la propria colonna sonora oppure prende una clip audio che guida il movimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello video Pruna da usare. Selezionando un modello vengono mostrati i relativi input qui sotto. | DYNAMIC_COMBO | Sì | `"p-video-2"` |

### Input di P-Video-2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.first_frame` | Immagine da cui inizia il video. L'output mantiene le proporzioni di questa immagine. | IMAGE | Sì | - |
| `model.last_frame` | Immagine su cui termina il video. Le sue proporzioni devono essere vicine a quelle del primo fotogramma. | IMAGE | No | - |
| `model.prompt` | Descrive come si muove e suona la scena. Deve contenere almeno un carattere diverso da spazi bianchi, fino a 5000 caratteri (predefinito: vuoto). | STRING | Sì | Fino a 5000 caratteri |
| `model.duration` | Durata del video in secondi. `"auto"` lascia che il modello scelga la durata dal prompt. Ignorato quando `model.audio` è collegato: il video segue quindi la durata dell'audio, arrotondata per eccesso al secondo intero, fino a 20 secondi (predefinito: `"5"`). | COMBO | Sì | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `model.resolution` | Risoluzione di output. 720p produce circa 0,9 megapixel (1280x704 in 16:9), 1080p circa 2 megapixel (1920x1088 in 16:9) (predefinito: `"720p"`). | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `model.fps` | Fotogrammi al secondo. 48 fps non è disponibile con draft a 1080p (predefinito: `"24"`). | COMBO | Sì | `"24"`<br>`"48"` |
| `model.draft` | Render più veloce e meno dettagliato, addebitato a una tariffa inferiore rispetto a un render standard (predefinito: False). | BOOLEAN | Sì | True/False |
| `model.generate_audio` | Genera una colonna sonora per il video. Ignorato quando `model.audio` è collegato, che diventa invece la colonna sonora (predefinito: True). | BOOLEAN | Sì | True/False |
| `model.enhance_prompt` | Riscrive il prompt con maggiori dettagli prima della generazione; i prompt brevi ne hanno bisogno. Disattivalo per riprodurre esattamente un risultato con lo stesso seed (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.audio` | Audio che guida il movimento e diventa la colonna sonora. Deve durare almeno 1 secondo; l'audio più lungo di 20 secondi viene troncato. Imposta la durata del video al posto di `model.duration`. | AUDIO | No | - |
| `model.seed` | Seed per la generazione. Lo stesso seed riproduce esattamente un risultato solo quando `model.enhance_prompt` è disattivato (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

**Note:**

- `model.first_frame` è obbligatorio e fissa le proporzioni dell'output, quindi questo nodo non ha un input per le proporzioni.
- `model.last_frame` è opzionale, ma le sue proporzioni devono essere vicine a quelle del primo fotogramma, altrimenti il nodo genera un errore.
- `model.prompt` è obbligatorio e limitato a 5000 caratteri.
- La modalità draft a 1080p non può essere combinata con 48 fps: il nodo genera un errore, quindi disattiva draft oppure usa 24 fps.
- L'audio collegato deve durare almeno 1 secondo; tutto ciò che supera i 20 secondi viene ignorato.
- Con `model.audio` collegato, l'audio imposta la durata del video, quindi `model.duration` e `model.generate_audio` non hanno effetto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video generato con la relativa colonna sonora. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `da8952e478eee593543fa7ae1aa329ad5bd5078024f905cdba185d18e76db130`
