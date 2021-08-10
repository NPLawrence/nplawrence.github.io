---
permalink: /
title: "Research overview"
excerpt: "About me"
author_profile: true

---
{% assign sup1 = site.author.supervisors[0] %}
{% assign sup2 = site.author.supervisors[1] %}

I'm a PhD candidate in {{ site.author.discipline }} at the {{ site.author.employer }} ({{ site.author.employer_short }}) under the supervision of [{{ sup1.name}}]({{ sup1.url }}) and [{{ sup2.name }}]({{ sup2.url }}). I'm interested in developing control design and tuning methods based on deep reinforcement learning for real-world industrial applications.

Recent publications
======

For a complete list of my papers, please see my [publications list]({{ site.baseurl }}/publications/). {% if site.author.googlescholar %}
  You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include recent_pubs.html %}
