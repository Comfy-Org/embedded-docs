> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/fr.md)

Voici la traduction en français de la documentation du nœud ImageFlip :

Le nœud ImageFlip retourne les images le long de différents axes. Il peut retourner les images verticalement le long de l'axe x ou horizontalement le long de l'axe y. Le nœud utilise les opérations torch.flip pour effectuer le retournement en fonction de la méthode sélectionnée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à retourner |
| `flip_method` | STRING | Oui | "x-axis: vertically"<br>"y-axis: horizontally" | La direction de retournement à appliquer (par défaut : "x-axis: vertically") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image retournée en sortie |

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
