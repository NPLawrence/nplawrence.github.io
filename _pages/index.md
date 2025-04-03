---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true

---

I recently joined [Mesbah Lab](https://www.mesbahlab.com) at UC Berkeley as a postdoc! 

My recent work develops a complementary framework inspired by deep reinforcement learning and model predictive control.
A more unified perspective of these two areas would make RL more appealing for real-world applications while also making MPC more flexible and scalable under general learning algorithms.
Ultimately, I want to create safe decision-making technologies that "just work" in response to high-level commands.


My PhD is in Applied Mathematics from UBC where I worked with [Philip Loewen](https://personal.math.ubc.ca/~loew/) and [Bhushan Gopaluni](https://dais.chbe.ubc.ca).
Here you can find my thesis on [Deep reinforcement learning agents for industrial control system design](https://open.library.ubc.ca/collections/24/items/1.0430547).
The first part of my thesis focuses on the practical implementation of RL and meta-RL for PID tuning in the context of industrial process control.
I later developed a general method for synthesizing stabilizing controllers with any RL algorithm using input-output data.


{% comment %}
News
======

Upper Bound 2024 MPC tutorial: Slides and code [here](https://nplawrence.com/RL-MPC-tutorial/)

I recently completed my PhD!

We are organizing a half-day workshop at AdCONIP 2022 on reinforcement learning to be held on August 7th 2022. Further details on the [conference webpage](https://adconip2022.org/workshops/#workshop-2-making-reinforcement-learning-a-practical-technology-for-industrial-control).
{% endcomment %}

Publications
======

Most of my papers are linked to arXiv or a DOI. If you can't find one, feel free to [get in touch](mailto:{{site.author.short_name}} <{{site.author.email}}>). {% if site.author.googlescholar %} You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include pub_list.html %}
