# ÉchantillonneurPersonnaliséAvancé

Le nœud SamplerCustomAdvanced effectue un échantillonnage avancé dans l'espace latent à l'aide de configurations personnalisées de bruit, de guidage et d'échantillonnage. Il traite une image latente via un processus d'échantillonnage guidé avec une génération de bruit personnalisable et des plannings de sigma, produisant à la fois la sortie échantillonnée finale et une version débruitée lorsque cela est disponible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `noise` | Le générateur de bruit qui fournit le motif de bruit initial et le seed pour le processus d'échantillonnage | NOISE | Oui | - |
| `guider` | Le modèle de guidage qui oriente le processus d'échantillonnage vers les sorties souhaitées | GUIDER | Oui | - |
| `sampler` | L'algorithme d'échantillonnage qui définit comment l'espace latent est parcouru pendant la génération | SAMPLER | Oui | - |
| `sigmas` | Le planning de sigma qui contrôle les niveaux de bruit tout au long des étapes d'échantillonnage | SIGMAS | Oui | - |
| `latent_image` | La représentation latente initiale qui sert de point de départ à l'échantillonnage. Prend en charge le `noise_mask` optionnel pour le débruitage sélectif, ainsi que les clés optionnelles `downscale_ratio_spacial` et `downscale_ratio_temporal` pour la gestion avancée des latents | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La représentation latente échantillonnée finale après l'achèvement du processus d'échantillonnage. Toutes les clés `downscale_ratio_spacial` ou `downscale_ratio_temporal` du latent d'entrée sont supprimées de cette sortie | LATENT |
| `denoised_output` | Une version débruitée de la sortie lorsque le processus d'échantillonnage produit une prédiction propre intermédiaire (x0), sinon renvoie la même chose que la sortie. Lorsqu'elle est disponible, elle représente la meilleure estimation du modèle du latent propre à chaque étape | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
