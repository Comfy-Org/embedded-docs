# Séparer les canaux audio

Le nœud SplitAudioChannels sépare un fichier audio stéréo en canaux gauche et droit individuels. Il prend une entrée audio stéréo à deux canaux et produit deux flux audio distincts, un pour le canal gauche et un pour le canal droit.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | L'entrée audio stéréo à séparer en canaux | AUDIO | Oui | - |

**Remarque :** L'entrée audio doit comporter exactement deux canaux (stéréo). Le nœud générera une erreur si l'entrée audio ne comporte qu'un seul canal.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `gauche` | Le canal gauche séparé de l'audio | AUDIO |
| `droite` | Le canal droit séparé de l'audio | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/fr.md)

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
