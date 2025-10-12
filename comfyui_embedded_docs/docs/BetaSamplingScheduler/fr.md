> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/fr.md)

Le nœud BetaSamplingScheduler génère une séquence de niveaux de bruit (sigmas) pour le processus d'échantillonnage en utilisant un algorithme de planification bêta. Il prend un modèle et des paramètres de configuration pour créer une planification de bruit personnalisée qui contrôle le processus de débruitage pendant la génération d'image. Ce planificateur permet un réglage fin de la trajectoire de réduction du bruit grâce aux paramètres alpha et bêta.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `modèle` | MODEL | Requis | - | - | Le modèle utilisé pour l'échantillonnage, qui fournit l'objet d'échantillonnage du modèle |
| `étapes` | INT | Requis | 20 | 1-10000 | Le nombre d'étapes d'échantillonnage pour lesquelles générer les sigmas |
| `alpha` | FLOAT | Requis | 0.6 | 0.0-50.0 | Paramètre alpha pour le planificateur bêta, contrôlant la courbe de planification |
| `beta` | FLOAT | Requis | 0.6 | 0.0-50.0 | Paramètre bêta pour le planificateur bêta, contrôlant la courbe de planification |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Une séquence de niveaux de bruit (sigmas) utilisée pour le processus d'échantillonnage |