> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/fr.md)

Voici la traduction de la documentation du nœud Curve Editor, conforme à vos règles :

L'éditeur de courbe fournit une interface visuelle pour ajuster et affiner une courbe. Il permet de modifier la forme d'une courbe d'entrée et, en option, de visualiser sa distribution à l'aide d'un histogramme. Le nœud produit la courbe modifiée pour une utilisation ultérieure dans votre flux de travail.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `curve` | CURVE | Oui | N/D | La courbe d'entrée à éditer. |
| `histogram` | HISTOGRAM | Non | N/D | Un histogramme optionnel à afficher aux côtés de la courbe pour référence visuelle. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `curve` | CURVE | La courbe éditée après les ajustements effectués dans l'interface du nœud. |

---
**Source fingerprint (SHA-256):** `34cf36a5b934c44ebfce0b81e7c515f1b31fb17f3b7e1ad52255d1d72f68240b`
