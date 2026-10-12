# Adaptive projizierte Führung

Der APG-Node (Adaptive Projected Guidance) modifiziert den Sampling-Prozess, indem er anpasst, wie Guidance während der Diffusion angewendet wird. Er trennt den Guidance-Vektor in parallele und orthogonale Komponenten relativ zur bedingten Ausgabe, was eine kontrolliertere Bilderzeugung ermöglicht. Der Node stellt Parameter bereit, um die Guidance zu skalieren, ihre Magnitude zu normalisieren und Momentum für sanftere Übergänge zwischen Diffusionsschritten anzuwenden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das adaptive projizierte Guidance angewendet werden soll | MODEL | Ja | - |
| `eta` | Steuert die Skalierung des parallelen Guidance-Vektors. Standard-CFG-Verhalten bei Einstellung 1 (Standard: 1.0). | FLOAT | Nein | -10.0 bis 10.0 |
| `norm_threshold` | Normalisiert den Guidance-Vektor auf diesen Wert, Normalisierung bei Einstellung 0 deaktiviert (Standard: 5.0). | FLOAT | Nein | 0.0 bis 50.0 |
| `momentum` | Steuert einen laufenden Mittelwert der Guidance während der Diffusion, bei Einstellung 0 deaktiviert (Standard: 0.0). | FLOAT | Nein | -5.0 bis 1.0 |

Hinweis: Wenn der Rauschpegel (`sigma`) während des Samplings ansteigt, wird der laufende Mittelwert des Momentums auf null zurückgesetzt. Wenn das Modell nur eine einzelne Konditionierungsausgabe bereitstellt (keine separate unbedingte Konditionierung), wird die Guidance-Anpassung übersprungen und die Konditionierung bleibt unverändert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Gibt das modifizierte Modell zurück, auf dessen Sampling-Prozess adaptive projizierte Guidance angewendet wurde | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/de.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
