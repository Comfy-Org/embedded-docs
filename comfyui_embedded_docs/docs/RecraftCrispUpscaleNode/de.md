# Recraft Crisp Bild-Upscale

Dieser Node skaliert ein Bild synchron mit dem Tool „crisp upscale“ hoch. Er verbessert ein gegebenes Rasterbild, indem er dessen Auflösung erhöht, wodurch das Bild schärfer und sauberer wird. Wenn ein Stapel von Bildern bereitgestellt wird, wird jedes Bild unabhängig verarbeitet und die hochskalierten Ergebnisse werden als Stapel zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das Eingabebild, das hochskaliert werden soll. Akzeptiert einen Stapel von Bildern; jedes Bild wird unabhängig verarbeitet. | IMAGE | Ja | — |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `image` | Das hochskalierte Bild mit verbesserter Auflösung und Klarheit. Gibt einen Stapel von Bildern zurück, wenn ein Stapel als Eingabe bereitgestellt wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
