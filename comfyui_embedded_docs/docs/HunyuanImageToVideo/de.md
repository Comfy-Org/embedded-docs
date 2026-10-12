# HunyuanImageToVideo

Der Node HunyuanImageToVideo wandelt Bilder mithilfe des Hunyuan-Videomodells in latente Video-Repräsentationen um. Er nimmt Konditionierungseingaben und optionale Startbilder entgegen, um Video-Latents zu erzeugen, die von Videogenerierungsmodellen weiterverarbeitet werden können. Der Node unterstützt verschiedene Guidance-Typen, mit denen gesteuert wird, wie das Startbild den Videogenerierungsprozess beeinflusst.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungseingabe zur Steuerung der Videogenerierung | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Bildern in den latenten Raum verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 848, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im Ausgabevideo (Standard: 53, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `guidance_type` | Methode zur Einbeziehung des Startbilds in die Videogenerierung (Standard: "v1 (concat)"). Erweiterte Option | COMBO | Ja | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Optionales Startbild (oder Bildsequenz) zur Initialisierung der Videogenerierung. Es werden nur die ersten `length` Frames und die ersten 3 Farbkanäle verwendet | IMAGE | Nein | - |

**Hinweis:** Wenn `start_image` bereitgestellt wird, verwendet der Node je nach ausgewähltem `guidance_type` unterschiedliche Guidance-Methoden:

- "v1 (concat)": Konkateniert das Bild-Latent mit dem Video-Latent und wendet eine Maske an, um das Bild in das Video zu mischen
- "v2 (replace)": Ersetzt anfängliche Video-Frames durch das Bild-Latent und wendet eine Rauschmaske an
- "custom": Verwendet das Bild als Referenz-Latent zur Steuerung

Wenn `start_image` nicht bereitgestellt wird, wird keine Guidance-Konditionierung hinzugefügt und das Latent wird als einfacher Block aus Nullen zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Modifizierte positive Konditionierung mit angewendeter Bild-Guidance, wenn start_image bereitgestellt wird | CONDITIONING |
| `latent` | Video-Latent-Repräsentation, bereit zur weiteren Verarbeitung durch Videogenerierungsmodelle | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
