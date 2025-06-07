Ce noeud a été ajouté pour prendre en charge le modèle Wan Fun Control d'Alibaba pour la génération vidéo, et a été ajouté après [ce commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Objectif :** Préparer les informations conditionnelles nécessaires à la génération vidéo, en utilisant le modèle Wan 2.1 Fun Control.

Le noeud WanFunControlToVideo est un ajout à ComfyUI conçu pour prendre en charge les modèles Wan Fun Control pour la génération vidéo, visant à utiliser le contrôle WanFun pour la création vidéo.

Ce noeud sert de point de préparation pour les informations conditionnelles essentielles et initialise le point central de l'espace latent, guidant le processus de génération vidéo ultérieur en utilisant le modèle Wan 2.1 Fun. Le nom du noeud indique clairement sa fonction : il accepte diverses entrées et les convertit en un format adapté pour contrôler la génération vidéo dans le cadre de WanFun.

La position du noeud dans la hiérarchie des noeuds ComfyUI indique qu'il opère aux premières étapes du pipeline de génération vidéo, se concentrant sur la manipulation des signaux conditionnels avant l'échantillonnage ou le décodage réel des cadres vidéo.

## Entrées

| Nom du paramètre    | Requis  | Type de données      | Description                                                  | Valeur par défaut |
|:-------------------|:--------|:--------------------|:-------------------------------------------------------------|:------------------|
| positif            | Oui     | CONDITIONING        | Données conditionnelles positives standard de ComfyUI, généralement provenant d'un noeud "CLIP Text Encode". L'invite positive décrit le contenu, le sujet et le style artistique que l'utilisateur envisage pour la vidéo générée. | N/A  |
| négatif            | Oui     | CONDITIONING        | Données conditionnelles négatives standard de ComfyUI, généralement générées par un noeud "CLIP Text Encode". L'invite négative spécifie les éléments, styles ou artefacts que l'utilisateur souhaite éviter dans la vidéo générée. | N/A  |
| vae                | Oui     | VAE                 | Nécessite un modèle VAE (Autoencodeur Variationnel) compatible avec la famille de modèles Wan 2.1 Fun, utilisé pour encoder et décoder des données image/vidéo. | N/A  |
| largeur            | Oui     | INT                 | La largeur souhaitée des cadres vidéo de sortie en pixels, avec une valeur par défaut de 832, une valeur minimale de 16, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 16. | 832  |
| hauteur            | Oui     | INT                 | La hauteur souhaitée des cadres vidéo de sortie en pixels, avec une valeur par défaut de 480, une valeur minimale de 16, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 16. | 480  |
| longueur           | Oui     | INT                 | Le nombre total de cadres dans la vidéo générée, avec une valeur par défaut de 81, une valeur minimale de 1, une valeur maximale déterminée par nodes.MAX_RESOLUTION, et un pas de 4. | 81   |
| taille_du_lot      | Oui     | INT                 | Le nombre de vidéos générées dans un seul lot, avec une valeur par défaut de 1, une valeur minimale de 1, et une valeur maximale de 4096. | 1    |
| clip_vision_output | Non     | CLIP_VISION_OUTPUT  | (Optionnel) Caractéristiques visuelles extraites par un modèle de vision CLIP, permettant une guidance de style et de contenu visuel. | Aucun |
| start_image        | Non     | IMAGE               | (Optionnel) Une image initiale qui influence le début de la vidéo générée. | Aucun |
| control_video      | Non     | IMAGE               | (Optionnel) Permet aux utilisateurs de fournir une vidéo de référence prétraitée par ControlNet qui guidera le mouvement et la structure potentielle de la vidéo générée.| Aucun |

### Paramètres de sortie

| Nom du paramètre    | Type de données      | Description                                                  |
|:-------------------|:--------------------|:-------------------------------------------------------------|
| positif            | CONDITIONING        | Fournit des données conditionnelles positives améliorées, y compris l'image start_image et control_video encodées. |
| négatif            | CONDITIONING        | Fournit des données conditionnelles négatives qui ont également été améliorées, contenant la même concat_latent_image. |
| latent             | LATENT              | Un dictionnaire contenant un tenseur latent vide avec la clé "samples". |
