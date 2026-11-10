# Breeze Text to Speech

Convertit du texte en parole avec Breeze TTS 2. Choisissez une voix Breeze, sélectionnez la langue du texte et, facultativement, dirigez la manière dont la ligne est interprétée. L’anglais et le chinois peuvent utiliser l’un ou l’autre des modèles Breeze TTS 2 ; toutes les autres langues utilisent Breeze TTS 2 Multilingual.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voice` | Voix Breeze à utiliser pour la parole, issue de Breeze Voice Selector ou de l’un des nœuds de création de voix Breeze. | BREEZE_VOICE | Oui | - |
| `text` | Texte à prononcer, de 1 à 1000 caractères. Les balises audio telles que `(laughs)` ou `(sighs)` sont interprétées au lieu d’être lues. Par défaut : vide. | STRING | Oui | 1 à 1000 caractères |
| `language` | Langue du texte. L’anglais et le chinois peuvent utiliser l’un ou l’autre des modèles ; les autres langues utilisent Breeze TTS 2 Multilingual. Une voix sonne mieux dans sa propre langue ; pour une autre langue, utilisez une copie créée avec Breeze Voice Localize. | DYNAMIC_COMBO | Oui | Plusieurs options disponibles |
| `delivery` | Comment la ligne est interprétée : `neutral` conserve la voix telle quelle, `directed` suit les instructions écrites. Par défaut : `"neutral"`. | DYNAMIC_COMBO | Oui | `"neutral"`<br>`"directed"` |
| `speed` | Multiplicateur de tempo qui laisse la hauteur inchangée. Par défaut : 1.0. | FLOAT | Non | 0.5 à 2.0 (pas : 0.05) |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Non | 0 à 2147483647 |

### Entrées pour les langues « English » et « Chinese »

Ces entrées apparaissent uniquement lorsque `language` correspond à English ou Chinese.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` ou `Breeze TTS 2 Multilingual`. Par défaut : `"Breeze TTS 2"`. | COMBO | Oui | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Entrées pour l’interprétation « neutral »

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `speaker_boost` | Garde la voix plus proche de son son d’origine. Par défaut : false. | BOOLEAN | Non | true<br>false |

### Entrées pour l’interprétation « directed »

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `instructions` | Comment interpréter le texte, rédigé dans la même langue que le texte. Par défaut : vide. | STRING | Non | Texte multiligne |
| `strength` | Force avec laquelle la voix suit les instructions. Par défaut : 4.0. | FLOAT | Non | 1.0 à 10.0 (pas : 0.1) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | La parole générée sous forme d’audio WAV. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`
