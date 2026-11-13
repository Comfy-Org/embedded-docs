# Breeze Voice Localize

Crée une copie d’une voix qui parle nativement une autre langue, au lieu de lire une langue étrangère avec son accent d’origine. La copie est enregistrée dans votre compte et renvoyée avec un aperçu audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voice` | Voix Breeze à copier. | BREEZE_VOICE | Oui | - |
| `language` | Langue parlée par la nouvelle voix. Par défaut : `"English"`. | COMBO | Oui | Plusieurs options disponibles |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats sont non déterministes quel que soit le seed. Par défaut : 42. | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voice` | La copie localisée de la voix, nommée d’après la voix d’origine et la langue. | BREEZE_VOICE |
| `preview` | Aperçu audio de la voix localisée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/fr.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`
