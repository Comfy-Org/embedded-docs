# LoadImageSetNode

Il nodo LoadImageSetNode carica più immagini dalla directory di input per l'elaborazione in batch e per scopi di addestramento. Supporta vari formati di immagine e può ridimensionare opzionalmente le immagini utilizzando metodi diversi. Questo nodo elabora tutte le immagini selezionate come un batch e le restituisce come un singolo tensore.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Seleziona più immagini dalla directory di input. Supporta i formati PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF e TIFF. Consente la selezione in batch di immagini. | IMAGE | Sì | Più file immagine |
| `resize_method` | Metodo opzionale per ridimensionare le immagini caricate (predefinito: "None"). Scegli "None" per mantenere le dimensioni originali, "Stretch" per forzare il ridimensionamento, "Crop" per mantenere le proporzioni ritagliando, oppure "Pad" per mantenere le proporzioni aggiungendo padding. | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | Un tensore contenente tutte le immagini caricate come batch per ulteriori elaborazioni. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/it.md)

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
