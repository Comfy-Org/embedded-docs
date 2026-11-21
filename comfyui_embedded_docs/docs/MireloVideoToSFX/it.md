# Da video a SFX di Mirelo

Genera effetti sonori che seguono un video con Mirelo SFX. La clip viene caricata, il modello segue l'azione sullo schermo e restituisce un mix di effetti sonori, oltre a una traccia voce separata con il dialogo estratto dalla colonna sonora. Usalo per aggiungere foley, ambienze e impatti a clip mute o parzialmente mute.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da usare. Selezionando un modello vengono mostrati i parametri specifici: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech`, `seed` e `auto_downscale`. | DYNAMIC_COMBO | Sì | `"sfx-2.0"` |
| `video` | Il video per cui generare il suono. Il suono viene generato per l'intera clip, da 1 a 600 secondi. | VIDEO | Sì | 1 a 600 secondi |
| `audio` | Traccia di dialogo da usare al posto della colonna sonora del video per `preserve_speech` e per l'output `speech`. Lasciala non connessa per usare il suono incorporato nel video. | AUDIO | No | - |
| `prompt` | Come dovrebbe essere il suono. Può essere lasciato vuoto (predefinito: vuoto) perché il modello descrive da sé il video e non segue sempre il prompt. Massimo 2000 caratteri. | STRING | Sì | Fino a 2000 caratteri |
| `negative_prompt` | Suoni da evitare, come breve elenco separato da virgole. Può essere lasciato vuoto (predefinito: vuoto). Massimo 1000 caratteri. | STRING | Sì | Fino a 1000 caratteri |
| `preserve_speech` | Mantieni il dialogo mescolato sotto il suono generato. Se disattivato, restituisce solo effetti sonori. (predefinito: True) | BOOLEAN | Sì | false<br>true |
| `seed` | Il seed per la richiesta. I risultati sono non deterministici, quindi lo stesso seed non riproduce una clip identica. (predefinito: 42) | INT | Sì | 0 a 4294967295 |
| `auto_downscale` | Ridimensiona verso il basso una clip il cui lato più corto supera i 2160 pixel prima del caricamento, mantenendone le proporzioni; le clip più piccole non vengono modificate (predefinito: True). | BOOLEAN | No | `True`<br>`False` |

Il nodo si interrompe con un errore quando la clip dura meno di 1 secondo o più di 600 secondi. Una traccia `audio` connessa imposta il dialogo che `preserve_speech` mantiene e che l'output `speech` separa; senza di essa, il dialogo proviene dalla colonna sonora del video.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | Il mix di effetti sonori per la clip, con il dialogo mescolato sotto quando `preserve_speech` è attivo. | AUDIO |
| `speech` | Il dialogo separato dalla colonna sonora. Silenzioso, con la stessa frequenza di campionamento di `audio`, quando non viene rilevata voce o la separazione vocale non restituisce nulla. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/it.md)

---
**Source fingerprint (SHA-256):** `a6bd749a902d5ca2e91863fd6c4df57cdeba7fd9505026053b72b29d588587fa`
