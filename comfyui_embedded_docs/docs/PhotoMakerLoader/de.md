# PhotoMakerLoader

Der Node PhotoMakerLoader lädt ein PhotoMaker-Modell aus den verfügbaren Modelldateien. Er liest die ausgewählte Datei, lädt deren ID-Encoder-Gewichte und bereitet den PhotoMaker-ID-Encoder für die Verwendung in identitätsbasierten Bildgenerierungsaufgaben vor. Dieser Node ist als experimentell gekennzeichnet und für Testzwecke vorgesehen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | Der Name der zu ladenden PhotoMaker-Modell-Datei. Die verfügbaren Optionen richten sich nach den im Ordner `photomaker` vorhandenen Modelldateien. | COMBO | Ja | Mehrere Optionen verfügbar (dynamisch befüllt aus dem Ordner `photomaker`) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `photomaker_model` | Das geladene PhotoMaker-Modell, das den ID-Encoder enthält und für die Verwendung in Identitätskodierungsvorgängen bereit ist. | PHOTOMAKER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/de.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
