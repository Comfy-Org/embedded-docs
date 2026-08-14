# BriaEraser

Bria Eraser supprime des objets ou des zones d’une image à l’aide de l’API Bria. Vous fournissez une image et un masque qui délimite les régions à supprimer ; le nœud télécharge les deux vers Bria, exécute la tâche d’effacement, attend son achèvement, puis renvoie l’image modifiée avec les zones masquées effacées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image d’entrée contenant les objets ou zones à supprimer. | IMAGE | Oui | - |
| `mask` | Les zones blanches sont effacées, les zones noires sont conservées. Le masque est binarisé avant l’envoi, donc les zones partiellement peintes comptent comme blanches. Il doit avoir le même rapport hauteur/largeur que l’image. | MASK | Oui | - |
| `mask_type` | Sélectionne la manière dont le masque a été créé. « manual » correspond aux masques dessinés à la main ou au pinceau ; « automatic » correspond aux masques produits par des modèles de segmentation tels que SAM. | STRING | Oui | « manual »<br>« automatic » |
| `moderation` | Paramètres de modération. Définissez « true » pour activer la modération du contenu sur les images d’entrée et/ou de sortie. | STRING | Oui | « false »<br>« true » |

Remarque : lorsque `moderation` est défini sur « true », deux paramètres booléens supplémentaires deviennent disponibles :

- `visual_input_moderation` — applique une modération visuelle du contenu à l’image d’entrée (défaut : false)
- `visual_output_moderation` — applique une modération visuelle du contenu à l’image de sortie (défaut : false)

Le masque doit correspondre au rapport hauteur/largeur de l’image, sinon la requête échoue. Le masque est converti en masque binaire (noir et blanc) avant d’être envoyé à l’API ; les zones partiellement peintes sont donc traitées comme blanches et seront effacées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image modifiée avec les objets ou zones masqués supprimés. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/fr.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
