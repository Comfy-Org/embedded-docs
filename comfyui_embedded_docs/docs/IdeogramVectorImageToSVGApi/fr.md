# Ideogram Vector Image to SVG

Ce nœud convertit une image en SVG modifiable avec Ideogram Vector. Le résultat est un balisage vectoriel plutôt qu’une image matricielle ; les formes vectorisées restent donc modifiables dans un éditeur vectoriel. Les zones transparentes d’une image avec alpha restent transparentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. Par défaut : `"ideogram-vector-1"`. | DYNAMIC_COMBO | Oui | `"ideogram-vector-1"` |
| `image` | L’image à convertir. Une entrée par lots est convertie image par image et les SVG résultants sont renvoyés ensemble. | IMAGE | Oui | - |
| `mode` | `"simple"` trace moins de formes, de plus grande taille ; `"default"` conserve davantage de détails fins. Par défaut : `"default"`. | COMBO | Oui | `"simple"`<br>`"default"` |

**Contraintes :**

* Les images dont le côté le plus long dépasse 2048 pixels sont réduites avant l’envoi.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | L’image convertie sous forme de balisage vectoriel éditable. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/fr.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`
