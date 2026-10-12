# ConvertDictionaryToString

Dieser Node wandelt ein Dictionary (eine Sammlung von Schlüssel-Wert-Paaren) in einen Text-String im JSON-Format um. Sie können die Einrückungsebene steuern, um die Ausgabe lesbarer oder kompakter zu machen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `dictionary` | Das Dictionary, das in einen String umgewandelt werden soll | DICT | Ja | - |
| `indent` | Leerzeichen pro Einrückungsebene. 0 erzeugt einen kompakten einzeiligen String (Standard: 2) | INT | Nein | 0 to 8 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-----------|-----------|
| `STRING` | Das in einen JSON-formatierten String umgewandelte Dictionary | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertDictionaryToString/de.md)

---
**Source fingerprint (SHA-256):** `ae4e9889d5347acfc69166bac66f2ba63f5cd37dafab25a9e0aff6bfe7381219`
