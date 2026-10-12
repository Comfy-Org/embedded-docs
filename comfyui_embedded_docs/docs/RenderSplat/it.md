# RenderSplat

Renderizza un gaussian splat come immagine utilizzando un rasterizzatore EWA anisotropico con splat ellittici orientati, antialiasing e rendering front-to-back ordinato per profondità. La camera proviene da un input camera_info, oppure puoi lasciarlo vuoto per inquadrare automaticamente lo splat. Imposta frames maggiore di 1 per un batch di immagini a giostra da fornire a un nodo Video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `splat` | I dati gaussian splat da renderizzare | SPLAT | Sì | - |
| `width` | Larghezza dell'immagine di output (predefinito: 1024) | INT | Sì | 64 a 2048 (passo: 8) |
| `height` | Altezza dell'immagine di output (predefinito: 1024) | INT | Sì | 64 a 2048 (passo: 8) |
| `frames` | Numero di frame da renderizzare. -1, 0 o 1 producono una singola immagine fissa. Valori maggiori di 1 creano un'animazione a giostra in cui la camera orbita per un giro completo di 360 gradi. Valori negativi orbitano nella direzione opposta (predefinito: 1) | INT | Sì | -240 a 240 |
| `splat_scale` | Moltiplicatore sull'impronta proiettata di ciascuno splat. Valori più bassi producono punti più nitidi, valori più alti producono superfici più morbide e piene (predefinito: 1.0) | FLOAT | Sì | 0.1 a 5.0 (passo: 0.05) |
| `sharpen` | Controlla la nitidezza degli splat sovrapposti. Un valore di 1.0 fornisce una fusione fisicamente corretta. Valori superiori a 1.0 orientano ciascun pixel verso il suo splat dominante (più vicino) per una texture più nitida senza restringere gli splat o aprire spazi vuoti (predefinito: 2.0) | FLOAT | Sì | 1.0 a 8.0 (passo: 0.5) |
| `headlight_shading` | Ombreggiatura diffusa da una luce nella posizione della camera, utilizzando le normali dei surfel degli splat. Scurisce le superfici che si allontanano dalla vista per rivelare forma e curvatura. 0 dà albedo piatto, 1 dà l'ombreggiatura più forte (predefinito: 0.0) | FLOAT | Sì | 0.0 a 3.0 (passo: 0.05) |
| `opacity_threshold` | Elimina le gaussiane con opacità inferiore a questa soglia, il che rimuove i floaters tenui (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `render_style` | Cosa mostra l'immagine di output. Le opzioni sono: color (rendering a colori completi), clay (ombreggiato con albedo neutro), depth (gli oggetti vicini appaiono luminosi), normal (mappa di normali OpenGL) (predefinito: "color") | COMBO | Sì | "color"<br>"clay"<br>"depth"<br>"normal" |
| `background` | Colore di sfondo solido per il rendering (predefinito: #000000) | COLOR | Sì | - |
| `bg_image` | Pannello di sfondo opzionale compositato dietro lo splat. Sovrascrive il colore di sfondo solido. Ridimensionato alla dimensione del rendering. Un batch di immagini viene utilizzato per frame, una singola immagine viene utilizzata per tutti i frame. Funziona solo con gli stili di rendering color e clay | IMAGE | No | - |
| `camera_info` | Camera da cui renderizzare. Può provenire da un nodo Load3D, Preview3D o Create Camera Info. Se vuoto, lo splat viene inquadrato automaticamente da una vista predefinita di 3/4 | CAMERA_3D | No | - |

## Output

| Nome Output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine renderizzata del gaussian splat | IMAGE |
| `mask` | La maschera alfa dello splat renderizzato | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/it.md)

---
**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`
