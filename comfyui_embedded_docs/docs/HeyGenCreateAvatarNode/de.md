# HeyGenCreateAvatarNode

Erstellen Sie einen wiederverwendbaren HeyGen-Avatar aus einem Foto einer Person oder aus einem Text-Prompt, der eine zu generierende Figur beschreibt. Die resultierende `avatar_id` kann mit dem HeyGen Avatar Video-Node verwendet werden und sollte gespeichert werden, um den Avatar in zukünftigen Workflows wiederzuverwenden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `source` | Generieren Sie eine neue Figur aus einem Text-Prompt oder erstellen Sie den Avatar aus einem verbundenen Foto einer Person. | DYNAMIC_COMBO | Ja | `"prompt"`<br>`"photo"` |

### Prompt-Eingaben

Verfügbar, wenn `source` auf `"prompt"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibung des zu generierenden Avatars (bis zu 1000 Zeichen). Muss mindestens 1 Zeichen enthalten, das kein Leerzeichen ist. Standard: leerer String. | STRING | Ja | 1 bis 1000 Zeichen |

### Foto-Eingaben

Verfügbar, wenn `source` auf `"photo"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Foto der Person, die in einen Avatar umgewandelt werden soll. Wird automatisch herunterskaliert, wenn es größer als 2K ist. | IMAGE | Ja | Einzelbild |

### Referenzeingaben

Verfügbar, wenn `source` auf `"prompt"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Bilder (`ref_image_1`...`ref_image_3`), die das generierte Aussehen steuern. Bilder werden automatisch herunterskaliert, wenn sie größer als 2K sind. | IMAGE | Nein | 0 bis 3 Bilder |

**Hinweis:** Der Parameter `source` wechselt zwischen zwei sich gegenseitig ausschließenden Modi. Im Modus `"prompt"` ist `prompt` erforderlich und optional können bis zu 3 Referenzbilder verbunden werden. Im Modus `"photo"` ist `identity_photo` erforderlich. Fotos und Referenzbilder werden automatisch herunterskaliert, wenn sie größer als 2K sind; mehr als 3 Referenzbilder werden nicht akzeptiert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `avatar_id` | Avatar-Look-ID. Übergeben Sie sie an `custom_avatar_id` von HeyGen Avatar Video; speichern Sie sie, um den Avatar später wiederzuverwenden. | STRING |
| `preview` | Vorschaubild des generierten Avatars. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/de.md)

---
**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`
