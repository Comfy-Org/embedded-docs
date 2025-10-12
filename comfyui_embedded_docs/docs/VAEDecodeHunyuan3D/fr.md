> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/fr.md)

Le nœud VAEDecodeHunyuan3D convertit des représentations latentes en données voxel 3D à l'aide d'un décodeur VAE. Il traite les échantillons latents via le modèle VAE avec des paramètres configurables de découpage et de résolution pour générer des données volumétriques adaptées aux applications 3D.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Oui | - | La représentation latente à décoder en données voxel 3D |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour décoder les échantillons latents |
| `num_chunks` | INT | Oui | 1000-500000 | Le nombre de segments pour diviser le traitement afin de gérer la mémoire (par défaut : 8000) |
| `octree_resolution` | INT | Oui | 16-512 | La résolution de la structure d'octree utilisée pour la génération de voxels 3D (par défaut : 256) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `voxels` | VOXEL | Les données voxel 3D générées à partir de la représentation latente décodée |