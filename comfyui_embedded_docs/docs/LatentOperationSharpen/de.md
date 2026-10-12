# LatentOperationSharpen

Der Node `LatentOperationSharpen` erstellt eine Schärfungsoperation für latente Repräsentationen unter Verwendung eines Gauß-basierten Kernels. Er normalisiert die latenten Daten, wendet einen benutzerdefinierten Schärfungskernel durch Faltung an und stellt anschließend die ursprüngliche Luminanz wieder her, wodurch Details und Kanten in der latenten Raumdarstellung verstärkt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | Der Radius des Schärfungskernels, der die Größe des für die Schärfung verwendeten Bereichs steuert (Standard: 9) | INT | Ja | 1-31 |
| `sigma` | Die Standardabweichung des Gauß-Kernels, der zum Aufbau des Schärfungskernels verwendet wird (Standard: 1.0) | FLOAT | Ja | 0.1-10.0 |
| `alpha` | Der Intensitätsfaktor für die Schärfung; höhere Werte erzeugen einen stärkeren Schärfungseffekt (Standard: 0.1) | FLOAT | Ja | 0.0-5.0 |

Alle drei Eingaben sind erweiterte Parameter und haben Standardwerte, sodass der Node verwendet werden kann, ohne sie zu ändern. Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `operation` | Gibt eine Schärfungsoperation zurück, die auf latente Daten angewendet werden kann | LATENT_OPERATION |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/de.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
