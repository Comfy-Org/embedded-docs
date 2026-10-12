# Kling 2.6 Text zu Video mit Audio

Der Node „Kling Text to Video with Audio“ generiert ein kurzes Video aus einer Textbeschreibung. Er sendet eine Anfrage an den Kling AI-Dienst, der den Prompt verarbeitet und eine Videodatei zurückgibt. Der Node kann außerdem begleitendes Audio für das Video basierend auf dem Text generieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_name` | Das spezifische KI-Modell, das für die Videogenerierung verwendet werden soll. | COMBO | Ja | `"kling-v2-6"` |
| `prompt` | Positiver Text-Prompt. Die Beschreibung, die zur Generierung des Videos verwendet wird. Muss zwischen 1 und 2500 Zeichen lang sein. | STRING | Ja | - |
| `mode` | Der Betriebsmodus für die Videogenerierung. | COMBO | Ja | `"pro"` |
| `aspect_ratio` | Das gewünschte Breiten-Höhen-Verhältnis für das generierte Video. | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Die Länge des Videos in Sekunden. | COMBO | Ja | `5`<br>`10` |
| `generate_audio` | Steuert, ob Audio für das Video generiert wird. Wenn aktiviert, erzeugt die KI Audio basierend auf dem Prompt (Standard: `True`). | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/de.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`
