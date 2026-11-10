# Breeze Voice Clone

Crée une voix Breeze à partir d'un enregistrement d'un seul locuteur. La voix est enregistrée dans votre compte et renvoyée sous forme d'identifiant de voix, accompagnée d'un aperçu audio de son rendu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Enregistrement d'un seul locuteur, d'une durée minimale de 3 secondes. Seules les 60 premières secondes sont utilisées. | AUDIO | Oui | - |
| `remove_background_noise` | Nettoie l'enregistrement avant le clonage. Par défaut : false. | BOOLEAN | Non | true<br>false |
| `seed` | Contrôle si le nœud est réexécuté ; les résultats ne sont pas déterministes quelle que soit la valeur de `seed`. Par défaut : 42. | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voice` | La nouvelle voix Breeze, pour Breeze Text to Speech. | BREEZE_VOICE |
| `preview` | Aperçu audio de la voix clonée. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/fr.md)

---
**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`
