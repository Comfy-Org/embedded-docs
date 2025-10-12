> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

Le nœud PatchModelAddDownscale implémente la fonctionnalité Kohya Deep Shrink en appliquant des opérations de réduction et d'agrandissement à des blocs spécifiques d'un modèle. Il réduit la résolution des caractéristiques intermédiaires pendant le traitement puis les restaure à leur taille d'origine, ce qui peut améliorer les performances tout en maintenant la qualité. Le nœud permet un contrôle précis du moment et de la manière dont ces opérations de mise à l'échelle se produisent pendant l'exécution du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer le correctif de réduction d'échelle |
| `numéro de bloc` | INT | Non | 1-32 | Le numéro de bloc spécifique où la réduction d'échelle sera appliquée (par défaut : 3) |
| `facteur de réduction` | FLOAT | Non | 0.1-9.0 | Le facteur par lequel réduire les caractéristiques (par défaut : 2.0) |
| `pourcentage de départ` | FLOAT | Non | 0.0-1.0 | Le point de départ dans le processus de débruitage où commence la réduction d'échelle (par défaut : 0.0) |
| `pourcentage de fin` | FLOAT | Non | 0.0-1.0 | Le point d'arrêt dans le processus de débruitage où la réduction d'échelle s'arrête (par défaut : 0.35) |
| `réduction après saut` | BOOLEAN | Non | - | Indique s'il faut appliquer la réduction d'échelle après les connexions de saut (par défaut : True) |
| `méthode de réduction` | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | La méthode d'interpolation utilisée pour les opérations de réduction d'échelle |
| `méthode d'agrandissement` | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | La méthode d'interpolation utilisée pour les opérations d'agrandissement |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec le correctif de réduction d'échelle appliqué |
