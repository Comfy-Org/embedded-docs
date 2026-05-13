> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/fr.md)

Voici la traduction en français de la documentation du nœud CLIPTextEncodeLumina2 :

Le nœud CLIP Text Encode pour Lumina2 encode une invite système et une invite utilisateur à l'aide d'un modèle CLIP en un embedding qui peut guider le modèle de diffusion pour générer des images spécifiques. Il combine une invite système prédéfinie avec votre invite texte personnalisée et les traite via le modèle CLIP pour créer des données de conditionnement destinées à la génération d'images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `system_prompt` | STRING | Oui | `"superior"`<br>`"alignment"` | Lumina2 propose deux types d'invites système : "superior" génère des images avec un alignement image-texte supérieur ; "alignment" génère des images de haute qualité avec le plus haut degré d'alignement image-texte. |
| `user_prompt` | STRING | Oui | N/A | Le texte à encoder. Prend en charge la saisie multiligne et les invites dynamiques. |
| `clip` | CLIP | Oui | N/A | Le modèle CLIP utilisé pour encoder le texte. |

**Remarque :** L'entrée `clip` est requise et ne peut pas être nulle. Si l'entrée clip est invalide, le nœud générera une erreur indiquant que le point de contrôle peut ne pas contenir un modèle CLIP ou un encodeur de texte valide.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Un conditionnement contenant le texte encodé utilisé pour guider le modèle de diffusion. |

---
**Source fingerprint (SHA-256):** `fcc0802180ffc2c0757b395850d54632da011473da0c6b1c5268b42da3747024`
