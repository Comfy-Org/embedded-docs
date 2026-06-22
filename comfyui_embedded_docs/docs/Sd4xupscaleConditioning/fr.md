# Sd4xupscaleConditioning

Ce nœud est spécialisé dans l'amélioration de la résolution des images via un processus de suréchantillonnage 4x, intégrant des éléments de conditionnement pour affiner le résultat. Il exploite des techniques de diffusion pour agrandir les images tout en permettant d'ajuster le rapport d'échelle et l'augmentation du bruit afin de peaufiner le processus d'amélioration.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `images` | Les images d'entrée à suréchantillonner. Ce paramètre est crucial car il influence directement la qualité et la résolution des images de sortie. | `IMAGE` |
| `positive` | Éléments de conditionnement positifs qui guident le processus de suréchantillonnage vers les attributs ou caractéristiques souhaités dans les images de sortie. | `CONDITIONNEMENT` |
| `negative` | Éléments de conditionnement négatifs que le processus de suréchantillonnage doit éviter, aidant à orienter la sortie loin des attributs ou caractéristiques indésirables. | `CONDITIONNEMENT` |
| `scale_ratio` | Détermine le facteur d'augmentation de la résolution de l'image. Un rapport d'échelle plus élevé produit une image de sortie plus grande, permettant davantage de détails et de netteté. | `FLOAT` |
| `noise_augmentation` | Contrôle le niveau d'augmentation du bruit appliqué pendant le processus de suréchantillonnage. Cela peut être utilisé pour introduire de la variabilité et améliorer la robustesse des images de sortie. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `positive` | Les éléments de conditionnement positifs affinés résultant du processus de suréchantillonnage. | `CONDITIONNEMENT` |
| `negative` | Les éléments de conditionnement négatifs affinés résultant du processus de suréchantillonnage. | `CONDITIONNEMENT` |
| `latent` | Une représentation latente générée pendant le processus de suréchantillonnage, qui peut être utilisée dans un traitement ultérieur ou l'entraînement d'un modèle. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/fr.md)
