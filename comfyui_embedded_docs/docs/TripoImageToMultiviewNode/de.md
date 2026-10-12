# TripoImageToMultiviewNode

Erzeugt Vorder-, linke, Rück- und rechte Ansichten des Motivs aus einem einzelnen Eingabebild mithilfe der Tripo-API. Das Bild wird hochgeladen, eine Multiview-Generierungsaufgabe gestartet und abgefragt, bis sie abgeschlossen ist, und die vier resultierenden Ansichten werden zusammen mit der Task-ID zurückgegeben. Dies ist eine kostenpflichtige Aufgabe, die mit etwa 0,10 USD abgerechnet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Quellbild des Motivs, aus dem Tripo die Vorder-, linken, Rück- und rechten Ansichten erzeugt. Es wird nur ein Bild für die Anfrage verwendet, selbst wenn ein Batch übergeben wird. | IMAGE | Ja | Einzelbild |

Hinweis: Der Node ruft die Cloud-API von Tripo auf und wartet, bis die Generierungsaufgabe abgeschlossen ist. Eine typische Aufgabe dauert etwa 25 Sekunden. Die Authentifizierung wird automatisch über die versteckten Eingaben des Nodes abgewickelt, sodass kein Tripo-API-Schlüssel im Workflow angegeben werden muss. Der Node benötigt alle vier Ansichts-URLs in der Tripo-Antwort (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); wenn eine Ansicht fehlt, schlägt die Ausführung mit einem Fehler fehl.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|----------|
| `multiview task_id` | Die von Tripo für die Multiview-Bildgenerierungsanfrage zurückgegebene Task-ID. Sie kann verwendet werden, um auf die abgeschlossene Aufgabe zu verweisen, beispielsweise beim Verfeinern der Ansichten mit Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `front` | Die erzeugte Vorderansicht des Motivs. | IMAGE |
| `left` | Die erzeugte linke Seitenansicht des Motivs. | IMAGE |
| `back` | Die erzeugte Rückansicht des Motivs. | IMAGE |
| `right` | Die erzeugte rechte Seitenansicht des Motivs. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/de.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
