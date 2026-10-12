# LoopProgress

LoopProgress ist ein Hilfsknoten, der nur für die Entwicklung gedacht ist und den Fortschritt einer Schleife an die ComfyUI-Server-Schnittstelle meldet. Bei jeder Ausführung sendet er den Text "Iteration X / Y" an den Client und gibt die aktuelle Iterationsposition unverändert zurück, wodurch er inline in einer Schleife platziert werden kann, ohne den Datenfluss zu verändern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `start_id` | Bezeichner der Prompt-/Schleifeninstanz, zu der die Fortschrittsmeldung gehört. Das erste Element der übergebenen Liste wird verwendet, um den Fortschrittstext an die korrekte laufende Ausführung zu leiten. | STRING | Ja | - |
| `position` | Die aktuelle Iterationsposition (Index). Das erste Element der übergebenen Liste wird in der Fortschrittsmeldung verwendet und außerdem als Ausgabe zurückgegeben. | INT | Ja | - |
| `total` | Die Gesamtzahl der Iterationen. Wird zusammen mit `position` verwendet, um die Fortschrittsmeldung "Iteration X / Y" zu erstellen. | INT | Ja | - |

Hinweis: Dieser Knoten ist mit Listeneingaben (`is_input_list=True`) deklariert und akzeptiert alle Eingaben. Daher wird jeder verbundene Wert als Liste behandelt und nur sein erstes Element gelesen. Der Knoten wird immer ausgeführt (sein Eingabe-Fingerprint ist fest), sodass er bei jedem Schleifendurchlauf erneut ausgeführt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `position` | Die aktuelle Iterationsposition, unverändert vom `position`-Eingang durchgereicht. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/de.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`
