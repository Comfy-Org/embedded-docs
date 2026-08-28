# PhotoMakerEncode

Le nœud PhotoMakerEncode combine une image de référence avec un prompt texte pour créer des données de conditionnement destinées à la génération d’images. Lorsque le texte contient le mot « photomaker », le nœud utilise le modèle PhotoMaker pour insérer l’identité visuelle de l’image de référence dans le conditionnement à cette position du prompt.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `photomaker` | Le modèle PhotoMaker utilisé pour traiter l’image de référence et générer des embeddings basés sur l’image | PHOTOMAKER | Oui | - |
| `image` | L’image de référence qui fournit les caractéristiques visuelles pour le conditionnement | IMAGE | Oui | - |
| `clip` | Le modèle CLIP utilisé pour la tokenisation du texte et l’encodage du texte | CLIP | Oui | - |
| `texte` | Le prompt texte pour la génération du conditionnement. Prend en charge les textes multilignes et les prompts dynamiques (par défaut : « photograph of photomaker ») | STRING | Oui | Toute chaîne |

**Remarque :** Lorsque le texte contient « photomaker » comme mot autonome, le nœud supprime ce mot du prompt encodé et applique l’identité de l’image de référence à cette position à l’aide du modèle PhotoMaker. Si « photomaker » est introuvable dans le texte, le nœud renvoie un conditionnement texte standard sans influence de l’image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement contenant les embeddings de texte et d’image qui guident la génération d’images, ainsi que la sortie poolée de l’encodeur de texte CLIP | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/fr.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
