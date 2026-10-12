# LoadImageDataSetFromFolder

Dieser Node lädt mehrere Bilder aus einem ausgewählten Unterordner innerhalb des Haupteingabeverzeichnisses von ComfyUI und gibt sie als Liste zurück. Er durchsucht den ausgewählten Ordner nach Bilddateien im Format PNG, JPG, JPEG oder WEBP, was ihn für die Stapelverarbeitung oder das Vorbereiten von Bilddatensätzen nützlich macht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `folder` | Der Ordner, aus dem Bilder geladen werden sollen. Die Optionen sind die Unterordner, die im Haupteingabeverzeichnis von ComfyUI vorhanden sind. | COMBO | Ja | Mehrere Optionen verfügbar |

Hinweis: Der ausgewählte Ordner muss ein Unterordner des Haupteingabeverzeichnisses von ComfyUI sein; jeder Wert, der außerhalb davon aufgelöst wird (zum Beispiel unter Verwendung von `..`, absoluten Pfaden, Laufwerksbuchstaben oder Symlinks), wird abgelehnt. Es werden nur Dateien mit den Erweiterungen .png, .jpg, .jpeg oder .webp geladen; bei der Prüfung der Erweiterung wird die Groß-/Kleinschreibung nicht unterschieden. Geladene Bilder werden in RGB konvertiert und auf den Bereich 0-1 skaliert. Wenn der ausgewählte Ordner keine gültigen Bilddateien enthält, löst der Node einen Fehler aus. Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Liste der geladenen Bilder. Der Node lädt alle gültigen Bilddateien (PNG, JPG, JPEG, WEBP), die im ausgewählten Ordner gefunden werden. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/de.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
