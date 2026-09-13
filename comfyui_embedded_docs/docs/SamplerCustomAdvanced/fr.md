# ÉchantillonneurPersonnaliséAvancé

Le nœud SamplerCustomAdvanced effectue un échantillonnage avancé dans l'espace latent à l'aide de configurations personnalisées de bruit, de guidage et d'échantillonnage. Il traite une image latente via un processus d'échantillonnage guidé avec un générateur de bruit et un programme de sigmas personnalisables, produisant à la fois la sortie échantillonnée finale et une version débruitée lorsqu'elle est disponible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `noise` | Le générateur de bruit qui fournit le motif de bruit initial et la graine pour le processus d'échantillonnage | NOISE | Oui | - |
| `guider` | Le modèle de guidage qui oriente le processus d'échantillonnage vers la sortie souhaitée | GUIDER | Oui | - |
| `sampler` | L'algorithme d'échantillonnage qui définit comment l'espace latent est parcouru pendant la génération | SAMPLER | Oui | - |
| `sigmas` | Le programme de sigmas qui contrôle les niveaux de bruit tout au long des étapes d'échantillonnage | SIGMAS | Oui | - |
| `latent_image` | La représentation latente initiale qui sert de point de départ à l'échantillonnage. Prend en charge une clé optionnelle `noise_mask` pour le débruitage sélectif, ainsi que les clés optionnelles `downscale_ratio_spacial` et `downscale_ratio_temporal` pour une gestion avancée du latent | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La représentation latente échantillonnée finale après l'achèvement du processus d'échantillonnage. Toutes les clés `downscale_ratio_spacial` ou `downscale_ratio_temporal` provenant du latent d'entrée sont supprimées de cette sortie | LATENT |
| `denoised_output` | Une version débruitée de la sortie lorsque le processus d'échantillonnage produit une prédiction propre intermédiaire (x0), sinon renvoie la même chose que `output`. Lorsqu'elle est disponible, elle représente la meilleure estimation du modèle du latent propre | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
