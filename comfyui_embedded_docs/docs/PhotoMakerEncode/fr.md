# PhotoMakerEncode

---

PhotoMakerEncode crée des données de conditionnement pour la génération d'images IA en combinant une image de référence avec un prompt texte. Il recherche le mot « photomaker » dans le prompt texte et, lorsqu'il le trouve, utilise le modèle PhotoMaker pour appliquer les caractéristiques visuelles de l'image de référence à cette position dans le prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `photomaker` | Le modèle PhotoMaker utilisé pour traiter l'image de référence et générer des embeddings basés sur l'image | PHOTOMAKER | Oui | - |
| `image` | L'image de référence qui fournit les caractéristiques visuelles pour le conditionnement | IMAGE | Oui | - |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte | CLIP | Oui | - |
| `text` | Le prompt texte pour la génération du conditionnement. Prend en charge plusieurs lignes et des prompts dynamiques (défaut : "photograph of photomaker") | STRING | Oui | - |

**Remarque :** Le mot « photomaker » doit apparaître comme un mot séparé dans le prompt texte (la correspondance est sensible à la casse) pour que le conditionnement basé sur l'image soit appliqué. Lorsqu'il est présent, les caractéristiques de l'image sont injectées à cette position dans le prompt. Si « photomaker » n'est pas trouvé, le nœud renvoie un conditionnement texte standard sans influence de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement contenant les embeddings d'image et de texte pour guider la génération d'images, ainsi que la sortie regroupée (pooled output) de l'encodeur de texte CLIP | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/fr.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
