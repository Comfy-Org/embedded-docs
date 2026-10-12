# Latent laden

Der LoadLatent-Node lädt zuvor gespeicherte latente Repräsentationen aus .latent-Dateien im Eingabeverzeichnis. Er liest die latenten Tensor-Daten aus der ausgewählten Datei und wendet alle erforderlichen Skalierungsanpassungen an, bevor er die latenten Daten zur Verwendung in anderen Nodes zurückgibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latent` | Wählt aus, welche .latent-Datei aus den verfügbaren Dateien im Eingabeverzeichnis geladen werden soll | COMBO | Ja | Alle .latent-Dateien im Eingabeverzeichnis (dynamische Liste, alphabetisch sortiert) |

Hinweis: Die Liste der verfügbaren Dateien wird dynamisch generiert und enthält nur Dateien mit der Endung .latent, die im Eingabeverzeichnis vorhanden sind. Wenn die ausgewählte Datei nicht mehr existiert, meldet der Node sie als ungültige Latent-Datei.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Gibt die geladenen latenten Repräsentationsdaten aus der ausgewählten Datei als Float-Tensor zurück. Wenn die Datei nicht den Marker `latent_format_version_0` enthält, wird der Tensor vor der Rückgabe um 1/0.18215 skaliert; Dateien, die den Marker enthalten, werden mit ihrer gespeicherten Skalierung zurückgegeben. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/de.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
