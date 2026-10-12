# ImageCompositor

Dieser Node kombiniert mehrere Bildebenen zu einem einzelnen zusammengesetzten Bild. Er nimmt einen mit dem Add Layer-Node erstellten Ebenenstapel entgegen und wendet optional gespeicherte Kompositionseinstellungen aus dem Compositor-Editor an, wobei die Ebenen entsprechend ihrer Platzierung, Größe, Drehung, Deckkraft und ihrem Mischmodus zusammengefügt werden. Eine gespeicherte Komposition, die zu den aktuellen Eingaben passt, hat Vorrang; andernfalls setzt der Node die Komposition aus den Ebeneneigenschaften zusammen und markiert den gespeicherten Status als veraltet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `layers` | Ebenenstapel, der zusammengesetzt werden soll; erstellen Sie ihn mit Add Layer. Elemente werden nach z_index gestapelt, Batch-Frames innerhalb eines Elements werden zu aufeinanderfolgenden Ebenen erweitert, und Platzierung, Deckkraft und Mischmodus des Elements definieren die anfängliche Komposition. Ohne eine explizite Dokument-Leinwand entspricht die Größe der bestmöglichen maximalen Ausdehnung der platzierten Ebenen. Eine gespeicherte Komposition, die zu den aktuellen Eingaben passt, hat Vorrang. | LAYERS | Ja | Maximal 50 Ebenen |
| `compositor` | Vom Compositor-Editor gespeicherte geschichtete Komposition. | COMPOSITOR | Nein | Keine |

**Hinweise zu Einschränkungen:**

- Der Ebenenstapel unterstützt maximal 50 erweiterte Ebenen; bei mehr wird ein Fehler ausgelöst.
- Derzeit werden nur Raster-Ebenenelemente unterstützt; andere Elementtypen führen zu einem Fehler.
- Die Dokumentversion von `layers` muss 1 sein; andere Versionen führen zu einem Fehler.
- Der gespeicherte `compositor`-Status wird nur dann wiedergegeben, wenn seine aufgezeichneten Eingabe-Fingerabdrücke mit dem aktuellen Ebenenstapel übereinstimmen. Wenn sie nicht übereinstimmen, fällt der Node auf die Komposition anhand der Ebeneneigenschaften zurück und markiert den gespeicherten Status als veraltet.
- Die Ebenendeckkraft wird auf den Bereich 0.0 bis 1.0 begrenzt.
- Die horizontale und vertikale Platzierung der Ebene (`x`, `y`) wird auf die maximale Auflösungsgrenze begrenzt.
- Die Ebenenbreite und -höhe fallen auf die natürliche Bildgröße zurück, wenn sie auf null oder kleiner gesetzt sind, und werden auf die maximale Auflösungsgrenze begrenzt.
- Die Größe der zusammengesetzten Leinwand darf die maximale Auflösungsgrenze nicht überschreiten.
- Wenn keine Ebenen bereitgestellt werden, wird ein 64x64-Platzhalterbild zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Zusammengesetztes Bild. Enthält einen Alphakanal, wenn die Komposition transparente Bereiche hat (z. B. ausgeblendeter Hintergrund), andernfalls reines RGB. | IMAGE |
| `MASK` | Transparenz der Komposition (1 = vollständig transparent). Alle Werte null, wenn die Komposition undurchsichtig ist. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/de.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
