---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true

---
{% assign sup1 = site.author.supervisors[0] %}
{% assign sup2 = site.author.supervisors[1] %}

I recently completed my PhD!

My degree is in {{ site.author.discipline }} at the {{ site.author.employer }} ({{ site.author.employer_short }}) and I studied under the supervision of [{{ sup1.name}}]({{ sup1.url }}) and [{{ sup2.name }}]({{ sup2.url }}).
Here you can find my thesis on [Deep reinforcement learning (RL) agents for industrial control system design](https://open.library.ubc.ca/collections/24/items/1.0430547).
I'm interested in developing actionable control methods based on RL for real-world applications.
The first part of my thesis focuses on the practical implementation of RL and meta-RL for PID tuning.
I later developed a general method for synthesizing stabilizing controllers with any RL algorithm using input-output data.

{% comment %}
News
======

We are organizing a half-day workshop at AdCONIP 2022 on reinforcement learning to be held on August 7th 2022. Further details on the [conference webpage](https://adconip2022.org/workshops/#workshop-2-making-reinforcement-learning-a-practical-technology-for-industrial-control).
{% endcomment %}

Publications
======

Most of my papers are linked to arXiv or a DOI. If you can't find one, feel free to [get in touch](mailto:{{site.author.short_name}} <{{site.author.email}}>). {% if site.author.googlescholar %} You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include pub_list.html %}
