# Pruna P-Video-2 Pro Avatar

Trasforma un ritratto in un video parlante con Pruna P-Video-2 Pro Avatar. Fai pronunciare uno script tramite sintesi vocale oppure collega il tuo audio e la persona eseguirà il lip-sync.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `immagine` | Ritratto da cui inizia il video. Le proporzioni da 1:2 a 4:1 vengono mantenute; le immagini più estreme, come 1:5, vengono ritagliate a 9:16 o 16:9. | IMAGE | Sì | - |
| `parlato` | Guida il video con uno script di sintesi vocale o con il tuo audio. Selezionando un'opzione vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"script"`<br>`"audio"` |
| `prompt` | Descrive ciò che mostra il video (predefinito: "The person is talking."). Fino a 5000 caratteri. | STRING | Sì | Fino a 5000 caratteri |
| `risoluzione` | Risoluzione di output (predefinito: `"768p"`). 1080p, 2k e 4k eseguono l'upscale del video generato a 768p. | COMBO | Sì | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | Aggiunge al prompt il movimento visibile nel ritratto, come sfondo, luci e movimento del corpo (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | `True`<br>`False` |
| `seme` | Seed per la generazione (predefinito: 42). Lo stesso seed riproduce esattamente un risultato solo quando `enhance_prompt` è disattivato. | INT | Sì | 0 a 2147483647<br>Passo: 1 |

### Input di `"script"`

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `script` | Parole pronunciate dalla persona. La durata del video corrisponde a quella del parlato; il parlato più lungo di 3 minuti viene tagliato a 3 minuti. | STRING | Sì | Qualsiasi testo |
| `voce` | Voce utilizzata per il parlato (predefinito: `"Zephyr (Female)"`). | COMBO | Sì | 30 voci preimpostate |
| `lingua` | Lingua in cui viene pronunciato lo script (predefinito: `"English (US)"`). | COMBO | Sì | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `voice_prompt` | Come viene pronunciato lo script: tono, cadenza, accento, emozione (predefinito: "Say the following."). Non viene letto ad alta voce. | STRING | Sì | Qualsiasi testo |

### Input di `"audio"`

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `speech.audio` | Parlato su cui la persona esegue il lip-sync. La durata del video corrisponde a quella dell'audio. | AUDIO | Sì | Almeno 1 secondo |

**Note:**

- Un output più lungo limita la durata dell'audio: 2k accetta fino a 150 secondi di audio e 4k fino a 60 secondi. Un audio più lungo a queste risoluzioni blocca il nodo con un errore, quindi usa una risoluzione inferiore o una clip più breve.
- Le proporzioni del ritratto determinano la forma dell'output. I ritratti molto alti o molto larghi vengono ritagliati anziché riempiti con padding, quindi mantieni il soggetto lontano dai bordi.
- Con `enhance_prompt` disattivato, il prompt viene usato così com'è scritto; è questo che fa sì che lo stesso seed riproduca esattamente un risultato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video parlante generato dal ritratto. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/it.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
