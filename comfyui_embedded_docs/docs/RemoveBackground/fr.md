# Supprimer l’arrière-plan

Voici la traduction de la documentation technique du nœud Remove Background, conforme à vos règles :

## Aperçu

Le nœud Remove Background utilise un modèle de suppression d'arrière-plan pour générer un masque qui sépare le sujet principal de l'arrière-plan d'une image d'entrée. Il prend une image et un modèle de suppression d'arrière-plan, puis produit un masque mettant en évidence le sujet principal.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image d'entrée dont il faut supprimer l'arrière-plan | IMAGE | Oui | N/A |
| `modèle_de_suppression_arrière-plan` | Modèle de suppression d'arrière-plan utilisé pour générer le masque | BACKGROUND_REMOVAL_MODEL | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `masque` | Masque de premier plan généré qui met en évidence le sujet principal de l'image d'entrée | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/fr.md)

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
