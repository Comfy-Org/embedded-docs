# Breeze Voice Selector

Sélectionne une voix Breeze mise en avant, ou tout identifiant de voix Breeze, et la transmet à Breeze Text to Speech. Le nœud ne fait que résoudre un identifiant et n’effectue aucun appel API.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `language` | Groupe de langues des voix mises en avant, ou `custom` pour saisir un identifiant. Par défaut : `"English"`. | DYNAMIC_COMBO | Oui | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### Entrées pour la langue "English", "Chinese" et "Japanese"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voice` | Voix mise en avant dans cette langue. | COMBO | Oui | Plusieurs options disponibles |

### Entrées pour la langue "custom"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voice_id` | Tout identifiant de voix Breeze, par exemple une voix créée par les autres nœuds Breeze. Lettres, chiffres, `_` et `-` uniquement. Par défaut : vide. | STRING | Oui | Identifiant de voix Breeze |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voice` | La voix Breeze sélectionnée. | BREEZE_VOICE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/fr.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
