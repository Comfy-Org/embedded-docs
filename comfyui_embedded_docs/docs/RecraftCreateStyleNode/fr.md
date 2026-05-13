> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/fr.md)

Ce nœud crée un style personnalisé pour la génération d'images en téléchargeant des images de référence. Vous pouvez télécharger entre 1 et 5 images pour définir le nouveau style, et le nœud renverra un identifiant de style unique pouvant être utilisé avec d'autres nœuds Recraft. La taille totale combinée de tous les fichiers image téléchargés ne doit pas dépasser 5 Mo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `style` | STRING | Oui | `"realistic_image"`<br>`"digital_illustration"` | Le style de base des images générées. |
| `images` | IMAGE | Oui | 1 à 5 images | Un ensemble de 1 à 5 images de référence utilisées pour créer le style personnalisé. |

**Remarque :** La taille totale des fichiers de toutes les images dans l'entrée `images` doit être inférieure à 5 Mo. Le nœud échouera si cette limite est dépassée.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `style_id` | STRING | L'identifiant unique du style personnalisé nouvellement créé. |

---
**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`
