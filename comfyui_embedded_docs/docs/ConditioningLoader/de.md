# Conditioning laden

Dieser Node lädt eine Konditionierung, die zuvor mit dem Node „Save Conditioning“ gespeichert wurde, oder eine beliebige safetensors-Datei, die einen `conditioning`-Tensor enthält, aus dem Embeddings-Ordner. Außerdem werden alle zusätzlichen Optionen und nummerierten Listenwerte wiederhergestellt, die zusammen mit der Konditionierung gespeichert wurden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `conditioning_name` | Die aus dem Embeddings-Ordner zu ladende Datei. Die Auswahlliste wird aus den derzeit in diesem Ordner verfügbaren Dateien erstellt. | COMBO | Ja | Alle Dateien im Embeddings-Ordner |

**Hinweis:** Die ausgewählte Datei muss einen `conditioning`-Tensor enthalten. Alle zusätzlichen in der Datei gespeicherten Schlüssel werden wiederhergestellt: nummerierte Schlüssel (zum Beispiel `key.0`, `key.1`) werden wieder zu geordneten Listen zusammengefasst, und andere Schlüssel werden als einfache Optionen wiederhergestellt. Zusätzliche Optionen werden, sofern vorhanden, aus den `conditioning_options`-Metadaten der Datei gelesen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CONDITIONING` | Die aus der Datei geladene Konditionierung zusammen mit den wiederhergestellten Optionen. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/de.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`
