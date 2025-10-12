> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/fr.md)

Le nœud VAEEncodeTiled traite les images en les découpant en tuiles plus petites et en les encodant à l'aide d'un Autoencodeur Variationnel. Cette approche par tuilage permet de gérer de grandes images qui pourraient autrement dépasser les limitations de mémoire. Le nœud prend en charge à la fois les VAE d'image et de vidéo, avec des contrôles de tuilage distincts pour les dimensions spatiales et temporelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `pixels` | IMAGE | Oui | - | Les données d'image d'entrée à encoder |
| `vae` | VAE | Oui | - | Le modèle d'Autoencodeur Variationnel utilisé pour l'encodage |
| `taille_de_tuile` | INT | Oui | 64-4096 (pas: 64) | La taille de chaque tuile pour le traitement spatial (par défaut: 512) |
| `chevauchement` | INT | Oui | 0-4096 (pas: 32) | La quantité de chevauchement entre les tuiles adjacentes (par défaut: 64) |
| `taille_temporelle` | INT | Oui | 8-4096 (pas: 4) | Utilisé uniquement pour les VAE vidéo: Nombre de trames à encoder à la fois (par défaut: 64) |
| `chevauchement_temporel` | INT | Oui | 4-4096 (pas: 4) | Utilisé uniquement pour les VAE vidéo: Nombre de trames à chevaucher (par défaut: 8) |

**Note:** Les paramètres `temporal_size` et `temporal_overlap` ne sont pertinents que lors de l'utilisation de VAE vidéo et n'ont aucun effet sur les VAE d'image standard.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La représentation latente encodée de l'image d'entrée |
