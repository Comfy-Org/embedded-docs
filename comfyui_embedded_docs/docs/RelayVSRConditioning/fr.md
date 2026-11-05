# RelayVSRConditioning

RelayVSR Conditioning prépare le conditionnement et le latent vide pour un agrandissement vidéo RelayVSR. RelayVSR n’exécute son modèle Wan 2.2 en une étape que sur une image sur 15 du clip, plus la dernière, de sorte que le latent qu’il vous fournit ne contient que ces images clés. VSR Decode comble ensuite les images entre elles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion RelayVSR, chargé avec Load Model : `relayvsr_x2_lightx2v_int8_convrot.safetensors` ou `relayvsr_x4_int8_convrot.safetensors`. | MODEL | Oui | N/A |
| `images` | La vidéo de faible qualité à sa résolution native. Le facteur d’agrandissement du modèle détermine la taille du résultat. | IMAGE | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement qui transporte les images clés sélectionnées comme guide de faible qualité. | CONDITIONING |
| `latent` | Latent vide avec une image par image clé, prêt pour l’échantillonneur. | LATENT |

## Utilisation

Connectez `positive` à l’entrée positive de l’échantillonneur, puis échantillonnez le `latent` avec une étape à CFG 1 : il n’y a ni prompt ni encodeur de texte dans le graphe. Envoyez la sortie de l’échantillonneur, les mêmes `images` et un RelayVSR Flash VAE dans VSR Decode, et conservez l’appariement : le modèle x2 avec le décodeur x2, le modèle x4 avec le décodeur x4.

Seules les images clés sont échantillonnées, donc un clip de 150 images devient un latent de 11 images. L’échantillonneur travaille sur une petite fraction de la vidéo, et VSR Decode restaure le reste.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
