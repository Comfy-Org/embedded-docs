# Wan 2.7 Image vers Vidéo

Le nœud Wan 2.7 Image to Video génère une vidéo à partir d'une image de première frame. Vous pouvez éventuellement fournir une image de dernière frame pour créer une transition entre les deux, ou fournir un fichier audio pour guider le mouvement et le timing de la vidéo. Le nœud utilise un modèle IA pour animer la scène en fonction de votre description textuelle.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle IA à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | `"wan2.7-i2v"` |
| `première image` | Image de la première frame. Le rapport d'aspect de la sortie est dérivé de cette image. | IMAGE | Oui | - |
| `dernière image` | Image de la dernière frame. Le modèle génère une vidéo en transition de la première à la dernière frame. | IMAGE | Non | - |
| `audio` | Audio pour piloter la génération vidéo (ex. synchronisation labiale, mouvement synchronisé sur le rythme). Durée : 2s-30s. Si aucune n'est fournie, le modèle génère automatiquement une musique de fond ou des effets sonores correspondants. | AUDIO | Non | - |
| `graine` | Graine (seed) à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `extension de prompt` | Indique si la requête doit être enrichie à l'aide de l'IA (par défaut : True). Ceci est un paramètre avancé. | BOOLEAN | Oui | True<br>False |
| `filigrane` | Indique si un filigrane généré par IA doit être ajouté au résultat (par défaut : False). Ceci est un paramètre avancé. | BOOLEAN | Oui | True<br>False |

### Entrées wan2.7-i2v

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Requête décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. | STRING | Oui | - |
| `negative_prompt` | Requête négative décrivant ce qu'il faut éviter. | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 2 à 15 |

**Remarque :** L'entrée `audio` a une contrainte de durée. Si elle est fournie, le fichier audio doit avoir une durée comprise entre 2 et 30 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
