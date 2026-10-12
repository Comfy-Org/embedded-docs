# Mescola Coppie Video-Testo

Questo nodo mescola casualmente l'ordine delle coppie video-testo in un elenco, mantenendo ogni video abbinato al testo corrispondente. Prende due elenchi di uguale lunghezza e applica a entrambi la stessa permutazione casuale, garantendo che gli abbinamenti originali siano preservati dopo il mescolamento. Un valore di seed controlla l'ordine di mescolamento, così i risultati possono essere riprodotti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `videos` | Elenco di video da mescolare. | VIDEO | Sì | Elenco di elementi video |
| `texts` | Elenco di testi da mescolare (le didascalie abbinate ai video). | STRING | Sì | Elenco di stringhe di testo |
| `seed` | Seed casuale che determina l'ordine di mescolamento (predefinito: 0). | INT | Sì | da 0 a 18446744073709551615 |

Nota: `videos` e `texts` devono avere la stessa lunghezza, poiché il nodo abbina ogni video al testo nella stessa posizione e preserva tali abbinamenti durante il mescolamento. Internamente, il valore `seed` viene ridotto usando il modulo 4294967295 (2^32 - 1) prima che venga generato l'ordine casuale, quindi valori di seed molto grandi possono produrre lo stesso mescolamento di valori più piccoli.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `videos` | Video mescolati nel nuovo ordine casuale. | VIDEO |
| `texts` | Testi mescolati nello stesso nuovo ordine dei video. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/it.md)

---
**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`
