# Video laden (aus Ordner)

Lädt einen Datensatz von Videos aus einem ausgewählten Ordner im ComfyUI-Eingabeverzeichnis und gibt sie als Liste von Lazy-Video-Referenzen zurück. Dieser Node lädt einen Datensatz von Videos: Frames werden erst dekodiert, wenn ein anderer Node sie tatsächlich benötigt. Unterstützte Formate sind MP4, AVI, MOV, WEBM, MKV und FLV.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `folder` | Der Ordner, der die Videodateien enthält. | COMBO | Ja | Alle Unterordner, die im ComfyUI-Eingabeverzeichnis verfügbar sind (dynamisch befüllt) |

**Hinweis:** Der ausgewählte Ordner muss ein Unterordner des ComfyUI-Eingabeverzeichnisses sein und mindestens eine unterstützte Videodatei enthalten. Unterstützte Erweiterungen sind MP4, AVI, MOV, WEBM, MKV und FLV. Wenn keine unterstützten Videodateien gefunden werden oder wenn der Ordnerpfad außerhalb des Eingabeverzeichnisses aufgelöst wird, gibt der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `videos` | Eine Liste von Lazy-Video-Referenzen, eine für jede unterstützte Videodatei im ausgewählten Ordner, alphabetisch nach Dateinamen sortiert. Video-Frames werden erst dekodiert, wenn die Ausgabe von einem anderen Node konsumiert wird. | VIDEO (list) |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/de.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
