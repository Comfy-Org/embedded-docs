# BriaEraser

Bria Eraser supprime des objets ou des zones d'une image à l'aide de l'API Bria. Vous fournissez une image et un masque qui délimite les régions à supprimer ; le nœud télécharge les deux sur Bria, exécute la tâche d'effacement, attend qu'elle se termine et renvoie l'image modifiée avec les zones masquées effacées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée contenant les objets ou les zones à supprimer. | IMAGE | Oui | - |
| `masque` | Les zones blanches sont effacées, les zones noires sont préservées. Le masque est binarisé avant l'envoi, donc les zones partiellement peintes sont considérées comme blanches. Doit avoir le même rapport hauteur/largeur que l'image. | MASK | Oui | - |
| `mask_type` | Sélectionne la façon dont le masque a été créé. « manual » est destiné aux masques dessinés à la main ou au pinceau ; « automatic » est destiné aux masques produits par des modèles de segmentation tels que SAM. | COMBO | Oui | "manual"<br>"automatic" |
| `modération` | Paramètres de modération. Réglez sur « true » pour activer la modération du contenu visuel sur les images d'entrée et/ou de sortie. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

Remarque : lorsque `moderation` est défini sur « true », deux paramètres booléens supplémentaires deviennent disponibles :

- `visual_input_moderation` — applique la modération du contenu visuel à l'image d'entrée (défaut : false)
- `visual_output_moderation` — applique la modération du contenu visuel à l'image de sortie (défaut : false)

Le masque doit correspondre au rapport hauteur/largeur de l'image, sinon la requête échoue. Le masque est converti en masque binaire (noir et blanc) avant d'être envoyé à l'API : les zones peintes à moins de 50 % d'opacité sont ignorées et les zones partiellement peintes sont considérées comme blanches et seront effacées. Le masque doit contenir au moins une zone blanche ; un masque vide entraîne l'échec de la requête car il n'y a rien à effacer.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée avec les objets ou les zones masqués supprimés. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/fr.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
