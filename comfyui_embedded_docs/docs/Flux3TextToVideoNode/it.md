# Flux 3 Da Testo a Video

Genera un video con audio sincronizzato da un prompt testuale usando FLUX 3. Il nodo invia il prompt al servizio FLUX 3, attende il completamento della generazione e restituisce la clip video finita.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Cosa vuoi ottenere, in linguaggio naturale; il prompt viene interpretato ed espanso prima della generazione. Descrivi separatamente suono ambientale, musica e parlato per un audio stratificato. (default: "") | STRING | Sì | Multiline text |
| `aspect_ratio` | Proporzioni dell'output. 'auto' ne sceglie una dal prompt e dagli input. (default: "auto") | COMBO | Sì | Multiple options available, including `"auto"` |
| `duration` | Durata della clip in secondi. 'auto' adatta la durata al contenuto. (default: "auto") | COMBO | Sì | Multiple options available, including `"auto"` |
| `resolution` | Risoluzione dell'output. (default: "720p") | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `generate_audio` | Genera audio sincronizzato (ambientale, parlato, effetti). Disattivato produce un video senza traccia audio. (default: True) | BOOLEAN | Sì | True<br>False |
| `safety_tolerance` | Tolleranza di moderazione, 0 è la più severa. Le richieste che inviano immagini o video sono limitate a 2 indipendentemente da quanto impostato qui. (default: 2) | INT | Sì | 0 to 4 |
| `seed` | Seed per determinare se il nodo deve rieseguirsi; FLUX 3 sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. (default: 42) | INT | Sì | 0 to 4294967295 |

Nota: `safety_tolerance` è un input avanzato. L'input `seed` include i controlli Control After Generate nell'interfaccia utente. Il prezzo visualizzato si basa su `resolution` e `duration`: HD (720p) viene addebitato a $0.2431 al secondo e FHD (1080p) a $0.4147 al secondo. Quando viene scelta una durata fissa, viene mostrato il costo totale stimato per la clip; quando `duration` è "auto", viene mostrata la tariffa al secondo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | La clip video generata, con audio sincronizzato quando `generate_audio` è abilitato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
