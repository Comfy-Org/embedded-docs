# HeyGen Voice 1.0 Instant Clone Text to Speech

Clone une voix à partir de l’enregistrement d’un seul locuteur, puis prononce un texte avec cette voix grâce à HeyGen Voice 1.0. Le nœud téléverse l’enregistrement, synthétise la parole et la renvoie sous forme audio ; ainsi, un seul nœud permet de passer d’un échantillon vocal à une parole finalisée.

La sélection d’un `model` révèle les paramètres qui lui sont propres : `audio`, `text`, `language`, `expressiveness_boost`, `recording_language`, `similarity`, `remove_background_noise` et `seed`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. `heygen-voice-1-turbo` est plus rapide et coûte moins cher (par défaut : `"heygen-voice-1"`). | DYNAMIC_COMBO | Oui | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | Enregistrement d’un seul locuteur à cloner. Utilisez au moins 10 secondes de parole claire ; seules les 3 premières minutes sont utilisées. | AUDIO | Oui | - |
| `text` | Texte à prononcer, jusqu’à 5000 caractères. Une synthèse de plus d’environ 12 minutes échoue ; divisez donc les textes très longs en chinois ou en japonais (par défaut : vide). | STRING | Oui | 1 à 5000 caractères |
| `language` | Langue du texte. Définissez-la pour des langues proches comme le serbe ou le malais, que la détection automatique peut confondre (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>Plusieurs préréglages de langue |
| `expressiveness_boost` | Des valeurs plus élevées sont plus expressives ; des valeurs plus faibles restent plus proches de la voix d’origine (par défaut : 0.5). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.05) |
| `recording_language` | Langue parlée dans l’enregistrement, ce qui limite le clonage à cette langue (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>Plusieurs préréglages de langue |
| `similarity` | Degré de fidélité de la voix à l’enregistrement (par défaut : `"max"`). | COMBO | Oui | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Nettoie le bruit de fond dans l’enregistrement avant le clonage (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `seed` | La graine contrôle si le nœud se réexécute ; les résultats ne sont pas déterministes quelle que soit la graine (par défaut : 42). | INT | Oui | 0 à 2147483647 |

`text` doit contenir au moins un caractère et `audio` est obligatoire : un enregistrement de plusieurs locuteurs, ou trop bruyant pour être cloné, donne une mauvaise voix. Définissez `recording_language` lorsque la langue de l’échantillon n’est pas évidente.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | Le texte prononcé avec la voix clonée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/fr.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`
