# VSR Decode

VSR Decode transforme les latents d’images clés de RelayVSR Conditioning en une vidéo complète avec le décodeur RelayVSR Flash. Le décodeur ajoute ses détails par-dessus un agrandissement bicubique des images de basse qualité que vous fournissez, selon le facteur x2 ou x4 du décodeur. Le nombre d’images reste inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | Le décodeur RelayVSR Flash, chargé avec Load VAE : `relayvsr_flash_vae_x2_fp32.safetensors` ou `relayvsr_flash_vae_x4_fp32.safetensors`. Le facteur d’agrandissement est défini par les métadonnées du fichier ; il doit donc correspondre au modèle. | VAE | Oui | N/A |
| `samples` | Le latent renvoyé par l’échantillonneur, contenant une image par image clé. | LATENT | Oui | N/A |
| `images` | La même vidéo de basse qualité que celle fournie à RelayVSR Conditioning. | IMAGE | Oui | N/A |
| `detail` | Part de détail du décodeur conservée par-dessus l’agrandissement bicubique : 1 correspond à la sortie complète du modèle, 0 à l’agrandissement simple. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | La vidéo agrandie avec chaque image restaurée. | IMAGE |

## Remarques

- Passez la même vidéo de basse qualité aux deux nœuds. Le décodeur la lit image par image ; une différence de longueur ou de résolution donne donc un résultat incorrect ou corrompu.
- Réduire `detail` adoucit le détail restauré et rapproche la sortie d’un simple agrandissement bicubique, ce qui peut aider sur des sources très bruitées.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/fr.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
