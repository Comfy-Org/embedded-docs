# VOIDWarpedNoise

Génère un bruit corrélé temporellement pour la seconde passe du processus d'affinage vidéo VOID. Il prend la vidéo de sortie de la passe 1 et déforme le bruit gaussien le long des vecteurs de flux optique, afin que le bruit se déplace de manière cohérente avec le contenu de la vidéo. Le bruit déformé résultant est utilisé comme latent de départ pour la passe 2, ce qui améliore la cohérence temporelle dans la sortie finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modèle de flux optique issu de OpticalFlowLoader (RAFT-large). | OPTICAL_FLOW | Oui | - |
| `video` | Trames vidéo de sortie de la passe 1 [T, H, W, 3]. | IMAGE | Oui | - |
| `width` | Largeur cible en pixels (par défaut : 672). La vidéo d'entrée est mise à l'échelle à cette largeur avant la génération du bruit, et la largeur latente est dérivée comme width ÷ 8. | INT | Oui | 16 à MAX_RESOLUTION (pas 8) |
| `height` | Hauteur cible en pixels (par défaut : 384). La vidéo d'entrée est mise à l'échelle à cette hauteur avant la génération du bruit, et la hauteur latente est dérivée comme height ÷ 8. | INT | Oui | 16 à MAX_RESOLUTION (pas 8) |
| `length` | Nombre de trames en pixels. Arrondi à l'inférieur pour rendre latent_t pair (exigence patch_size_t=2), par ex. 49 à 45 (par défaut : 45). | INT | Oui | 1 à MAX_RESOLUTION (pas 1) |
| `batch_size` | Nombre de séquences de bruit déformé identiques à produire (par défaut : 1). Le bruit généré est répété ce nombre de fois le long de la dimension de lot. | INT | Oui | 1 à 64 |

**Remarque sur le paramètre `length` :** La valeur de `length` est automatiquement arrondie à l'inférieur à la valeur la plus proche produisant une dimension `latent_t` paire, comme l'exige la contrainte `patch_size_t=2` du modèle CogVideoX-Fun-V1.5 (par exemple, 49 devient 45). Le nœud journalise un avertissement lorsque cet arrondi se produit. Les trames au-delà du `length` ajusté sont ignorées, et le bruit est rééchantillonné selon le nombre de trames latentes résultant.

**Remarque sur `width` et `height` :** Ces valeurs sont utilisées à la fois pour redimensionner les trames vidéo entrantes (bilinéaire, recadrage centré) et pour déterminer la résolution latente finale (divisée par 8). Si le bruit généré ne correspond pas à la taille latente demandée, il est redimensionné pour s'adapter.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `warped_noise` | Un tenseur 5D (B, C, T, H, W) contenant un bruit gaussien déformé par flux optique, prêt à être utilisé comme latent initial dans la passe 2 de VOID. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/fr.md)

---
**Source fingerprint (SHA-256):** `f46b0a73b09a5d2d0bc25676f9571563c6bb8bad8d835e7564ac092c72136107`
