# LTXVFreezeLatent

Der Node LTXV Freeze Latent setzt die Rauschmaske eines Latents auf null, wodurch dieses Latent sauber und unverändert bleibt, während das Sampling läuft. Er funktioniert sowohl mit Video- als auch mit Audio-Latents, sodass ein Latent eingefroren werden kann, bevor es mit anderen verkettet wird oder wenn es überhaupt nicht entrauscht werden soll.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `latent` | Video- oder Audio-Latent, das eingefroren werden soll. Audio ist 4D; Video ist 5D. | LATENT | Ja | N/A |

### Einschränkungen

- Das Latent muss einen einfachen Tensor enthalten. Ein verkettetes Audio-Video-Latent wird nicht akzeptiert; es muss zuerst mit dem Node Separate AV Latent getrennt werden.
- Es werden nur 4D-Latents (Audio) und 5D-Latents (Video) unterstützt. Jede andere Form verursacht einen Fehler.
- Die generierte Rauschmaske wird mit Nullen erstellt und verwendet dasselbe Gerät wie der Eingabe-Tensor. Bei Video-Latents hat die Maske die Form (batch, 1, frames, 1, 1); bei Audio-Latents hat sie die Form (batch, 1, frames, 1).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `latent` | Das Eingabe-Latent mit einer hinzugefügten Rauschmaske aus Nullen, sodass es während des Samplings sauber bleibt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/de.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
