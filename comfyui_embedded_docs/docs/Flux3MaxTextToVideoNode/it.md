# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video genera un video con audio sincronizzato a partire da un prompt testuale. Il prompt viene interpretato ed espanso da FLUX 3 Max prima del rendering, il nodo attende il completamento del rendering e il clip completato viene restituito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Cosa deve mostrare il clip, in linguaggio naturale. Descrivi separatamente suono ambientale, musica e parlato per un audio a più livelli (predefinito: vuoto). | STRING | Sì | Testo multiriga |
| `aspect_ratio` | Proporzioni di uscita. `"auto"` corrisponde a 16:9 per i prompt testuali (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Durata del clip in secondi (predefinito: `"5"`). | COMBO | Sì | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Risoluzione di uscita (predefinito: `"720p"`). | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Quanto il modello ragiona ed espande il prompt prima di generare. `"high"` richiede più tempo; il prezzo è lo stesso (predefinito: `"high"`). | COMBO | Sì | `"low"`<br>`"high"` |
| `generate_audio` | Genera audio sincronizzato. Se disattivato, produce un video senza traccia audio (predefinito: true). | BOOLEAN | Sì | `true`<br>`false` |
| `seed` | Seed che controlla se il nodo viene rieseguito. I risultati non sono deterministici indipendentemente da questo valore (predefinito: 42). | INT | Sì | 0 a 2147483646 |

Nota: `prompt` deve contenere almeno un carattere. Il prezzo visualizzato si basa su `resolution` e `duration`: 720p viene addebitato a $0.060775 al secondo e 1080p a $0.103675 al secondo fino al 7 novembre 2026, e a $0.2431 e $0.4147 al secondo dopo tale data. Il costo totale stimato per il clip viene mostrato nell'interfaccia utente.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il clip video generato, con audio sincronizzato quando `generate_audio` è abilitato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
