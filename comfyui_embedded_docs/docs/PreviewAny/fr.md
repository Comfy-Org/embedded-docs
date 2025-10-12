> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

Le nœud PreviewAny affiche un aperçu de tout type de données d'entrée sous format texte. Il accepte n'importe quel type de données en entrée et le convertit en une représentation textuelle lisible pour visualisation. Le nœud gère automatiquement les différents types de données, y compris les chaînes de caractères, les nombres, les booléens et les objets complexes, en tentant de les sérialiser au format JSON.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `source` | ANY | Oui | Tout type de données | Accepte n'importe quel type de données d'entrée pour l'affichage d'aperçu |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| Affichage texte UI | TEXT | Affiche les données d'entrée converties en format texte dans l'interface utilisateur |
