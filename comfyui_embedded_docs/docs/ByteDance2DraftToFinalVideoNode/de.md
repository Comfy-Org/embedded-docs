# ByteDance Seedance 2.5 Draft in finales Video

Dieser Node rendert das finale Video eines Seedance 2.5 Draft mit 1080p oder 4k. 4k ist für alle Konten verfügbar. Ein Draft ist eine schnelle 480p-Vorschau: Legen Sie in einem Seedance 2.5 Video-Node (Text zu Video, Erstes-Letztes-Bild zu Video oder Referenz zu Video) `model` auf `Seedance 2.5 Draft` fest, führen Sie ihn aus und verbinden Sie dessen Ausgabe `draft_task_id` mit diesem Node. Das Finale behält Szene und Bewegung des Drafts bei und verwendet den Prompt, die Referenzen, die Dauer, das Seitenverhältnis und die Audio-Einstellung wieder, mit denen der Draft erzeugt wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `draft_task_id` | Die Ausgabe `draft_task_id` eines Seedance 2.5 Node-Laufs mit dem Modell Seedance 2.5 Draft oder eine eingefügte Draft-Task-ID. Wenn Sie den erzeugenden Node erneut ausführen, stellen Sie dessen Seed-Steuerung auf fest, da sonst der nächste Lauf einen neuen Draft erzeugt, anstatt den von Ihnen geprüften wiederzuverwenden. | STRING | Ja | - |
| `Wasserzeichen` | Ob dem Video ein Wasserzeichen hinzugefügt werden soll. Standard ist False. Dies ist eine erweiterte Einstellung. | BOOLEAN | Nein | True oder False |
| `resolution` | Auflösung des finalen Videos. `"4k"` ist für alle Konten verfügbar; verwenden Sie genau den kleingeschriebenen Wert `"4k"`. Standard: `"1080p"`. | COMBO | Nein | `"1080p"`<br>`"4k"` |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das gerenderte finale Video, das vom Anbieter heruntergeladen wird, sobald die Render-Aufgabe abgeschlossen ist. | VIDEO |

**Hinweis:** Ein Draft kann bis zu 7 Tage nach seiner Erstellung gerendert werden. Die Draft-Task-ID identifiziert den Draft eigenständig, daher müssen Prompt, Referenzen, Dauer, Seitenverhältnis und Audio-Einstellung nicht erneut übergeben werden.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bf96a485d5febde26e22433d190cfe42bd21dc6316d66141ad23d4b95a845dc5`
