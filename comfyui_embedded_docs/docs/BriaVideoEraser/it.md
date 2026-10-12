# BriaVideoEraser

Cancella ciò che una maschera per fotogramma copre da un video con Bria e riempie lo spazio vuoto. La maschera deve essere bianca su ciò che deve essere rimosso e nera altrove. Bria accetta clip di al massimo 5,1 secondi a 20-30 fotogrammi al secondo con dimensioni in pixel pari; l'audio viene mantenuto per impostazione predefinita. La clip restituita può essere più corta di alcuni fotogrammi rispetto all'input.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Clip da cui cancellare. | VIDEO | Sì | - |
| `mask` | Una maschera per ogni fotogramma del video, bianca dove si trova l'oggetto da cancellare. Fornire una maschera o un video maschera, non entrambi. | MASK | No | - |
| `mask_video` | Un video maschera già codificato con le stesse dimensioni e lo stesso numero di fotogrammi del video. Fornire una maschera o un video maschera, non entrambi. | VIDEO | No | - |
| `preserve_audio` | Mantiene la traccia audio dell'input. Predefinito: true. | BOOLEAN | No | `true`<br>`false` |

**Note sui vincoli:**

- Esattamente uno tra `mask` e `mask_video` deve essere collegato. Viene generato un errore se nessuno dei due è fornito, o se entrambi sono forniti.
- Il video deve essere lungo al massimo 5,1 secondi e deve essere a 20-30 fotogrammi al secondo. Ritemporizzare la clip con Get Video Components e Create Video se necessario.
- Il video deve avere dimensioni in pixel pari (larghezza e altezza divisibili per 2). Ritagliarlo o ridimensionarlo prima, altrimenti.
- Quando si utilizza `mask`, deve contenere un fotogramma di maschera per ogni fotogramma del video, e le sue proporzioni devono corrispondere a quelle del video. Le maschere vengono binarizzate al 50%: le aree dipinte con opacità inferiore alla metà vengono ignorate, e una maschera vuota genera un errore. Se la risoluzione della maschera differisce da quella del video, viene ridimensionata alle dimensioni del video.
- Quando si utilizza `mask_video`, deve avere le stesse dimensioni e lo stesso numero di fotogrammi del video.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | La clip modificata con le aree mascherate cancellate e gli spazi vuoti riempiti. L'output può essere più corto di alcuni fotogrammi rispetto alla clip di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/it.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
