
Ce nœud est spécialisé dans l'amélioration de la résolution des images grâce à un processus de mise à l'échelle 4x, en intégrant des éléments de conditionnement pour affiner le résultat. Il utilise des techniques de diffusion pour mettre à l'échelle les images tout en permettant l'ajustement du ratio d'échelle et l'augmentation du bruit pour affiner le processus d'amélioration.

## Entrées

| Paramètre            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `images`             | `IMAGE`            | Les images d'entrée à mettre à l'échelle. Ce paramètre est crucial car il influence directement la qualité et la résolution des images de sortie. |
| `positive`           | `CONDITIONING`     | Éléments de conditionnement positifs qui guident le processus de mise à l'échelle vers les attributs ou caractéristiques souhaités dans les images de sortie. |
| `negative`           | `CONDITIONING`     | Éléments de conditionnement négatifs que le processus de mise à l'échelle doit éviter, aidant à orienter la sortie loin des attributs ou caractéristiques indésirables. |
| `scale_ratio`        | `FLOAT`            | Détermine le facteur par lequel la résolution de l'image est augmentée. Un ratio d'échelle plus élevé se traduit par une image de sortie plus grande, permettant plus de détails et de clarté. |
| `noise_augmentation` | `FLOAT`            | Contrôle le niveau d'augmentation du bruit appliqué pendant le processus de mise à l'échelle. Cela peut être utilisé pour introduire de la variabilité et améliorer la robustesse des images de sortie. |

## Sorties

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Les éléments de conditionnement positifs raffinés résultant du processus de mise à l'échelle. |
| `negative`    | `CONDITIONING` | Les éléments de conditionnement négatifs raffinés résultant du processus de mise à l'échelle. |
| `latent`      | `LATENT`     | Une représentation latente générée pendant le processus de mise à l'échelle, qui peut être utilisée dans un traitement ultérieur ou pour l'entraînement du modèle. |
