# Mirelo Video to SFX

Genera effetti sonori che seguono un video con Mirelo SFX. La clip viene caricata, il modello segue l'azione sullo schermo e restituisce un mix di effetti sonori, oltre a una traccia voce separata con il dialogo estratto dalla colonna sonora. Usalo per aggiungere foley, ambienti sonori e impatti a clip silenziose o parzialmente silenziose.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da usare. Selezionando un modello vengono mostrati i parametri specifici: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech` e `seed`. | DYNAMIC_COMBO | Sì | `"sfx-2.0"` |
| `video` | Il video per cui generare il suono. Il suono viene generato per l'intera clip, da 1 a 600 secondi. | VIDEO | Sì | Da 1 a 600 secondi |
| `audio` | Traccia di dialogo da usare al posto della colonna sonora del video per `preserve_speech` e per l'output `speech`. Lasciala non connessa per usare il suono incorporato nel video. | AUDIO | No | - |
| `prompt` | Come dovrebbe essere il suono. Può essere lasciato vuoto (predefinito: vuoto) perché il modello descrive il video stesso e non sempre segue il prompt. Massimo 2000 caratteri. | STRING | Sì | Fino a 2000 caratteri |
| `negative_prompt` | Suoni da evitare, come breve elenco separato da virgole. Può essere lasciato vuoto (predefinito: vuoto). Massimo 1000 caratteri. | STRING | Sì | Fino a 1000 caratteri |
| `preserve_speech` | Mantieni il dialogo mixato sotto il suono generato. Se disattivato, restituisce solo effetti sonori. (predefinito: True) | BOOLEAN | Sì | false<br>true |
| `seed` | Il seed per la richiesta. I risultati non sono deterministici, quindi lo stesso seed non ripete una clip. (predefinito: 42) | INT | Sì | 0 a 4294967295 |

Il nodo si interrompe con un errore quando la clip dura meno di 1 secondo o più di 600 secondi. Una traccia `audio` connessa definisce il dialogo che `preserve_speech` mantiene e che l'output `speech` separa; senza di essa, il dialogo proviene dalla colonna sonora del video.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | Il mix di effetti sonori per la clip, con il dialogo mixato sotto quando `preserve_speech` è attivo. | AUDIO |
| `speech` | Il dialogo separato dalla colonna sonora. Silenzioso, con la stessa frequenza di campionamento di `audio`, quando non viene rilevato parlato o la separazione del parlato non restituisce nulla. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/it.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`
