# CLIP-Gerät auswählen

## Überblick

Mit dem Node Select CLIP Device können Sie auswählen, auf welchem Gerät (CPU oder einer bestimmten GPU) der CLIP-Textencoder ausgeführt wird. Standardmäßig wird das Gerät vom Modell-Loader zugewiesen, Sie können diese Zuweisung jedoch überschreiben, um die CPU oder eine bestimmte GPU zu verwenden. Wenn das angeforderte Gerät auf Ihrem Rechner nicht vorhanden ist, reicht der Node den CLIP einfach unverändert durch und protokolliert eine Meldung, anstatt einen Fehler zu verursachen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Der CLIP-Textencoder, der einem bestimmten Gerät zugewiesen werden soll. | CLIP | Ja |  |
| `device` | Das Gerät, auf dem der CLIP-Textencoder platziert werden soll. `"default"` stellt das vom Loader zugewiesene Gerät wieder her. `"cpu"` fixiert sowohl das Load- als auch das Offload-Gerät auf CPU. `"gpu:N"` fixiert das Load-Gerät auf die N-te verfügbare GPU (Standard: `"default"`). | COMBO | Ja | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Der CLIP-Textencoder, der dem ausgewählten Gerät zugewiesen wurde, oder das ursprüngliche CLIP, das unverändert durchgereicht wird, wenn das angeforderte Gerät nicht verfügbar ist. | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/de.md)

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
