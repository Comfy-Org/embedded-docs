# BasicScheduler

Der `BasicScheduler`-Node ist darauf ausgelegt, eine Sequenz von Sigma-Werten für Diffusionsmodelle basierend auf dem angegebenen Scheduler, Modell und Denoising-Parametern zu berechnen. Er passt die Gesamtzahl der Schritte dynamisch anhand des Denoise-Faktors an, um den Diffusionsprozess fein abzustimmen, und liefert präzise „Rezepte“ für verschiedene Phasen in fortgeschrittenen Sampling-Prozessen, die eine feine Steuerung erfordern (z. B. mehrstufiges Sampling).

## Eingaben

| Parameter | Metaphorische Beschreibung | Datentyp | Eingabetyp | Standard | Bereich | Technischer Zweck |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | **Leinwandtyp**: Unterschiedliche Leinwandmaterialien benötigen unterschiedliche Farbformeln | MODEL | Eingabe | - | - | Diffusionsmodell-Objekt, bestimmt die Grundlage der Sigma-Berechnung |
| `scheduler` | **Mischtechnik**: Wählen Sie, wie sich die Farbkonzentration ändert | COMBO[STRING] | Widget | - | 9 Optionen | Scheduler-Algorithmus, steuert den Modus des Rauschabfalls |
| `steps` | **Mischungsanzahl**: Präzisionsunterschied zwischen 20 Mischungen und 50 Mischungen | INT | Widget | 20 | 1-10000 | Sampling-Schritte, beeinflussen Generierungsqualität und -geschwindigkeit |
| `denoise` | **Erstellungsintensität**: Steuerungsstufe von Feinabstimmung bis zum Übermalen | FLOAT | Widget | 1.0 | 0.0-1.0 | Denoising-Stärke, unterstützt Szenarien mit partiellem Übermalen |

### Scheduler-Typen

Basierend auf dem Quellcode `comfy.samplers.SCHEDULER_NAMES` werden die folgenden 9 Scheduler unterstützt:

| Scheduler-Name       | Eigenschaften      | Anwendungsfälle                    | Rauschabfallmuster          |
| -------------------- | -------------------- | ---------------------------- | ---------------------------- |
| **normal**           | Standardlinear      | Allgemeine Szenarien, ausgewogen  | Gleichmäßiger Abfall                |
| **karras**           | Sanfter Übergang    | Hohe Qualität, detailreich    | Sanfter nichtlinearer Abfall      |
| **exponential**      | Exponentieller Abfall    | Schnelle Generierung, Effizienz  | Exponentiell schneller Abfall      |
| **sgm_uniform**      | SGM-uniform          | Optimierung für bestimmte Modelle  | SGM-optimierter Abfall          |
| **simple**           | Einfache Planung    | Schnelltests, grundlegende Nutzung     | Vereinfachter Abfall             |
| **ddim_uniform**     | DDIM-uniform         | DDIM-Sampling-Optimierung   | DDIM-spezifischer Abfall          |
| **beta**             | Beta-Verteilung    | Besondere Verteilungsanforderungen   | Beta-Funktions-Abfall          |
| **linear_quadratic** | Linear-quadratisch     | Optimierung komplexer Szenarien| Quadratischer Funktionsabfall     |
| **kl_optimal**       | KL-optimal           | Theoretische Optimierung     | KL-Divergenz-optimierter Abfall|

## Ausgaben

| Parameter | Metaphorische Beschreibung | Datentyp | Ausgabetyp | Technische Bedeutung |
| --- | --- | --- | --- | --- |
| `sigmas` | **Farbmischungs-Rezepttabelle**: Detaillierte Liste der Farbkonzentrationen zur schrittweisen Verwendung | SIGMAS | Ausgabe | Rauschpegel-Sequenz, leitet den Denoising-Prozess des Diffusionsmodells an |

## Node-Rolle: Farbmischassistent des Künstlers

Stellen Sie sich vor, Sie sind ein Künstler, der aus einer chaotischen Farbmischung (Rauschen) ein klares Bild erstellt. `BasicScheduler` fungiert als Ihr **professioneller Farbmischassistent**, dessen Aufgabe es ist, eine Reihe präziser Rezepte für Farbkonzentrationen vorzubereiten:

### Arbeitsablauf

- **Schritt 1**: Farbe mit 90 % Konzentration verwenden (hoher Rauschpegel)
- **Schritt 2**: Farbe mit 80 % Konzentration verwenden  
- **Schritt 3**: Farbe mit 70 % Konzentration verwenden
- **...**
- **Letzter Schritt**: 0 % Konzentration verwenden (saubere Leinwand, kein Rauschen)

### Spezielle Fähigkeiten des Farbassistenten

**Verschiedene Mischmethoden (Scheduler)**:

- **„karras“-Mischmethode**: Die Farbkonzentration ändert sich sehr sanft, wie die Gradiententechnik eines professionellen Künstlers
- **„exponential“-Mischmethode**: Die Farbkonzentration nimmt schnell ab, geeignet für schnelles Erstellen
- **„linear“-Mischmethode**: Die Farbkonzentration nimmt gleichmäßig ab, stabil und kontrollierbar

**Feinsteuerung (steps)**:

- **20 Mischungen**: Schnelles Malen, Effizienz im Vordergrund
- **50 Mischungen**: Feines Malen, Qualität im Vordergrund

**Erstellungsintensität (denoise)**:

- **1.0 = Vollständige Neuerstellung**: Vollständig von einer leeren Leinwand beginnen
- **0.5 = Halbe Umwandlung**: Die Hälfte des Originalgemäldes behalten, die Hälfte umwandeln
- **0.2 = Feinabstimmung**: Nur subtile Anpassungen am Originalgemälde vornehmen

### Zusammenarbeit mit anderen Nodes

`BasicScheduler` (Farbassistent) → Rezept vorbereiten → `SamplerCustom` (Künstler) → Tatsächliches Malen → Fertiges Werk

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/de.md)
