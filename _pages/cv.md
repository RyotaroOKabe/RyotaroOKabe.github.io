---
layout: archive
title: "CV"
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---

{% include base_path %}
{% assign cv = site.data.cv %}

<p class="cv-download">
  <a class="cv-download__button" href="{{ base_path }}{{ cv.pdf }}">
    <i class="fas fa-file-pdf" aria-hidden="true"></i>
    {{ cv.pdf_label }}
  </a>
  <span class="cv-download__date">Last updated: {{ cv.pdf_date }}</span>
</p>

<section class="cv-section">
  <h2>Education</h2>
  <ul class="cv-list">
    {% for e in cv.education %}
      <li class="cv-entry">
        <div class="cv-entry__main">
          <span class="cv-entry__title">{{ e.degree }}</span>
          <span class="cv-entry__org">{{ e.institution }}, {{ e.location }}</span>
        </div>
        <span class="cv-entry__period">{{ e.period }}</span>
      </li>
    {% endfor %}
  </ul>
  {% if cv.education_notes %}
    <ul class="cv-notes">
      {% for n in cv.education_notes %}<li>{{ n }}</li>{% endfor %}
    </ul>
  {% endif %}
</section>

<section class="cv-section">
  <h2>Experience</h2>
  <ul class="cv-list">
    {% for x in cv.experience %}
      <li class="cv-entry">
        <div class="cv-entry__main">
          <span class="cv-entry__title">{{ x.role }}</span>
          <span class="cv-entry__org">{{ x.org }} ({{ x.detail }}), {{ x.location }}</span>
          {% if x.bullets %}
            <ul class="cv-entry__bullets">
              {% for b in x.bullets %}<li>{{ b }}</li>{% endfor %}
            </ul>
          {% endif %}
        </div>
        <span class="cv-entry__period">{{ x.period }}</span>
      </li>
    {% endfor %}
  </ul>
</section>

<section class="cv-section">
  <h2>Honors &amp; Awards</h2>
  <ul class="cv-list">
    {% for a in cv.awards %}
      <li class="cv-entry cv-entry--compact">
        <div class="cv-entry__main">{{ a.text }}</div>
        <span class="cv-entry__period">{{ a.date }}</span>
      </li>
    {% endfor %}
  </ul>
</section>

<section class="cv-section">
  <h2>Skills</h2>
  <ul class="cv-notes">
    {% for s in cv.skills %}
      <li><strong>{{ s.category }}:</strong> {{ s.items }}</li>
    {% endfor %}
  </ul>
</section>

<section class="cv-section">
  <h2>Community Service</h2>
  <ul class="cv-notes">
    {% for c in cv.community_service %}<li>{{ c }}</li>{% endfor %}
  </ul>
</section>

<section class="cv-section">
  <h2>Publications &amp; Presentations</h2>
  <p>
    Full lists are on the <a href="{{ base_path }}/publications/">Publications</a>
    and <a href="{{ base_path }}/talks/">Talks</a> pages.
  </p>
</section>

<div class="cv-embed">
  <embed src="{{ base_path }}{{ cv.pdf }}" type="application/pdf" width="100%" height="800px" />
</div>
