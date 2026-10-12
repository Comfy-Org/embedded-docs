# SamplerCustom

Der SamplerCustom-Node wurde entwickelt, um einen flexiblen und anpassbaren Sampling-Mechanismus für verschiedene Anwendungen bereitzustellen. Er ermöglicht Benutzern, verschiedene Sampling-Strategien auszuwählen und zu konfigurieren, die auf ihre spezifischen Anforderungen zugeschnitten sind, wodurch die Anpassungsfähigkeit und Effizienz des Sampling-Prozesses erhöht werden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Der Eingabetyp `model` gibt das für das Sampling zu verwendende Modell an und spielt eine entscheidende Rolle bei der Bestimmung des Sampling-Verhaltens und der Ausgabe. | `MODEL` |
| `add_noise` | Der Eingabetyp `add_noise` ermöglicht es Benutzern anzugeben, ob dem Sampling-Prozess Rauschen hinzugefügt werden soll, was die Vielfalt und die Eigenschaften der erzeugten Samples beeinflusst. | `BOOLEAN` |
| `noise_seed` | Der Eingabetyp `noise_seed` liefert einen Seed für die Rauscherzeugung, wodurch Reproduzierbarkeit und Konsistenz im Sampling-Prozess beim Hinzufügen von Rauschen gewährleistet werden. | `INT` |
| `cfg` | Der Eingabetyp `cfg` legt die Konfiguration für den Sampling-Prozess fest und ermöglicht die Feinabstimmung der Sampling-Parameter und des Verhaltens. | `FLOAT` |
| `positive` | Der Eingabetyp `positive` repräsentiert positive Konditionierungsinformationen und lenkt den Sampling-Prozess darauf, Samples zu erzeugen, die mit den angegebenen positiven Attributen übereinstimmen. | `CONDITIONING` |
| `negative` | Der Eingabetyp `negative` repräsentiert negative Konditionierungsinformationen und steuert den Sampling-Prozess so, dass keine Samples erzeugt werden, die die angegebenen negativen Attribute aufweisen. | `CONDITIONING` |
| `sampler` | Der Eingabetyp `sampler` wählt die spezifische zu verwendende Sampling-Strategie aus und wirkt sich direkt auf die Art und Qualität der erzeugten Samples aus. | `SAMPLER` |
| `sigmas` | Der Eingabetyp `sigmas` definiert die im Sampling-Prozess zu verwendenden Rauschpegel, was die Erkundung des Sample-Raums und die Vielfalt der Ausgabe beeinflusst. | `SIGMAS` |
| `latent_image` | Der Eingabetyp `latent_image` stellt ein anfängliches latentes Bild für den Sampling-Prozess bereit, das als Ausgangspunkt für die Sample-Erzeugung dient. | `LATENT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Der Ausgang `output` stellt das primäre Ergebnis des Sampling-Prozesses dar und enthält die erzeugten Samples. | `LATENT` |
| `denoised_output` | Der Ausgang `denoised_output` repräsentiert die Samples nach Anwendung eines Denoising-Prozesses, wodurch möglicherweise die Klarheit und Qualität der erzeugten Samples verbessert wird. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/de.md)
