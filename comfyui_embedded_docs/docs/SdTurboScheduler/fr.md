
Le SDTurboScheduler est conçu pour générer une séquence de valeurs sigma pour l'échantillonnage d'images, en ajustant la séquence en fonction du niveau de débruitage et du nombre d'étapes spécifiées. Il exploite les capacités d'échantillonnage d'un modèle spécifique pour produire ces valeurs sigma, qui sont cruciales pour contrôler le processus de débruitage lors de la génération d'images.

## Entrées

| Paramètre | Type de Donnée | Description |
| --- | --- | --- |
| `model` | `MODEL` | Le paramètre model spécifie le modèle génératif à utiliser pour la génération des valeurs sigma. Il est crucial pour déterminer le comportement d'échantillonnage spécifique et les capacités du planificateur. |
| `steps` | `INT` | Le paramètre steps détermine la longueur de la séquence sigma à générer, influençant directement la granularité du processus de débruitage. |
| `denoise` | `FLOAT` | Le paramètre denoise ajuste le point de départ de la séquence sigma, permettant un contrôle plus fin du niveau de débruitage appliqué lors de la génération d'images. |

## Sorties

| Paramètre | Type de Donnée | Description |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Une séquence de valeurs sigma générées en fonction du modèle spécifié, des étapes et du niveau de débruitage. Ces valeurs sont essentielles pour contrôler le processus de débruitage dans la génération d'images. |
