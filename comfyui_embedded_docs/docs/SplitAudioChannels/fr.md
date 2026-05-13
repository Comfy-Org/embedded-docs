> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/fr.md)

Le nœud SplitAudioChannels sépare un fichier audio stéréo en canaux gauche et droit individuels. Il prend une entrée audio stéréo à deux canaux et produit deux flux audio distincts, un pour le canal gauche et un pour le canal droit.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | L'entrée audio stéréo à séparer en canaux |

**Remarque :** L'entrée audio doit comporter exactement deux canaux (stéréo). Le nœud générera une erreur si l'entrée audio ne comporte qu'un seul canal.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `droite` | AUDIO | Le canal gauche séparé de l'audio |
| `right` | AUDIO | Le canal droit séparé de l'audio |

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
