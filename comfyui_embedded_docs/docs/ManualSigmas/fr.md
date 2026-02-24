> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/fr.md)

Le nœud ManualSigmas vous permet de définir manuellement une séquence personnalisée de niveaux de bruit (sigmas) pour le processus d'échantillonnage. Vous saisissez une liste de nombres sous forme de chaîne de caractères, et le nœud les convertit en un tenseur utilisable par d'autres nœuds d'échantillonnage. Cela est utile pour des tests ou pour créer des planifications de bruit spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | STRING | Oui | Nombres séparés par des virgules ou des espaces | Une chaîne de caractères contenant les valeurs sigma. Le nœud extraira tous les nombres de cette chaîne. Par exemple : "1, 0.5, 0.1" ou "1 0.5 0.1". La valeur par défaut est "1, 0.5". |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Le tenseur contenant la séquence de valeurs sigma extraites de la chaîne d'entrée. |
