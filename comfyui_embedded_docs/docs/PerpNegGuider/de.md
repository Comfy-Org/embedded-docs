# Perp-Neg Guider

Der PerpNegGuider-Node erstellt ein Führungssystem zur Steuerung der Bilderzeugung unter Verwendung von senkrechter negativer Konditionierung. Er akzeptiert positive, negative und leere Konditionierungseingaben und wendet einen spezialisierten Führungsalgorithmus an, der alle drei Rauschvorhersagen für mehr Effizienz in einem einzigen Batch berechnet. Dieser Node ist für experimentelle Tests gedacht und bietet feine Kontrolle über die Führungsstärke und die negative Skalierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das für die Führungserzeugung zu verwendende Modell | MODEL | Ja | - |
| `positive` | Die positive Konditionierung, die die Erzeugung in Richtung gewünschter Inhalte lenkt | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, die die Erzeugung von unerwünschten Inhalten weglenkt | CONDITIONING | Ja | - |
| `empty_conditioning` | Die leere oder neutrale Konditionierung, die als Basisreferenz für die senkrechte negative Führung verwendet wird | CONDITIONING | Ja | - |
| `cfg` | Der Classifier-Free-Guidance-Skalierungswert, der steuert, wie stark die Konditionierung die Erzeugung beeinflusst (Standard: 8.0) | FLOAT | Ja | 0.0 - 100.0 |
| `neg_scale` | Der negative Skalierungsfaktor, der die Stärke des senkrechten negativen Effekts anpasst (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `guider` | Ein konfiguriertes Führungssystem, bereit zur Verwendung in der Generierungspipeline | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/de.md)

---
**Source fingerprint (SHA-256):** `02e4b4e0ea413da31c280cb1e510bdf5caa7b5187eb6de94632e45a91e881820`
