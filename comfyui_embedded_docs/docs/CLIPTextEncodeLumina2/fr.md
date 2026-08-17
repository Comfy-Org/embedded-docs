# CLIP Text Encode pour Lumina2

Le nœud CLIP Text Encode pour Lumina2 encode une invite système et une invite utilisateur à l'aide d'un modèle CLIP en un embedding qui peut guider le modèle de diffusion pour générer des images spécifiques. Il combine une invite système prédéfinie avec votre invite texte personnalisée et les traite via le modèle CLIP pour créer des données de conditionnement pour la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 fournit deux types d'invites système : "superior" génère des images avec un alignement image-texte supérieur ; "alignment" génère des images de haute qualité avec le plus haut degré d'alignement image-texte. | COMBO | Oui | `"superior"`<br>`"alignment"` |
| `user_prompt` | Le texte à encoder. Prend en charge la saisie multiligne et les invites dynamiques. | STRING | Oui | N/A |
| `clip` | Le modèle CLIP utilisé pour encoder le texte. | CLIP | Oui | N/A |

**Remarque :** L'entrée `clip` est requise et ne peut pas être None. Si l'entrée clip est invalide, le nœud lèvera une erreur indiquant que le checkpoint peut ne pas contenir un modèle CLIP ou un encodeur de texte valide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Un conditionnement contenant le texte intégré utilisé pour guider le modèle de diffusion. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/fr.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
