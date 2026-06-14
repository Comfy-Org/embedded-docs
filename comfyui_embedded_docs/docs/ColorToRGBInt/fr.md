Le nœud ColorToRGBInt convertit une couleur spécifiée au format hexadécimal en une valeur entière unique. Il prend une chaîne de couleur comme `#FF5733` et calcule l'entier RVB correspondant en combinant les composantes rouge, verte et bleue.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `couleur` | Une valeur de couleur au format hexadécimal `#RRGGBB`. | STRING | Oui | N/A |

**Remarque :** La chaîne `color` en entrée doit comporter exactement 7 caractères et commencer par le symbole `#`, suivie de six chiffres hexadécimaux (par exemple, `#FF0000` pour le rouge). Le nœud générera une erreur si le format est incorrect.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `hex` | La valeur entière RVB calculée. Elle est obtenue à partir de la formule : `(Rouge * 65536) + (Vert * 256) + Bleu`. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/fr.md)

---
**Source fingerprint (SHA-256):** `5b8617d6b28caaa5f01dad1c6a302fa321f1bd53a0454451d468e36747e70e8f`
