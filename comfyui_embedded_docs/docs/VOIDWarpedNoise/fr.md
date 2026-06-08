Voici la traduction en français de la documentation technique, en respectant toutes les règles spécifiées :

---

## Aperçu

Génère un bruit corrélé temporellement pour la seconde passe du processus de raffinement vidéo VOID. Il prend la vidéo de sortie de la Passe 1 et déforme le bruit gaussien le long des vecteurs de flux optique, créant un bruit qui se déplace de manière cohérente avec le contenu vidéo. Ce bruit déformé est utilisé comme latent initial pour la Passe 2, ce qui améliore la cohérence temporelle dans la sortie finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modèle de flux optique provenant d'OpticalFlowLoader (RAFT-large). | MODEL | Oui | - |
| `video` | Images vidéo de sortie de la Passe 1 [T, H, W, 3]. | IMAGE | Oui | - |
| `width` | Largeur du latent de sortie (par défaut : 672). | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `height` | Hauteur du latent de sortie (par défaut : 384). | INT | Oui | 16 à MAX_RESOLUTION (pas de 8) |
| `length` | Nombre d'images pixels. Arrondi à l'inférieur pour que `latent_t` soit pair (exigence `patch_size_t=2`), par ex. 49 → 45 (par défaut : 45). | INT | Oui | 1 à MAX_RESOLUTION (pas de 1) |
| `batch_size` | Nombre de séquences de bruit identiques à générer (par défaut : 1). | INT | Oui | 1 à 64 |

**Remarque sur le paramètre `length` :** La valeur de `length` est automatiquement arrondie à l'inférieur à la valeur valide la plus proche produisant une dimension `latent_t` paire. Cela est requis par la contrainte `patch_size_t=2` du modèle CogVideoX-Fun-V1.5. Un avertissement est enregistré lorsqu'un arrondi se produit.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `warped_noise` | Un tenseur 5D (B, C, T, H, W) contenant un bruit gaussien déformé par flux optique, prêt à être utilisé comme latent initial dans la Passe 2 de VOID. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/fr.md)

---
**Source fingerprint (SHA-256):** `a0f986e54bcc6c455220f89f5d840585a9eae081e522ea11e0ce37ab46821bd9`
