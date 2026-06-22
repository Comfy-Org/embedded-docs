# Créer un style Recraft

Ce nœud crée un style personnalisé pour la génération d'images en téléchargeant des images de référence. Vous pouvez télécharger entre 1 et 5 images pour définir le nouveau style, et le nœud renverra un identifiant de style unique pouvant être utilisé avec d'autres nœuds Recraft. La taille totale combinée de tous les fichiers image téléchargés ne doit pas dépasser 5 Mo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `style` | Le style de base des images générées. | STRING | Oui | `"realistic_image"`<br>`"digital_illustration"` |
| `images` | Un ensemble de 1 à 5 images de référence utilisées pour créer le style personnalisé. | IMAGE | Oui | 1 à 5 images |

**Remarque :** La taille totale des fichiers de toutes les images dans l'entrée `images` doit être inférieure à 5 Mo. Le nœud échouera si cette limite est dépassée.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `style_id` | L'identifiant unique du style personnalisé nouvellement créé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/fr.md)

---
**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`
