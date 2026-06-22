# PhotoMakerEncode

Le nœud PhotoMakerEncode traite des images et du texte pour générer des données de conditionnement destinées à la génération d'images par IA. Il prend une image de référence et un prompt textuel, puis crée des embeddings qui peuvent être utilisés pour guider la génération d'images en fonction des caractéristiques visuelles de l'image de référence. Le nœud recherche spécifiquement le token "photomaker" dans le texte pour déterminer où appliquer le conditionnement basé sur l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `photomaker` | Le modèle PhotoMaker utilisé pour traiter l'image et générer les embeddings | PHOTOMAKER | Oui | - |
| `image` | L'image de référence qui fournit les caractéristiques visuelles pour le conditionnement | IMAGE | Oui | - |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage du texte | CLIP | Oui | - |
| `texte` | Le prompt textuel pour la génération du conditionnement (par défaut : "photograph of photomaker") | STRING | Oui | - |

**Remarque :** Lorsque le texte contient le mot "photomaker", le nœud applique un conditionnement basé sur l'image à cette position dans le prompt. Si "photomaker" n'est pas trouvé dans le texte, le nœud génère un conditionnement textuel standard sans influence de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement contenant les embeddings d'image et de texte pour guider la génération d'images | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/fr.md)

---
**Source fingerprint (SHA-256):** `535fd3dbbe0e48205bebde030138ffca841dc94a18fd47db768a1066fe84bce4`
