# Bildfarben normalisieren

Dieser Node normalisiert die Farben eines Eingabebildes, indem er seine Pixelwerte basierend auf einem angegebenen Mittelwert und einer angegebenen Standardabweichung anpasst. Von jedem Pixel wird der Mittelwert subtrahiert und anschließend durch die Standardabweichung dividiert. Dies ist ein üblicher Schritt, um Bilddaten vor der weiteren Verarbeitung zu standardisieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das normalisiert werden soll. | IMAGE | Ja | - |
| `mean` | Mittelwert für die Normalisierung (Standard: 0.5). | FLOAT | Nein | 0.0 - 1.0 |
| `std` | Standardabweichung für die Normalisierung (Standard: 0.5). | FLOAT | Nein | 0.001 - 1.0 |

Die Parameter `mean` und `std` steuern die auf das Eingabebild angewendete Normalisierung. Der Standardwert für beide Parameter ist 0.5.

Hinweis: Wenn das Eingabebild einen Alpha-Kanal (Transparenz) besitzt, wird dieser Kanal nicht normalisiert. Er wird unverändert in die Ausgabe kopiert, da Alpha Transparenz und nicht Farbe speichert.

Hinweis: Der Node funktioniert mit jeder Batch-Größe, sodass mehrere Bilder gleichzeitig verarbeitet werden können.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das resultierende Bild, nachdem der Normalisierungsprozess angewendet wurde. Die Pixelwerte werden unter Verwendung des angegebenen Mittelwerts und der angegebenen Standardabweichung angepasst, und der Alpha-Kanal (falls vorhanden) bleibt erhalten. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/de.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
