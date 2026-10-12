# Tripo: Da immagine a viste multiple

Genera le viste frontale, sinistra, posteriore e destra del soggetto a partire da una singola immagine di input utilizzando l'API Tripo. L'immagine viene caricata, viene avviata un'attività di generazione multiview che viene monitorata fino al completamento, e le quattro viste risultanti vengono restituite insieme all'ID dell'attività. Questa è un'attività a pagamento dal costo di circa 0,10 USD.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di origine del soggetto da cui Tripo genera le viste frontale, sinistra, posteriore e destra. Per la richiesta viene utilizzata una sola immagine, anche se viene fornito un batch. | IMAGE | Sì | Immagine singola |

Nota: il nodo chiama l'API cloud di Tripo e attende il completamento dell'attività di generazione. Un'attività tipica richiede circa 25 secondi. L'autenticazione è gestita automaticamente tramite gli input nascosti del nodo, quindi non è necessario fornire alcuna chiave API Tripo nel workflow. Il nodo richiede tutti e quattro gli URL delle viste nella risposta di Tripo (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); se manca una qualsiasi vista, l'esecuzione fallisce con un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `multiview task_id` | L'identificatore dell'attività restituito da Tripo per la richiesta di generazione dell'immagine multiview. Può essere utilizzato per fare riferimento all'attività completata, ad esempio quando si rifiniscono le viste con Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `front` | La vista frontale generata del soggetto. | IMAGE |
| `left` | La vista laterale sinistra generata del soggetto. | IMAGE |
| `back` | La vista posteriore generata del soggetto. | IMAGE |
| `right` | La vista laterale destra generata del soggetto. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/it.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
