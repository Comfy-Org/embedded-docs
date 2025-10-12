> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/fr.md)

Le nœud ModelMergeWAN2_1 fusionne deux modèles en mélangeant leurs composants à l'aide de moyennes pondérées. Il prend en charge différentes tailles de modèles, y compris les modèles 1,3B avec 30 blocs et les modèles 14B avec 40 blocs, avec un traitement spécial pour les modèles image vers vidéo qui incluent un composant supplémentaire d'incorporation d'image. Chaque composant des modèles peut être individuellement pondéré pour contrôler le ratio de mélange entre les deux modèles d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Second modèle à fusionner |
| `patch_embedding.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation de patch (par défaut : 1.0) |
| `time_embedding.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation temporelle (par défaut : 1.0) |
| `time_projection.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant de projection temporelle (par défaut : 1.0) |
| `text_embedding.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation de texte (par défaut : 1.0) |
| `img_emb.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation d'image, utilisé dans les modèles image vers vidéo (par défaut : 1.0) |
| `blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 0 (par défaut : 1.0) |
| `blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 1 (par défaut : 1.0) |
| `blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 2 (par défaut : 1.0) |
| `blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 3 (par défaut : 1.0) |
| `blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 4 (par défaut : 1.0) |
| `blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 5 (par défaut : 1.0) |
| `blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 6 (par défaut : 1.0) |
| `blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 7 (par défaut : 1.0) |
| `blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 8 (par défaut : 1.0) |
| `blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 9 (par défaut : 1.0) |
| `blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 10 (par défaut : 1.0) |
| `blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 11 (par défaut : 1.0) |
| `blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 12 (par défaut : 1.0) |
| `blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 13 (par défaut : 1.0) |
| `blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 14 (par défaut : 1.0) |
| `blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 15 (par défaut : 1.0) |
| `blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 16 (par défaut : 1.0) |
| `blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 17 (par défaut : 1.0) |
| `blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 18 (par défaut : 1.0) |
| `blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 19 (par défaut : 1.0) |
| `blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 20 (par défaut : 1.0) |
| `blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 21 (par défaut : 1.0) |
| `blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 22 (par défaut : 1.0) |
| `blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 23 (par défaut : 1.0) |
| `blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 24 (par défaut : 1.0) |
| `blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 25 (par défaut : 1.0) |
| `blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 26 (par défaut : 1.0) |
| `blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 27 (par défaut : 1.0) |
| `blocks.28.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 28 (par défaut : 1.0) |
| `blocks.29.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 29 (par défaut : 1.0) |
| `blocks.30.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 30 (par défaut : 1.0) |
| `blocks.31.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 31 (par défaut : 1.0) |
| `blocks.32.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 32 (par défaut : 1.0) |
| `blocks.33.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 33 (par défaut : 1.0) |
| `blocks.34.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 34 (par défaut : 1.0) |
| `blocks.35.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 35 (par défaut : 1.0) |
| `blocks.36.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 36 (par défaut : 1.0) |
| `blocks.37.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 37 (par défaut : 1.0) |
| `blocks.38.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 38 (par défaut : 1.0) |
| `blocks.39.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 39 (par défaut : 1.0) |
| `head.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant de tête (par défaut : 1.0) |

**Note :** Tous les paramètres de poids utilisent une plage de 0.0 à 1.0 avec des incréments de 0.01. Le nœud prend en charge jusqu'à 40 blocs pour s'adapter aux différentes tailles de modèles, où les modèles 1,3B utilisent 30 blocs et les modèles 14B utilisent 40 blocs. Le paramètre `img_emb.` est spécifiquement destiné aux modèles image vers vidéo.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les composants des deux modèles d'entrée selon les poids spécifiés |
