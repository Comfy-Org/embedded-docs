> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/fr.md)

Ce nœud est spécialisé dans l'amélioration de la résolution des images via un processus de suréchantillonnage 4x, intégrant des éléments de conditionnement pour affiner le résultat. Il exploite des techniques de diffusion pour agrandir les images tout en permettant d'ajuster le rapport d'échelle et l'augmentation du bruit afin de peaufiner le processus d'amélioration.

## Entrées

| Paramètre            | Type Comfy        | Description |
|----------------------|--------------------|-------------|
| `images`             | `IMAGE`            | Les images d'entrée à suréchantillonner. Ce paramètre est crucial car il influence directement la qualité et la résolution des images de sortie. |
| `positive`           | `CONDITIONNEMENT`     | Éléments de conditionnement positifs qui guident le processus de suréchantillonnage vers les attributs ou caractéristiques souhaités dans les images de sortie. |
| `negative`           | `CONDITIONNEMENT`     | Éléments de conditionnement négatifs que le processus de suréchantillonnage doit éviter, aidant à orienter la sortie loin des attributs ou caractéristiques indésirables. |
| `scale_ratio`        | `FLOAT`            | Détermine le facteur d'augmentation de la résolution de l'image. Un rapport d'échelle plus élevé produit une image de sortie plus grande, permettant davantage de détails et de netteté. |
| `noise_augmentation` | `FLOAT`            | Contrôle le niveau d'augmentation du bruit appliqué pendant le processus de suréchantillonnage. Cela peut être utilisé pour introduire de la variabilité et améliorer la robustesse des images de sortie. |

## Sorties

| Paramètre     | Type de données | Description |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONNEMENT` | Les éléments de conditionnement positifs affinés résultant du processus de suréchantillonnage. |
| `negative`    | `CONDITIONNEMENT` | Les éléments de conditionnement négatifs affinés résultant du processus de suréchantillonnage. |
| `latent`      | `LATENT`     | Une représentation latente générée pendant le processus de suréchantillonnage, qui peut être utilisée dans un traitement ultérieur ou l'entraînement d'un modèle. |