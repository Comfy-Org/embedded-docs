# PerturbedAttentionGuidance

Der Node PerturbedAttentionGuidance wendet Perturbed Attention Guidance auf ein Diffusionsmodell an, um die Generierungsqualität zu verbessern. Während des Samplings führt er eine zusätzliche Vorhersage durch, bei der die Self-Attention des Middle Blocks durch eine vereinfachte Version ersetzt wird, die die Value-Projektionen direkt weiterleitet; anschließend wird die skalierte Differenz zwischen der normalen bedingten Vorhersage und dieser perturbierten Vorhersage zum entrauschten Ergebnis addiert. Wenn `scale` auf 0 gesetzt wird, ist der Effekt vollständig deaktiviert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Diffusionsmodell, auf das Perturbed Attention Guidance angewendet werden soll | MODEL | Ja | - |
| `scale` | Die Stärke des Perturbed Attention Guidance-Effekts (Standard: 3.0). Bei Einstellung auf 0 hat der Node keine Wirkung und gibt das ursprüngliche entrauschte Ergebnis unverändert zurück. | FLOAT | Ja | 0.0 - 100.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model` | Das modifizierte Modell, bei dem der Perturbed Attention Guidance-Patch an seinen Sampling-Prozess angehängt ist | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/de.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
