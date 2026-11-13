# Breeze Voice Design

Crée une nouvelle voix Breeze à partir d'une description écrite. Fournissez une description de la voix et une phrase à prononcer ; la voix est construite à partir de cet aperçu et enregistrée dans votre compte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `description` | Description de la voix en 3 à 500 caractères : âge, genre, accent, ton, rythme. Par défaut : vide. | STRING | Oui | 3 à 500 caractères |
| `preview_text` | La phrase que la nouvelle voix prononce dans l'aperçu, jusqu'à 500 caractères. Écrivez-la dans la langue sélectionnée, car la voix est construite à partir de cet aperçu. Par défaut : vide. | STRING | Oui | 1 à 500 caractères |
| `language` | Langue du texte d'aperçu. English et Chinese peuvent utiliser l'un ou l'autre modèle ; les autres langues utilisent Breeze TTS 2 Multilingual. | DYNAMIC_COMBO | Oui | Plusieurs options disponibles |
| `strength` | À quel point la voix suit la description. Par défaut : 4.0. | FLOAT | Non | 1.0 à 10.0 (pas : 0.1) |
| `seed` | Contrôle si le nœud s'exécute à nouveau ; les résultats sont non déterministes quel que soit la graine. Par défaut : 42. | INT | Non | 0 à 2147483647 |

### Entrées pour les langues "English" et "Chinese"

Celles-ci n'apparaissent que lorsque `language` est English ou Chinese.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` ou `Breeze TTS 2 Multilingual`. Par défaut : `"Breeze TTS 2"`. | COMBO | Oui | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voice` | La nouvelle voix Breeze, nommée d'après la description. | BREEZE_VOICE |
| `preview` | Aperçu audio de la voix conçue. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/fr.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
