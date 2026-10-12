# Positiv gewichtete Guidance

Der Mahiro-Node modifiziert die Guidance-Funktion, um stärker auf die Richtung des positiven Prompts zu fokussieren, anstatt auf die Differenz zwischen positivem und negativem Prompt. Er erstellt ein gepatchtes Modell, das einen benutzerdefinierten Guidance-Skalierungsansatz unter Verwendung der Kosinusähnlichkeit zwischen normalisierten bedingten und unbedingten entrauschten Ausgaben anwendet. Dieser experimentelle Node hilft dabei, die Generierung stärker in die beabsichtigte Richtung des positiven Prompts zu lenken.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das mit der modifizierten Guidance-Funktion gepatcht werden soll | MODEL | Ja |  |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `patched_model` | Das modifizierte Modell mit angewendeter Mahiro-Guidance-Funktion | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/de.md)

---
**Source fingerprint (SHA-256):** `56f13cd14ffde21ab980850b62e07bdd4db6733a545f9329bf908c6030147981`
