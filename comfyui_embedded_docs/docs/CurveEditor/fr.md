> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/fr.md)

Le nœud Éditeur de Courbe fournit une interface visuelle pour ajuster et affiner une courbe. Il vous permet de modifier la forme d'une courbe d'entrée et, optionnellement, de visualiser sa distribution avec un histogramme. Le nœud renvoie la courbe modifiée pour une utilisation dans d'autres parties de votre flux de travail.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `curve` | CURVE | Oui | N/A | La courbe d'entrée à éditer. |
| `histogram` | HISTOGRAM | Non | N/A | Un histogramme optionnel à afficher à côté de la courbe pour référence visuelle. |

## Sorties

| Nom de Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `curve` | CURVE | La courbe éditée après que des ajustements ont été effectués dans l'interface du nœud. |