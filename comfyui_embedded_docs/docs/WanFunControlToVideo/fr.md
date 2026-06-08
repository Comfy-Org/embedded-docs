Ce nœud a été ajouté pour prendre en charge le modèle Alibaba Wan Fun Control pour la génération vidéo, et a été intégré après [ce commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Objectif :** Préparer les informations de conditionnement nécessaires à la génération vidéo, en utilisant le modèle Wan 2.1 Fun Control.

Le nœud WanFunControlToVideo est un ajout à ComfyUI conçu pour prendre en charge les modèles Wan Fun Control pour la génération vidéo, visant à utiliser le contrôle WanFun pour la création de vidéos.

Ce nœud sert de point de préparation pour les informations de conditionnement essentielles et initialise le point central de l'espace latent, guidant ainsi le processus de génération vidéo ultérieur à l'aide du modèle Wan 2.1 Fun. Le nom du nœud indique clairement sa fonction : il accepte diverses entrées et les convertit en un format adapté au contrôle de la génération vidéo dans le cadre de WanFun.

La position du nœud dans la hiérarchie des nœuds ComfyUI indique qu'il opère dans les premières étapes du pipeline de génération vidéo, en se concentrant sur la manipulation des signaux de conditionnement avant l'échantillonnage ou le décodage réel des trames vidéo.

## Entrées

| Nom du paramètre | Description | Requis | Type de données | Valeur par défaut |
| --- | --- | --- | --- | --- |
| positive | Données de conditionnement positif standard de ComfyUI, généralement issues d'un nœud "CLIP Text Encode". Le prompt positif décrit le contenu, le sujet et le style artistique que l'utilisateur envisage pour la vidéo générée. | Oui | CONDITIONING | N/A |
| negative | Données de conditionnement négatif standard de ComfyUI, généralement générées par un nœud "CLIP Text Encode". Le prompt négatif spécifie les éléments, styles ou artefacts que l'utilisateur souhaite éviter dans la vidéo générée. | Oui | CONDITIONING | N/A |
| vae | Nécessite un modèle VAE (Autoencodeur Variationnel) compatible avec la famille de modèles Wan 2.1 Fun, utilisé pour encoder et décoder les données image/vidéo. | Oui | VAE | N/A |
| width | La largeur souhaitée des trames vidéo de sortie en pixels, avec une valeur par défaut de 832, une valeur minimale de 16, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 16. | Oui | INT | 832 |
| height | La hauteur souhaitée des trames vidéo de sortie en pixels, avec une valeur par défaut de 480, une valeur minimale de 16, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 16. | Oui | INT | 480 |
| length | Le nombre total de trames dans la vidéo générée, avec une valeur par défaut de 81, une valeur minimale de 1, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 4. | Oui | INT | 81 |
| batch_size | Le nombre de vidéos générées en un seul lot, avec une valeur par défaut de 1, une valeur minimale de 1 et une valeur maximale de 4096. | Oui | INT | 1 |
| clip_vision_output | (Optionnel) Caractéristiques visuelles extraites par un modèle de vision CLIP, permettant un guidage du style et du contenu visuel. | Non | CLIP_VISION_OUTPUT | Aucun |
| start_image | (Optionnel) Une image initiale qui influence le début de la vidéo générée. | Non | IMAGE | Aucun |
| control_video | (Optionnel) Permet aux utilisateurs de fournir une vidéo de référence ControlNet prétraitée qui guidera le mouvement et la structure potentielle de la vidéo générée. | Non | IMAGE | Aucun |

## Sorties

| Nom du paramètre | Description | Type de données |
| --- | --- | --- |
| positive | Fournit des données de conditionnement positif améliorées, incluant l'encodage de start_image et control_video. | CONDITIONING |
| negative | Fournit des données de conditionnement négatif également améliorées, contenant le même concat_latent_image. | CONDITIONING |
| latent | Un dictionnaire contenant un tenseur latent vide avec la clé "samples". | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/fr.md)
