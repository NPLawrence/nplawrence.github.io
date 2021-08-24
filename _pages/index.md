---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true

---
{% assign sup1 = site.author.supervisors[0] %}
{% assign sup2 = site.author.supervisors[1] %}

I'm a PhD candidate in {{ site.author.discipline }} at the {{ site.author.employer }} ({{ site.author.employer_short }}) under the supervision of [{{ sup1.name}}]({{ sup1.url }}) and [{{ sup2.name }}]({{ sup2.url }}). I'm interested in developing actionable control methods based on deep reinforcement learning for real-world applications.

Publications
======

Most of my papers are linked to arXiv or a DOI. If you can't find one, feel free to [get in touch](mailto:{{site.author.short_name}} <{{site.author.email}}>). {% if site.author.googlescholar %} You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include pub_list.html %}
