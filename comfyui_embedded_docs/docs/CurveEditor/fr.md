# Éditeur de courbe

Le nœud Curve Editor fournit une interface visuelle pour ajuster et affiner une courbe. Il vous permet de modifier la forme d'une courbe d'entrée et, en option, de visualiser sa distribution à l'aide d'un histogramme. Le nœud renvoie la courbe modifiée pour une utilisation dans d'autres parties de votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `curve` | La courbe d'entrée à modifier. | CURVE | Oui | N/A |
| `histogram` | Un histogramme facultatif à afficher à côté de la courbe pour référence visuelle. | HISTOGRAM | Non | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `curve` | La courbe modifiée après les ajustements effectués dans l'interface du nœud. | CURVE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/fr.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
