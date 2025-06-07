
Ce nœud est conçu pour encoder des images en une représentation latente adaptée aux tâches d'inpainting, en intégrant des étapes de prétraitement supplémentaires pour ajuster l'image d'entrée et le masque pour un encodage optimal par le modèle VAE.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | L'image d'entrée à encoder. Cette image subit un prétraitement et un redimensionnement pour correspondre aux dimensions d'entrée attendues par le modèle VAE avant l'encodage. |
| `vae`     | VAE       | Le modèle VAE utilisé pour encoder l'image en sa représentation latente. Il joue un rôle crucial dans le processus de transformation, déterminant la qualité et les caractéristiques de l'espace latent de sortie. |
| `mask`    | `MASK`      | Un masque indiquant les régions de l'image d'entrée à inpeindre. Il est utilisé pour modifier l'image avant l'encodage, garantissant que le VAE se concentre sur les zones pertinentes. |
| `grow_mask_by` | `INT` | Spécifie dans quelle mesure étendre le masque d'inpainting pour assurer des transitions fluides dans l'espace latent. Une valeur plus grande augmente la zone affectée par l'inpainting. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie inclut la représentation latente encodée de l'image et un masque de bruit, tous deux cruciaux pour les tâches d'inpainting ultérieures. |
