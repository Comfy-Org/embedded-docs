# AddLayer

Der Node „Add Layer“ wandelt ein Eingabebild in eine Ebene um und platziert es auf einer Leinwand, wobei entweder ein neuer Ebenenstapel begonnen oder ein vorhandener erweitert wird. Sie können den Namen, die Position, die Größe, die Rotation, die Deckkraft, den Mischmodus, die Stapelreihenfolge sowie horizontales oder vertikales Spiegeln der Ebene festlegen. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `layers` | Ebenenstapel, an den angehängt werden soll. Nicht verbunden lassen, um einen neuen Stapel zu beginnen. | LAYERS | Nein | — |
| `image` | Ebeneninhalt in seiner nativen Größe. Ein Batch wird zu aufeinanderfolgenden Ebenen erweitert. | IMAGE | Ja | — |
| `mask` | Transparenzmaske für diese Ebene. Maskierte Bereiche (Wert 1) werden transparent und multiplizieren sich mit einem etwaigen Alphakanal, den das Bild bereits enthält. | MASK | Nein | — |
| `name` | Ebenenname, der im Compositor-Editor angezeigt wird. (Standard: "") | STRING | Nein | — |
| `x` | Anfängliche horizontale Platzierung auf der Leinwand. (Standard: 0) | INT | Nein | -MAX_RESOLUTION bis MAX_RESOLUTION |
| `y` | Anfängliche vertikale Platzierung auf der Leinwand. (Standard: 0) | INT | Nein | -MAX_RESOLUTION bis MAX_RESOLUTION |
| `opacity` | Anfängliche Deckkraft der Ebene. (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 (Schritt: 0.01) |
| `blend_mode` | Anfänglicher Mischmodus, angewendet gegen die darunterliegenden Ebenen. Auf der untersten Ebene über dem standardmäßig transparenten Hintergrund erzeugen Nicht-Normal-Modi Transparenz. (Standard: "normal") | COMBO | Nein | Mehrere Optionen verfügbar |
| `rotation` | Anfängliche Rotation in Grad, im Uhrzeigersinn. (Standard: 0.0) | FLOAT | Nein | -360.0 bis 360.0 (Schritt: 1.0) |
| `width` | Anfängliche Anzeigebreite. 0 behält die native Breite des Bildes bei. (Standard: 0) | INT | Nein | 0 bis MAX_RESOLUTION |
| `height` | Anfängliche Anzeigehöhe. 0 behält die native Höhe des Bildes bei. (Standard: 0) | INT | Nein | 0 bis MAX_RESOLUTION |
| `z_index` | Überschreibung der Stapelreihenfolge. Ebenen werden stabil nach z_index sortiert; gleiche Werte behalten ihre Listenreihenfolge. (Standard: 0) | INT | Nein | -1000 bis 1000 |
| `flip_h` | Ebene horizontal spiegeln. (Standard: False) | BOOLEAN | Nein | false / true |
| `flip_v` | Ebene vertikal spiegeln. (Standard: False) | BOOLEAN | Nein | false / true |

Hinweise:
- Nur `image` ist erforderlich; alle anderen Eingaben sind optional.
- Wenn `layers` nicht verbunden gelassen wird, wird ein neuer Ebenenstapel erstellt. Wenn ein Ebenenstapel verbunden ist, wird die neue Ebene daran angehängt.
- Ein Batch von Bildern in der Eingabe `image` erzeugt mehrere aufeinanderfolgende Ebenen.
- `width` und `height` haben standardmäßig den Wert 0, wodurch die nativen Abmessungen des Bildes beibehalten werden. Werte größer als 0 überschreiben die Anzeigegröße.
- `opacity`, `blend_mode`, `rotation`, `width` und `height` werden nur angewendet, wenn sie von ihren Standardwerten abweichen.
- Die Leinwandgröße eines verbundenen Ebenenstapels bleibt in der Ausgabe erhalten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `layers` | Der Ebenenstapel mit der angehängten Ebene. | LAYERS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/de.md)

---
**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`
