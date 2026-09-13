# LTXV Ajouter un guide latent

Le nœud LTXV Add Latent Guide fixe un latent déjà encodé comme guide, pour les cas où le guide provient d'une étape antérieure plutôt que d'une image. Il a le même effet que LTXV Add Guide sans l'aller-retour de décodage/encodage VAE. Un guide spatialement plus petit que la cible (une référence IC-LoRA ou de détaillage) est dilaté sur une grille clairsemée, et ses positions de fin RoPE sont étendues du même ratio afin qu'il couvre le canevas cible au lieu de ne s'adresser qu'au coin supérieur gauche de celui-ci.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Entrée de conditionnement positif. | CONDITIONING | Oui | N/A |
| `negative` | Entrée de conditionnement négatif. | CONDITIONING | Oui | N/A |
| `vae` | Modèle VAE utilisé pour lire la formule d'indice de sous-échantillonnage pour le placement des trames. | VAE | Oui | N/A |
| `latent` | Latent vidéo cible sur lequel le guide est fixé. | LATENT | Oui | N/A |
| `guiding_latent` | Latent guide. Sa taille spatiale doit diviser celle de la cible par le même nombre entier sur les deux axes ; une taille égale le fixe tel quel, une taille de moitié est traitée comme une référence IC-LoRA x2. | LATENT | Oui | N/A |
| `latent_idx` | Indice de trame latente où commencer le guide, compté en trames latentes plutôt qu'en trames de pixels. Les valeurs négatives placent le guide sur des trames avant le début du latent, sans être comptées à rebours depuis sa fin. Valeur par défaut : 0. | INT | Oui | -9999 à 9999 |
| `strength` | Plafonné à 1.0. Un guide dilaté marque ses positions de remplissage avec un masque de débruitage négatif afin que le modèle les abandonne ; au-delà de 1.0, les positions conservées deviendraient également négatives et tout le guide serait abandonné. Amplifiez au-delà de 1.0 avec `attention_mask` à la place. Valeur par défaut : 1.0. | FLOAT | Oui | 0.0 à 1.0, pas 0.01 |
| `attention_mask` | Masque spatial optionnel dans l'espace des pixels. Contrôle l'influence du conditionnement par région via l'auto-attention, multipliée par `strength`. | MASK | Non | N/A |

### Remarques

- Les deux `latent` et `guiding_latent` doivent être des latents vidéo 5D de forme (batch, channels, frames, height, width).
- Le guide doit tenir à l'intérieur du latent cible : le nombre de trames du guide ajouté à `latent_idx` ne doit pas dépasser la fin du latent cible. Les valeurs négatives de `latent_idx` sont autorisées et placent le guide avant le début du latent.
- La taille spatiale du guide doit diviser la taille spatiale de la cible par un nombre entier sur les deux axes, hauteur et largeur.
- Le ratio de hauteur et le ratio de largeur doivent être la même valeur (un ratio carré). Un ratio non carré déclenche une erreur, car la dilatation et le placement RoPE utilisent un seul facteur de réduction d'échelle pour les deux axes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif avec le guide attaché. | CONDITIONING |
| `negative` | Conditionnement négatif avec le guide attaché. | CONDITIONING |
| `latent` | Sortie latente avec le guide appliqué, incluant le `noise_mask` mis à jour. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/fr.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
