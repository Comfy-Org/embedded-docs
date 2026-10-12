# Immagine Latent Stratificata Vuota Qwen

Empty Qwen Image Layered Latent prepara la tela vuota su cui dipinge il modello Qwen-Image-Layered. Immaginalo come una pila di fogli da lucido puliti fissati insieme in ordine: il modello riempie il primo foglio con l'immagine completa, e ogni foglio successivo con una parte di quell'immagine. Questo nodo decide quanto sono grandi i fogli e quanti sono. Non disegna nulla da solo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dell'immagine latente da creare. Il valore deve essere divisibile per 16. (predefinito: 640) | INT | Sì | da 16 a MAX_RESOLUTION (passo 16) |
| `height` | L'altezza dell'immagine latente da creare. Il valore deve essere divisibile per 16. (predefinito: 640) | INT | Sì | da 16 a MAX_RESOLUTION (passo 16) |
| `layers` | In quanti livelli separare l'immagine. Un foglio aggiuntivo è sempre riservato all'immagine completa, quindi si ottengono `layers + 1` immagini, non `layers`. Impostalo su 2 e ottieni l'immagine completa più 2 livelli. Impostalo su 0 e ottieni solo l'immagine completa. (predefinito: 3) | INT | Sì | da 0 a MAX_RESOLUTION (passo 1) |
| `batch_size` | Il numero di campioni latenti da generare in un batch. (predefinito: 1) | INT | Sì | da 1 a 4096 |

**Nota:** i parametri `width` e `height` vengono divisi internamente per 8 per determinare le dimensioni spaziali del tensore latente di output.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Un tensore latente riempito di zeri. La sua forma è `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Perché si ottiene un'immagine in più rispetto a quelle richieste

Qwen-Image-Layered non si limita a scomporre un'immagine. Ridipinge anche l'immagine completa, su un foglio dedicato, accanto ai livelli. Ecco perché la pila è sempre più alta di un foglio rispetto al numero di livelli richiesti.

- **La prima immagine è l'immagine completa, non un livello.** È la stessa immagine che hai già, quindi scartala quando vuoi solo i livelli.
- **Sovrapponi di nuovo tutti i livelli uno sull'altro e otterrai di nuovo l'immagine completa.** Se non ricompongono la prima immagine, la separazione non ha funzionato come desideravi, quindi questo è un modo rapido per verificare il risultato.
- **Mantieni i fogli in ordine.** La pila è l'unica registrazione di quale livello sta sopra a quale. Sui fogli stessi non c'è scritto nulla che indichi la loro posizione, quindi riordinare o eliminare immagini significa riordinare o perdere livelli.
- **I livelli vengono prodotti con trasparenza**, quindi possono essere sovrapposti senza che quelli inferiori vengano nascosti dietro uno sfondo opaco.

## Suggerimenti per l'uso

Invia l'output al sampler come faresti con un normale latente vuoto, poi inserisci LatentCutToBatch con `dim` impostato su `t` prima di VAE Decode. È il passaggio che separa la pila in immagini distinte, in ordine, a partire dall'immagine completa.

Inizia con il valore predefinito di 3 livelli. Richiederne di più significa una generazione più lunga e una separazione più fine, e non vale la pena aumentarlo finché non hai visto cosa fa il modello con un numero piccolo.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/it.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
