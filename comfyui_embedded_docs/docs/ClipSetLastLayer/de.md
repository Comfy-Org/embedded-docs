# ClipSetLastLayer

`CLIP Set Last Layer` ist ein Kernknoten in ComfyUI zur Steuerung der Verarbeitungstiefe von CLIP-Modellen. Er ermöglicht es Benutzern, präzise zu steuern, wo der CLIP-Text-Encoder die Verarbeitung beendet, was sowohl die Tiefe des Textverständnisses als auch den Stil der generierten Bilder beeinflusst. Das ursprüngliche CLIP-Modell bleibt unverändert: Der Knoten arbeitet mit einer Kopie und gibt die geänderte Kopie zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das zu ändernde CLIP-Modell | CLIP | Ja | - |
| `stop_at_clip_layer` | Gibt an, bei welcher Schicht gestoppt werden soll. Ein Wert von -1 verwendet alle Schichten, während -24 nur die erste Schicht verwendet (Standard: -1). Dies ist ein erweiterter Parameter. | INT | Ja | -24 bis -1 (Schritt: 1) |

Die Werte sind negativ und zählen vom Ende des Modells rückwärts: -1 bezieht sich auf die letzte (tiefste) Schicht und -24 auf die erste (flachste) Schicht, weshalb der zulässige Bereich nur -24 bis -1 abdeckt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Das geänderte CLIP-Modell (ein Klon der Eingabe; das ursprüngliche CLIP-Modell wird nicht geändert), bei dem die angegebene Schicht als letzte festgelegt wurde | CLIP |

## Warum die letzte Schicht festlegen

- **Performance-Optimierung**: Ähnlich wie man keinen Doktortitel braucht, um einfache Sätze zu verstehen, reicht manchmal ein flaches Verständnis aus und ist schneller
- **Stilsteuerung**: Unterschiedliche Verständnistiefen erzeugen unterschiedliche künstlerische Stile
- **Kompatibilität**: Einige Modelle erzielen bei bestimmten Schichten möglicherweise bessere Ergebnisse

Stellen Sie sich das CLIP-Modell als ein intelligentes Gehirn mit 24 Schichten vor:

- Flache Schichten (1-8): Erkennen grundlegende Buchstaben und Wörter
- Mittlere Schichten (9-16): Verstehen Grammatik und Satzstruktur
- Tiefe Schichten (17-24): Erfassen abstrakte Konzepte und komplexe Semantik

`CLIP Set Last Layer` funktioniert wie ein **„Denktiefen-Controller“**:

- -1: Alle 24 Schichten verwenden (vollständiges Verständnis)
- -2: Bei Schicht 23 stoppen (leicht vereinfacht)
- -12: Bei Schicht 13 stoppen (mittleres Verständnis)
- -24: Nur Schicht 1 verwenden (grundlegendes Verständnis)

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSetLastLayer/de.md)

---
**Source fingerprint (SHA-256):** `41a7feb9729dbb2a987a15a53c56641eae2a5611db8762ef2ce14b58970752fe`
