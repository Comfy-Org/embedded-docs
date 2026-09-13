# Gomme Bria

Bria Eraser supprime des objets ou des zones d'une image à l'aide de l'API Bria. Vous fournissez une image et un masque qui délimite les régions à supprimer ; le nœud téléverse les deux vers Bria, exécute la tâche d'effacement, attend qu'elle soit terminée et renvoie l'image modifiée avec les zones masquées effacées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée contenant les objets ou zones à supprimer. | IMAGE | Oui | - |
| `mask` | Les zones blanches sont effacées, les zones noires sont conservées. Le masque est binarisé avant l'envoi avec un seuil de coupure de 50 % : seules les zones peintes avec une opacité supérieure à 50 % sont considérées comme blanches. Doit avoir le même rapport d'aspect que l'image. | MASK | Oui | - |
| `mask_type` | Le type de source du masque. "manual" est destiné aux masques dessinés à la main ou au pinceau ; "automatic" est destiné aux masques produits par des modèles de segmentation tels que SAM. | COMBO | Oui | "manual"<br>"automatic" |
| `moderation` | Paramètres de modération. Défini sur "true" pour activer la modération du contenu visuel sur les images d'entrée et/ou de sortie. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

Lorsque `moderation` est défini sur "true", deux paramètres booléens supplémentaires deviennent disponibles :

- `visual_input_moderation` — applique la modération du contenu visuel à l'image d'entrée (valeur par défaut : false)
- `visual_output_moderation` — applique la modération du contenu visuel à l'image de sortie (valeur par défaut : false)

Remarque : Le masque doit avoir le même rapport d'aspect que l'image, sinon la requête échoue. Le masque est converti en masque binaire (noir et blanc) avant d'être envoyé à l'API : les zones peintes avec une opacité inférieure à la moitié sont ignorées, et les zones partiellement peintes sont traitées comme blanches et seront effacées. Le masque doit contenir au moins une zone blanche ; un masque vide fait échouer la requête car il n'y a rien à effacer.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée avec les objets ou zones masqués supprimés. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/fr.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
