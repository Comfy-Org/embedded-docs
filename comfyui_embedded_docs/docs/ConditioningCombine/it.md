# ConditioningCombine

Questo nodo combina due input di condizionamento in un unico output, fondendone efficacemente le informazioni. Le due condizioni vengono combinate tramite concatenazione di liste.

## Input

| Nome parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning_1` | Il primo input di condizionamento da combinare. Ha pari importanza rispetto a `conditioning_2` nel processo di combinazione. | `CONDITIONING` |
| `conditioning_2` | Il secondo input di condizionamento da combinare. Ha pari importanza rispetto a `conditioning_1` nel processo di combinazione. | `CONDITIONING` |

## Output

| Nome parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | Il risultato della combinazione di `conditioning_1` e `conditioning_2`, che racchiude le informazioni unite. | `CONDITIONING` |

## Scenari di utilizzo

Confronta i due gruppi seguenti: il lato sinistro utilizza il nodo ConditioningCombine, mentre il lato destro mostra l'output normale.

![Confronto](./asset/compare.jpg)

In questo esempio, le due condizioni usate in `Conditioning Combine` hanno importanza equivalente. Pertanto, puoi usare codifiche di testo diverse per stile dell'immagine, caratteristiche del soggetto, ecc., consentendo di restituire in modo più completo le caratteristiche del prompt. Il secondo prompt utilizza il prompt completo combinato, ma la comprensione semantica può codificare condizioni completamente diverse.

Utilizzando questo nodo, puoi ottenere:

- Unione di testo di base: collega gli output di due nodi `CLIP Text Encode` alle due porte di input di `Conditioning Combine`
- Combinazione complessa di prompt: combina prompt positivi e negativi, oppure codifica separatamente descrizioni principali e descrizioni di stile prima di unirle
- Combinazione a catena di condizioni: è possibile usare più nodi `Conditioning Combine` in serie per ottenere una combinazione graduale di più condizioni

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/it.md)
