# ByteDance Seedance 2.5 Draft in finales Video

Dieser Node rendert das finale 1080p-Video eines Seedance 2.5 Drafts. Ein Draft ist eine schnelle 480p-Vorschau: In einem Seedance 2.5-Video-Node (Text-zu-Video, First-Last-Frame-zu-Video oder Referenz-zu-Video) setzen Sie `model` auf `Seedance 2.5 Draft`, führen Sie ihn aus und verbinden Sie dessen `draft_task_id`-Ausgabe hier. Das finale Video behält die Szene und die Bewegung des Drafts bei und verwendet den Prompt, die Referenzen, die Dauer, das Seitenverhältnis und die Audioeinstellung wieder, mit denen der Draft erzeugt wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `draft_task_id` | Die `draft_task_id`-Ausgabe eines Seedance 2.5-Nodes, der mit dem Modell Seedance 2.5 Draft ausgeführt wurde, oder eine eingefügte Draft-Task-ID. Wenn Sie den erzeugenden Node erneut ausführen, setzen Sie dessen Seed-Steuerung auf „fixed“, andernfalls generiert der nächste Lauf einen neuen Draft, anstatt den von Ihnen geprüften wiederzuverwenden. | STRING | Ja | - |
| `watermark` | Ob dem Video ein Wasserzeichen hinzugefügt werden soll. Der Standardwert ist False. Dies ist eine erweiterte Einstellung. | BOOLEAN | Nein | True / False |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das gerenderte finale 1080p-Video, das vom Anbieter heruntergeladen wird, sobald der Render-Task abgeschlossen ist. | VIDEO |

**Hinweis:** Ein Draft kann 7 Tage nach seiner Erstellung gerendert werden. Die Draft-Task-ID identifiziert den Draft eigenständig, daher müssen der Prompt, die Referenzen, die Dauer, das Seitenverhältnis und die Audioeinstellung nicht erneut übergeben werden.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
