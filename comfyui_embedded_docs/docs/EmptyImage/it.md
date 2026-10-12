# Immagine Vuota

## Descrizione della funzione

Il nodo EmptyImage viene utilizzato per creare immagini vuote con dimensioni e colori specificati. Può generare immagini con sfondo a tinta unita, comunemente usate come punti di partenza o immagini di sfondo per i flussi di lavoro di elaborazione delle immagini.

## Principio di funzionamento

Proprio come un pittore che prepara una tela bianca prima di iniziare a creare, il nodo EmptyImage ti fornisce una "tela digitale". Puoi specificare le dimensioni della tela (larghezza e altezza), scegliere il colore di base della tela e persino preparare più tele con le stesse specifiche contemporaneamente. Questo nodo è come un negozio intelligente di materiali artistici in grado di creare tele standardizzate che soddisfano perfettamente i tuoi requisiti di dimensioni e colore.

## Input

| Nome parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `width` | Imposta la larghezza dell'immagine generata (in pixel), determinando le dimensioni orizzontali della tela | INT |
| `height` | Imposta l'altezza dell'immagine generata (in pixel), determinando le dimensioni verticali della tela | INT |
| `batch_size` | Il numero di immagini da generare contemporaneamente, usato per la creazione batch di immagini con le stesse specifiche | INT |
| `color` | Il colore di sfondo dell'immagine. È possibile inserire impostazioni di colore esadecimali, che verranno automaticamente convertite in decimale | INT |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il tensore immagine vuota generato, formattato come [batch_size, height, width, 3], contenente i tre canali di colore RGB | IMAGE |

## Valori di riferimento comuni per i colori

Poiché l'input del colore per questo nodo attualmente non è intuitivo, con tutti i valori di colore convertiti in decimale, ecco alcuni valori di colore comuni che possono essere usati direttamente per un'applicazione rapida.

| Nome colore | Valore esadecimale |
|------------|-------------------|
| Nero      | 0x000000         |
| Bianco      | 0xFFFFFF         |
| Rosso    | 0xFF0000         |
| Verde    | 0x00FF00         |
| Blu    | 0x0000FF         |
| Giallo    | 0xFFFF00         |
| Ciano    | 0x00FFFF         |
| Magenta    | 0xFF00FF         |
| Arancione    | 0xFF8000         |
| Viola     | 0x8000FF         |
| Rosa    | 0xFF80C0         |
| Marrone    | 0x8B4513         |
| Grigio scuro  | 0x404040         |
| Grigio chiaro | 0xC0C0C0         |
| Blu navy  | 0x000080         |
| Verde scuro | 0x008000         |
| Rosso scuro   | 0x800000         |
| Oro       | 0xFFD700         |
| Argento       | 0xC0C0C0         |
| Beige      | 0xF5F5DC         |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/it.md)
