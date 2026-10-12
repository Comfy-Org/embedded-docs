# SeedVR2-Latents zusammenführen

Dieser Node rekombiniert gesampelte latente zeitliche SeedVR2-Chunks zu einem einzelnen Latent voller Länge. Wenn eine zeitliche Überlappung angegeben ist, überblendet er jeden überlappenden Bereich mit einem Hann-Fenster, um sanfte Übergänge zwischen den Chunks zu erzeugen; wenn die Überlappung 0 ist, führt er eine einfache Verkettung durch.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `latents` | Die gesampelten zeitlichen Chunks in Sequenzreihenfolge. | LATENT | Ja | Liste von Latents |
| `temporal_overlap` | Die `temporal_overlap`-Ausgabe von Split SeedVR2 Latent. 0 = einfache Verkettung. (Standard: 0) | INT | Ja | 0 bis 16384 |

**Hinweis:** Der Wert `temporal_overlap` muss größer oder gleich 0 sein. Alle Chunks müssen 5-dimensionale Video-Latents (B, C, T, H, W) sein und in jeder Dimension außer der zeitlichen Achse (T) übereinstimmen; nur der letzte Chunk darf kürzer als die anderen sein. Wenn nur ein Chunk bereitgestellt wird, wird er unverändert zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `latent` | Das rekombinierte Latent voller Länge. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/de.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
