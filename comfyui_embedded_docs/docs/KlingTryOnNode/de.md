# KlingTryOnNode

Kleiden Sie eine Person mit einem Kleidungsstück mithilfe von Klings virtueller Anprobe. Verbinden Sie ein Foto einer Person und ein Foto des Kleidungsstücks; der Node gibt ein neues Bild dieser Person zurück, die das Kleidungsstück trägt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `person_image` | Foto einer Person, idealerweise in Frontal- oder Dreiviertelansicht. Muss mindestens 300x300 Pixel groß sein; Bilder mit einer Seite über 2048 Pixel werden zuerst herunterskaliert. | IMAGE | Ja | N/A |
| `garment_image` | Das anzuziehende Kleidungsstück: Produktfoto, flache Auslage, Schaufensterpuppe oder Foto an einem Model. Ein Foto an einem Model kann den Rest dieses Outfits übernehmen. Muss mindestens 300x300 Pixel groß sein. Nur Kleidung; Schuhe, Taschen und Accessoires werden nicht unterstützt. | IMAGE | Ja | N/A |
| `keep_pose` | Ausschalten, um zuzulassen, dass sich die Pose für eine bessere Präsentation des Outfits ändert. Erweiterter Parameter (Standard: True). | BOOLEAN | Ja | `True`<br>`False` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Dieser Parameter bietet eine „control after generate“-Funktionalität (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Das Ergebnis hat dieselbe Größe wie `person_image`, begrenzt auf 2048 Pixel an der längsten Seite. Beide Eingaben werden in die Kling-API hochgeladen, was einen Moment dauern kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Die Person, die das Kleidungsstück trägt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/de.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
