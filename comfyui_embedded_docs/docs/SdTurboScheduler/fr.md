> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/fr.md)

SDTurboScheduler est conçu pour générer une séquence de valeurs sigma pour l'échantillonnage d'images, en ajustant la séquence en fonction du niveau de débruitage et du nombre d'étapes spécifiées. Il exploite les capacités d'échantillonnage d'un modèle spécifique pour produire ces valeurs sigma, qui sont essentielles pour contrôler le processus de débruitage lors de la génération d'images.

## Entrées

| Paramètre | Type de données | Description |
| --- | --- | --- |
| `modèle` | `MODEL` | Le paramètre model spécifie le modèle génératif à utiliser pour la génération des valeurs sigma. Il est crucial pour déterminer le comportement d'échantillonnage spécifique et les capacités du planificateur. |
| `étapes` | `INT` | Le paramètre steps détermine la longueur de la séquence sigma à générer, influençant directement la granularité du processus de débruitage. |
| `débruitage` | `FLOAT` | Le paramètre denoise ajuste le point de départ de la séquence sigma, permettant un contrôle plus précis du niveau de débruitage appliqué lors de la génération d'images. |

## Sorties

| Paramètre | Type de données | Description |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Une séquence de valeurs sigma générées en fonction du modèle, des étapes et du niveau de débruitage spécifiés. Ces valeurs sont essentielles pour contrôler le processus de débruitage dans la génération d'images. |