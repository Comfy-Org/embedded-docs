# Breeze Voice Remix

Crée une copie modifiée d’une voix dans la même langue, soit à partir d’une description écrite de la modification, soit à partir d’un préréglage nommé. La copie est enregistrée dans votre compte et renvoyée avec un aperçu audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voice` | Voix Breeze à modifier. | BREEZE_VOICE | Oui | - |
| `change` | `custom` décrit la modification en texte, `preset` sélectionne une modification nommée. Par défaut : `"custom"`. | DYNAMIC_COMBO | Oui | `"custom"`<br>`"preset"` |
| `strength` | Des valeurs plus élevées modifient davantage la voix. Par défaut : 4.0. | FLOAT | Non | 1.0 à 10.0 (pas : 0.1) |
| `seed` | Contrôle si le nœud se réexécute ; les résultats ne sont pas déterministes quel que soit le seed. Par défaut : 42. | INT | Non | 0 à 2147483647 |

### Entrées de modification "custom"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Comment la voix doit changer, par exemple plus âgée et rauque. Par défaut : vide. | STRING | Oui | Texte multiligne |

### Entrées de modification "preset"

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `preset` | Modification nommée, regroupée par âge, genre, hauteur, rythme, énergie et émotion. | COMBO | Oui | Plusieurs options disponibles |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voice` | La copie modifiée de la voix. | BREEZE_VOICE |
| `preview` | Aperçu audio de la voix remixée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/fr.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`
