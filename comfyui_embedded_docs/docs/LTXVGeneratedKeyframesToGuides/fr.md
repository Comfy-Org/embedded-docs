# LTXV Images clés générées vers guides

Le nœud LTXV Generated Keyframes to Guides fixe les keyframes générées d'une étape antérieure comme guides d'image figés sur un canevas ultérieur. Il décode les keyframes comme des trames autonomes, les redimensionne si nécessaire et les écrit avec un masque de bruit de 0 afin qu'elles ne soient pas débruitées à nouveau. Après un upscale temporel, les indices enregistrés sont mis à l'échelle depuis le canevas sur lequel elles ont été générées vers celui-ci ; utilisez `override_frame_indices` pour définir explicitement les positions.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Conditionnement positif auquel ajouter les guides de keyframes. | CONDITIONING | Oui | |
| `negative` | Conditionnement négatif auquel ajouter les guides de keyframes. | CONDITIONING | Oui | |
| `vae` | Le VAE utilisé pour décoder les keyframes si un redimensionnement est nécessaire. | VAE | Oui | |
| `latent` | Le latent vidéo cible auquel ajouter les guides, par ex. celui ayant subi un upscale temporel. | LATENT | Oui | |
| `keyframes` | La sortie keyframes de LTXV Separate Generated Keyframes, qui porte l'indice de trame pixel auquel chaque keyframe a été générée. | LATENT | Oui | |
| `strength` | Force du guide. 1.0 correspond à un ancrage fort ; des valeurs plus faibles relâchent l'ancrage. (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 (pas 0.01) |
| `override_frame_indices` | Facultatif — fixez à ces trames pixel au lieu des positions enregistrées (ou mises à l'échelle automatiquement). Fournissez un indice par keyframe. Laissez vide pour réutiliser les positions enregistrées, ou pour les mettre à l'échelle lorsque le canevas cible a une longueur différente (par ex. après un upscale temporel x2). (par défaut : "") | STRING | Non | |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif avec les keyframes fixées comme guides d'image. | CONDITIONING |
| `negative` | Conditionnement négatif avec les keyframes fixées comme guides d'image. | CONDITIONING |
| `latent` | Latent vidéo cible avec les keyframes ajoutées comme guides figés. | LATENT |

## Remarques

- L'entrée `keyframes` doit être connectée à la sortie keyframes de LTXV Separate Generated Keyframes. Le nœud lève une erreur si le latent ne porte pas les positions des keyframes générées.
- Les entrées de conditionnement `positive` et `negative` doivent provenir des sorties positive et negative de LTXV Separate Generated Keyframes. Le nœud lève une erreur si le conditionnement positif porte encore des keyframes générées.
- L'entrée `latent` doit être un latent vidéo simple (tenseur 5D). Les guides doivent être ajoutés avant la fusion des latents vidéo et audio avec Concat AV Latent.
- Seule une taille de lot de 1 est prise en charge. Chaque guide est encodé à partir d'une image, il ne peut donc pas différer d'un élément du lot à l'autre.
- Le nombre de keyframes dans le latent `keyframes` doit correspondre au nombre de positions enregistrées ; sinon, une erreur est levée.
- Si `override_frame_indices` est laissé vide, les positions enregistrées sont utilisées. Si le canevas cible a un nombre de trames différent de celui du canevas sur lequel les keyframes ont été générées, les indices enregistrés sont mis à l'échelle automatiquement.
- Si `override_frame_indices` est fourni, il doit contenir un indice entier par keyframe, les indices étant séparés par des virgules ou des espaces. Les indices doivent être uniques et compris entre 1 et (nombre de trames pixel dans le latent cible - 1). Sinon, une erreur est levée.
- Si un indice final de keyframe est supérieur ou égal au nombre de trames pixel dans le latent cible, le nœud lève une erreur. Cela peut se produire lorsque la cible a été redimensionnée temporellement après la génération des keyframes.
- Le paramètre `strength` a un minimum de 0.0 et un maximum de 10.0.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/fr.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
